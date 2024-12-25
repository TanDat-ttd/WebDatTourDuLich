from django.urls import path, include
from . import views

urlpatterns = [
    path('book/<int:tour_id>/', views.book_tour, name='book_tour'),
    path('booking/', include('booking.urls')),  # Trong urlpatterns
    path('<int:booking_id>/', views.checkout, name='checkout'),
    path('success/<int:booking_id>/', views.payment_success, name='payment_success'),
    path('failed/', views.payment_failed, name='payment_failed'),
]