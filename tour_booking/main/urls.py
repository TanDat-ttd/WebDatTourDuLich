from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Trang chủ
    path('about/', views.about, name='about'),  # Trang about
]