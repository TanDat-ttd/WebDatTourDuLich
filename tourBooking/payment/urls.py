# payment/urls.py
from django.urls import path
from . import views
from main.models import Tour

urlpatterns = [
    path('payment/<int:tour_id>/', views.destination_payment, name='destination_payment'),  # Trang thanh toán tích hợp form
    path('payment/success/', views.payment_success, name='payment_success'),  # Thanh toán thành công

    path('confirm/<uuid:booking_id>/', views.confirm_booking, name='confirm_booking'),
    path('failed/', views.payment_failed, name='payment_failed'),  # Thanh toán thất bại
]