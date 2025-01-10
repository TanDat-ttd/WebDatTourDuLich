from django.shortcuts import render, get_object_or_404, redirect
from .models import DiscountCode, Booking
from main.models import Tour, Schedule
from django.contrib import messages
from django.core.mail import send_mail
from collections import defaultdict
from django.conf import settings
from datetime import date
import logging
from django.http import HttpResponse
from django.utils.html import format_html
from django.urls import reverse


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

    if request.method == "POST":
        # Lấy thông tin từ form
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()
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

        # Kiểm tra số lượng vé không vượt quá số lượng chỗ còn lại
        if number_of_people > tour.remaining_capacity:
            messages.error(request, "Số lượng vé đặt vượt quá số chỗ trống còn lại của tour!")
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
            'number_of_people': number_of_people,
            'total_price': float(total_price),
            'tour_name': tour.name,
            'payment_method': payment_method,
        }
        messages.success(request, "Đặt tour thành công!")
        return redirect('payment_success')

    # Hiển thị thông tin tour & form đặt vé
    return render(request, "destination_payment.html", {
        "tour": tour,
        "grouped_schedules": grouped_schedules,
    })


def payment_success(request):
    # Lấy thông tin đặt tour từ session
    booking = request.session.get('booking')
    if not booking:
        messages.error(request, "Không thể truy cập trực tiếp trang này. Vui lòng hoàn tất thanh toán trước!")
        return redirect('index')  # Redirect đến trang chính nếu không có dữ liệu session

    try:
        # Lấy thông tin tour đã đặt
        tour = get_object_or_404(Tour, name=booking['tour_name'])

        # Kiểm tra nếu số lượng vé đặt vượt quá chỗ còn lại
        if int(booking['number_of_people']) > tour.remaining_capacity:
            messages.error(request,
                           f"Số lượng vé đặt ({booking['number_of_people']}) vượt quá số lượng chỗ trống còn lại ({tour.remaining_capacity}) của tour!")
            return redirect('destination_payment', tour_id=tour.id)

        # Tạo hoặc lấy booking trong database
        new_booking, created = Booking.objects.get_or_create(
            tour=tour,
            first_name=booking['first_name'],
            last_name=booking['last_name'],
            email=booking['email'],
            phone=booking['phone'],
            address=booking['address'],
            number_of_people=booking['number_of_people'],
            total_price=booking['total_price'],
            defaults={
                'payment_method': booking['payment_method'],
                'status': 'paid',  # Đặt trạng thái mặc định là "đã thanh toán"
            },
        )

        # Nếu booking được tạo mới, giảm số lượng chỗ còn lại
        if created:
            tour.remaining_capacity -= new_booking.number_of_people
            # Đảm bảo giá trị remaining_capacity không âm
            if tour.remaining_capacity < 0:
                tour.remaining_capacity = 0
            tour.save()

            # Gửi email xác nhận cho người dùng
            confirm_url = request.build_absolute_uri(
                reverse('confirm_booking', args=[new_booking.id])
            )
            subject = "Xác nhận thanh toán tour du lịch"
            message = f"""
            Chào {new_booking.first_name} {new_booking.last_name},

            Mã đặt tour của bạn: {new_booking.booking_code}

            Cảm ơn bạn đã đặt tour "{new_booking.tour.name}" với chúng tôi!
            Số tiền đã thanh toán: {new_booking.total_price:.2f} VNĐ

            Vui lòng nhấn vào nút dưới đây để xác nhận đặt tour của bạn:
            {confirm_url}

            Trân trọng,
            Đội ngũ quản lý Tour
            """
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [new_booking.email],
                fail_silently=False
            )
        else:
            # Nếu booking đã tồn tại, thông báo cho người dùng
            messages.info(request, "Bạn đã đặt tour này trước đó. Không thể đặt lại!")

    except Exception as e:
        # Ghi log lỗi và hiển thị thông báo chung
        logger.error(f"Lỗi xảy ra trong quá trình xử lý thanh toán: {e}")
        messages.error(request, "Có lỗi xảy ra khi xử lý thông tin thanh toán. Vui lòng liên hệ chúng tôi!")
        return redirect('destination_payment', tour_id=tour.id)

    # Xóa session booking (đảm bảo không truy cập lại mà không qua thanh toán)
    del request.session['booking']

    # Trả về trang xác nhận đặt tour thành công
    return render(request, "success.html", {"booking": new_booking})



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



def confirm_booking(request, booking_id):
    try:
        # Tìm booking dựa vào ID từ URL
        booking = get_object_or_404(Booking, id=booking_id)

        # Kiểm tra trạng thái và cập nhật
        if booking.status != 'confirmed':
            booking.status = 'confirmed'
            booking.save()
            messages.success(request, "Đặt tour của bạn đã được xác nhận thành công!")
        else:
            messages.info(request, "Đặt tour này đã được xác nhận trước đó.")
    except Exception as e:
        logger.error(f"Lỗi khi xác nhận booking: {e}")
        return HttpResponse("Có lỗi xảy ra khi xác nhận. Vui lòng thử lại sau!", status=500)

    # Redirect về trang thành công hoặc trang khác
    return redirect('payment_success')



