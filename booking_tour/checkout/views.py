from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Booking, Tour, DiscountCode

# Create your views here.
def index(request):
   return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blog_detail(request):
    return render(request, 'blog_detail.html')

def contact(request):
    return render(request, 'contact.html')

def destination(request):
    return render(request, 'destination.html')

def destination2(request):
    return render(request, 'destination2.html')

def destination3(request):
    return render(request, 'destination3.html')

def destination_BinhDinh(request):
    return render(request, 'destination_BinhDinh.html')

def destination_CaoBang(request):
    return render(request, 'destination_CaoBang.html')

def destination_DaLat(request):
    return render(request, 'destination_DaLat.html')

def destination_HaNoi(request):
    return render(request, 'destination_HaNoi.html')

def destination_HoiAn(request):
    return render(request, 'destination_HoiAn.html')

def destination_NinhBinh(request):
    return render(request, 'destination_NinhBinh.html')

def destination_VinhHaLong(request):
    return render(request, 'destination_VinhHaLong.html')

def destination_VungTau(request):
    return render(request, 'destination_VungTau.html')

def detail(request):
    return render(request, 'detail.html')

def faq(request):
    return render(request, 'faq.html')

def gallery(request):
    return render(request, 'gallery.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def tour(request):
    return render(request, 'tour.html')

def payment(request):
    return render(request, 'checkout/payment.html')


def payment_view(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    error = None

    if request.method == 'POST':
        # Lấy dữ liệu từ form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST.get('address', '')
        payment_method = request.POST['payment_method']
        number_of_people = int(request.POST.get('number_of_people', 1))
        discount_code_input = request.POST.get('discount_code', '').strip()

        # Tính tổng tiền ban đầu
        total_price = tour.price * number_of_people
        discount_code = None

        # Kiểm tra mã giảm giá (nếu có)
        if discount_code_input:
            try:
                discount_code = DiscountCode.objects.get(code=discount_code_input, active=True)
                discount_amount = total_price * (discount_code.discount_percentage / 100)
                total_price -= discount_amount
            except DiscountCode.DoesNotExist:
                error = 'Mã giảm giá không hợp lệ hoặc đã hết hạn.'

        # Nếu không có lỗi, lưu thông tin đặt tour
        if not error:
            booking = Booking.objects.create(
                tour=tour,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email=email,
                address=address,
                number_of_people=number_of_people,
                discount_code=discount_code_input if discount_code else None,
                total_price=total_price,
                payment_method=payment_method,
            )
            # Chuyển đến trang thành công
            return redirect(reverse('success', args=[booking.id]))

    return render(request, 'payment.html', {'tour': tour, 'error': error})


def success_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'success.html', {'booking': booking})


def failed_view(request):
    return render(request, 'failed.html')

def apply_discount(request):
    if request.method == "POST":
        tour_id = request.POST.get('tour_id')
        code = request.POST.get('code')

        try:
            tour = Tour.objects.get(id=tour_id)
            original_price = tour.price
        except Tour.DoesNotExist:
            return JsonResponse({'valid': False, 'error': 'Tour không tồn tại!'})

        try:
            discount = DiscountCode.objects.get(code=code, active=True)
            discount_value = original_price * (discount.discount_percentage / 100)
            discounted_price = original_price - discount_value
        except DiscountCode.DoesNotExist:
            return JsonResponse({'valid': False, 'error': 'Mã giảm giá không hợp lệ hoặc đã hết hạn!'})

        return JsonResponse({'valid': True, 'original_price': original_price, 'discounted_price': discounted_price})

    return JsonResponse({'valid': False, 'error': 'Request không hợp lệ!'})







