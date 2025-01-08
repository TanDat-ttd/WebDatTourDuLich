from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    plain_password = models.CharField(max_length=128, blank=True, null=True)  # Thêm trường mật khẩu không mã hóa

    def __str__(self):
        return self.user.username
