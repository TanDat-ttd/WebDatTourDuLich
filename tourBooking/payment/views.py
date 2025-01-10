from django.shortcuts import render, get_object_or_404, redirect
from .models import DiscountCode
from main.models import Tour, Schedule
from django.contrib import messages
from django.core.mail import send_mail
from collections import defaultdict
from django.conf import settings
from datetime import date
import logging

# Thiết lập logger để theo dõi lỗi
logger = logging.getLogger(__name__)


def destination_payment(request, tour_id):
    # Lấy thông tin của Tour hoặc trả về 404 nếu không tồn tại
    tour = get_object_or_404(Tour, id=tour_id)

    # Lấy lịch trình của Tour, sắp xếp theo ngày và buổi
    schedules = tour.schedules.all().order_by('day', 'period')
    grouped_schedules = defaultdict(list)
    for schedule in schedules:
        grouped_schedules[schedule.day].append(schedule)

    if not schedules.exists():
        # Hiển thị thông báo nếu lịch trình không có dữ liệu
        messages.warning(request, "Không có lịch trình chi tiết nào cho tour này.")
    else:
        # Nhóm dữ liệu lịch trình theo ngày
        for schedule in schedules:
            grouped_schedules[schedule.day].append(schedule)

    if request.method == "POST":
        # Lấy thông tin từ form
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()
        date_of_travel = request.POST.get("date", "").strip()
        number_of_people = int(request.POST.get("tickets", 1))
        discount_code = request.POST.get("coupon", "").strip()
        payment_method = request.POST.get("payment_method", "cash").strip()

        # Kiểm tra thông tin nhập từ user, trả lỗi nếu thiếu dữ liệu
        if not first_name or not last_name or not email:
            messages.error(request, "Vui lòng điền đầy đủ thông tin cá nhân.")
            return redirect('destination_payment', tour_id=tour_id)

        if number_of_people < 1:
            messages.error(request, "Số lượng vé phải lớn hơn hoặc bằng 1.")
            return redirect('destination_payment', tour_id=tour_id)

        try:
            if date_of_travel and date.fromisoformat(date_of_travel) < date.today():
                messages.error(request, "Ngày đi không hợp lệ. Ngày đi phải ở tương lai.")
                return redirect('destination_payment', tour_id=tour_id)
        except ValueError:
            messages.error(request, "Định dạng ngày đi không đúng. Vui lòng nhập đúng định dạng!")
            return redirect('destination_payment', tour_id=tour_id)

        # Tính toán tổng giá ban đầu
        total_price = tour.price * number_of_people

        # Xử lý mã giảm giá nếu được cung cấp
        if discount_code:
            try:
                discount = DiscountCode.objects.get(code=discount_code)
                if discount.is_valid():
                    discount_amount = discount.calculate_discount(total_price)
                    total_price -= discount_amount
                    discount.use_discount()
                    messages.success(request, f"Áp dụng mã giảm giá thành công! Đã giảm {discount_amount} VNĐ.")
                else:
                    messages.error(request, "Mã giảm giá đã hết hạn hoặc không còn khả dụng!")
            except DiscountCode.DoesNotExist:
                messages.error(request, "Mã giảm giá không hợp lệ!")

        # Kiểm tra tổng giá trị thanh toán
        if total_price <= 0:
            messages.error(request, "Có lỗi xảy ra trong quá trình xử lý thanh toán. Tổng giá trị không hợp lệ!")
            return redirect('destination_payment', tour_id=tour_id)

        # Lưu thông tin đặt tour vào session
        request.session['booking'] = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'address': address,
            'date_of_travel': date_of_travel,
            'number_of_people': number_of_people,
            'total_price': float(total_price),
            'tour_name': tour.name,
            'payment_method': payment_method,
        }
        messages.success(request, "Đặt tour thành công!")
        return redirect('payment_success')

    return render(request, "destination_payment.html", {
        "tour": tour,
        "grouped_schedules": grouped_schedules,  # Truyền lịch trình nhóm theo ngày
    })


def payment_success(request):
    # Lấy thông tin đặt tour từ session
    booking = request.session.get('booking')
    if not booking:
        messages.error(request, "Không tìm thấy thông tin đặt tour. Vui lòng thử lại!")
        return redirect('destination_payment')

    # Chuẩn bị nội dung email để gửi cho khách hàng
    subject = "Xác nhận thanh toán tour du lịch"
    message = f"""
    Chào {booking['first_name']} {booking['last_name']},
    
    Cảm ơn bạn đã đặt tour "{booking['tour_name']}" với chúng tôi!
    Dưới đây là thông tin bạn đã cung cấp:

    - Số lượng vé: {booking['number_of_people']}
    - Tổng số tiền: {booking['total_price']:,.2f} VNĐ
    - Số điện thoại: {booking['phone']}
    - Địa chỉ: {booking['address']}
    - Ngày đi: {booking['date_of_travel']}
    - Phương thức thanh toán: {booking['payment_method']}
    
    Xin hãy liên hệ với chúng tôi nếu có bất kỳ câu hỏi nào. Chúc bạn một chuyến đi vui vẻ!
    """

    recipient_email = booking['email']

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient_email],
            fail_silently=False,
        )
        messages.success(request, "Xác nhận đã được gửi qua email của bạn!")
    except Exception as e:
        logger.error(f"Lỗi khi gửi email xác nhận: {e}")
        messages.error(request, "Có lỗi xảy ra khi gửi email xác nhận. Vui lòng liên hệ chúng tôi qua hotline.")

    # Trả về trang xác nhận thành công
    return render(request, "success.html", {"booking": booking})


def payment_failed(request):
    return render(request, "failed.html", {})


def tour_schedule_view(request, tour_id):
    # Lấy thông tin Tour cùng danh sách lịch trình
    tour = get_object_or_404(Tour, id=tour_id)
    schedules = tour.schedules.all().order_by('day', 'period')

    return render(request, 'destination_payment.html', {
        'tour': tour,
        'schedules': schedules,
    })

