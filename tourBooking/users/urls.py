from django.urls import path
from . import views  # Import các views liên quan đến app này

urlpatterns = [
    path('login/', views.login, name='login'),  # Đường dẫn /auth/login/
    path('register/', views.register, name='register'),  # Đường dẫn /auth/register/
]