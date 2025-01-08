from django.shortcuts import render, get_object_or_404, redirect
from .models import DiscountCode
from main.models import Tour
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Hàm xử lý thanh toán
# Hàm xử lý thanh toán
def destination_payment(request, tour_id):
    # Lấy thông tin tour
    tour = get_object_or_404(Tour, id=tour_id)

    if request.method == "POST":
        # Lấy thông tin form
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone").strip()
        address = request.POST.get("address", "").strip()
        date_of_travel = request.POST.get("date")
        number_of_people = int(request.POST.get("tickets", 1))
        discount_code = request.POST.get("coupon", "").strip()
        payment_method = request.POST.get("payment_method", "cash").strip()

        # Tổng giá trị ban đầu
        total_price = tour.price * number_of_people

        # Xử lý mã giảm giá nếu có
        if discount_code:
            try:
                discount = DiscountCode.objects.get(code=discount_code)
                if discount.is_valid():
                    discount_amount = discount.calculate_discount(total_price)
                    total_price -= discount_amount
                    discount.use_discount()
                else:
                    messages.error(request, "Mã giảm giá hết hạn hoặc không còn khả dụng!")
            except DiscountCode.DoesNotExist:
                messages.error(request, "Mã giảm giá không tồn tại!")

        # Xử lý thanh toán
        if total_price > 0:
            # Nếu thanh toán hợp lệ, lưu thông tin booking vào session
            request.session['booking'] = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'address': address,
                'date_of_travel': date_of_travel,
                'number_of_people': number_of_people,
                'total_price': float(total_price),  # Chuyển Decimal thành float
                'tour_name': tour.name,
                'payment_method': payment_method,
            }
            messages.success(request, "Đặt tour thành công!")
            return redirect('payment_success')
        else:
            messages.error(request, "Có lỗi xảy ra trong quá trình thanh toán. Giá trị thanh toán không hợp lệ!")

    # Render trang chi tiết nếu không có POST
    return render(request, "destination_payment.html", {"tour": tour})

def payment_success(request):
    # Lấy dữ liệu từ session
    booking = request.session.get('booking')
    if not booking:
        return redirect('destination_payment')  # Quay về trang đặt tour nếu không có dữ liệu.

    # Chuẩn bị thông tin email
    subject = "Xác nhận thanh toán tour du lịch thành công"
    message = f"""
    Chào {booking['first_name']} {booking['last_name']},
    
    Cảm ơn bạn đã đặt tour "{booking['tour_name']}" với chúng tôi!
    Dưới đây là thông tin mà bạn đã cung cấp:
    
    - Số lượng vé: {booking['number_of_people']}
    - Tổng số tiền: {booking['total_price']:,.2f} VNĐ
    - Số điện thoại: {booking['phone']}
    - Địa chỉ: {booking['address']}
    - Ngày đi: {booking['date_of_travel']}
    - Phương thức thanh toán: {booking['payment_method']}
    
    Xin hãy liên hệ nếu bạn cần thêm thông tin. Chúng tôi hy vọng bạn sẽ có chuyến đi tuyệt vời!
    """

    recipient_email = booking['email']

    try:
        # Gửi email
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # Địa chỉ email người gửi (được cấu hình trong settings)
            [recipient_email],  # Danh sách người nhận
            fail_silently=False,
        )
        # Ghi log hoặc cài đặt thông báo gửi thành công (tùy chọn)
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")  # Bạn nên log lỗi trong hệ thống log của Django

    return render(request, "success.html", {"booking": booking})  # Hiển thị trang thanh toán thành công
def payment_failed(request):
    return render(request, "failed.html", {})

