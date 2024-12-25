from django.db import models
import datetime


class Tour(models.Model):
    name = models.CharField(max_length=200)  # Tên tour
    code = models.CharField(max_length=20, unique=True, default="DEFAULT_CODE")  # Thêm mặc định
    details = models.TextField(blank=True, null=True, default="")  # Chi tiết tour
    start_date = models.DateField(default=datetime.date.today)  # Ngày bắt đầu
    end_date = models.DateField(default=datetime.date.today)  # Ngày kết thúc
    location = models.CharField(max_length=200)  # Địa điểm
    image = models.ImageField(upload_to='tour_images/', blank=True, null=True, default=None)  # Hình ảnh
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá

    def __str__(self):
        return self.name


class DiscountCode(models.Model):
    code = models.CharField(max_length=20, unique=True)  # Mã giảm giá
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # % giảm giá (e.g., 10%)
    active = models.BooleanField(default=True)  # Trạng thái mã giảm giá (còn hiệu lực hay không)
    amount = models.PositiveIntegerField(default=0)  # Số lượng mã giảm giá khả dụng
    terms_conditions = models.TextField(blank=True, null=True, default="")  # Điều khoản và điều kiện áp dụng
    start_date = models.DateField(default=datetime.date.today)  # Ngày bắt đầu áp dụng mã giảm giá
    end_date = models.DateField(blank=True, null=True)  # Ngày kết thúc áp dụng mã giảm giá

    def __str__(self):
        return self.code


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)  # Tour liên kết
    first_name = models.CharField(max_length=100)  # Họ
    last_name = models.CharField(max_length=100)  # Tên
    phone_number = models.CharField(max_length=15)  # Số điện thoại
    email = models.EmailField()  # Email
    address = models.TextField(blank=True, null=True, default="")  # Địa chỉ
    number_of_people = models.PositiveIntegerField()  # Số người
    discount_code = models.CharField(max_length=20, blank=True, null=True,
                                     default=None)  # Mã giảm giá đã áp dụng (nếu có)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Tổng tiền sau giảm giá
    payment_method = models.CharField(
        max_length=20,
        choices=[('credit_card', 'Credit Card'), ('cod', 'COD'), ('bank_transfer', 'Bank Transfer')]
    )  # Phương thức thanh toán
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian đặt

    def __str__(self):
        return f"Booking for {self.tour.name} by {self.first_name} {self.last_name}"