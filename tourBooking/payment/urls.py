# payment/urls.py
from django.urls import path
from . import views
from main.models import Tour

urlpatterns = [
    path('<int:tour_id>/', views.payment, name='payment'),  # Trang thanh toán
    path('success/', views.payment_success, name='payment_success'),  # Thanh toán thành công
    path('failed/', views.payment_failed, name='payment_failed'),  # Thanh toán thất bại
]