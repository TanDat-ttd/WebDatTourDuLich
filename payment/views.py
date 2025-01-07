# payment/views.py
from django.shortcuts import render, redirect
from .models import DiscountCode
from main.models import Tour  # Đảm bảo không import từ tour.models


def payment(request, tour_id):
    # Lấy thông tin tour từ ID
    tour = Tour.objects.get(id=tour_id)

    if request.method == "POST":
        # Lấy thông tin từ Form
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        number_of_people = int(request.POST.get("number_of_people", 1))  # Giá trị mặc định là 1
        discount_code = request.POST.get("discount_code")
        payment_method = request.POST.get("payment_method")

        # Tính tổng giá tiền
        total_price = tour.price * number_of_people

        # Xử lý mã giảm giá nếu có
        if discount_code:
            try:
                discount = DiscountCode.objects.get(code=discount_code)
                if discount.is_valid():
                    discount_amount = discount.calculate_discount(total_price)
                    total_price -= discount_amount
                    discount.use_discount()  # Giảm lượt sử dụng
                else:
                    return render(request, "payment.html", {
                        "tour": tour,
                        "error": "Mã giảm giá không hợp lệ!"
                    })
            except DiscountCode.DoesNotExist:
                return render(request, "payment.html", {
                    "tour": tour,
                    "error": "Mã giảm giá không tồn tại!"
                })

        # Xử lý thanh toán
        if total_price > 0:  # Giả lập thanh toán thành công nếu tổng giá > 0
            # Thành công
            return redirect('payment_success')
        else:
            # Thất bại
            return redirect('payment_failed')

    # Hiển thị form nếu không phải POST
    return render(request, "payment.html", {"tour": tour})
# payment/views.py
# payment/views.py
def payment_success(request):
    booking = request.session.get('booking')  # Cần lưu booking vào session ở bước xử lý thanh toán
    return render(request, "success.html", {"booking": booking})

# payment/views.py
def payment_failed(request):
    return render(request, "failed.html", {})