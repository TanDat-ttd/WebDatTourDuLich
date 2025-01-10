from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Kiểm tra Email',  # Chủ đề email
    'Đây là email kiểm tra gửi từ Django.',  # Nội dung email
    settings.EMAIL_HOST_USER,  # Email người gửi
    ['truongdat531@gmail.com'],  # Email người nhận
    fail_silently=False,
)