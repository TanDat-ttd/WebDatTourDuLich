
from django.urls import path
from . import views  # Import views của app

urlpatterns = [
    path('tour', views.tour, name='tour'),  # URL trỏ đến view tour
    path('tour/<int:id>/', views.tour_detail, name='tour_detail'),  # Trang chi tiết tour


]   
