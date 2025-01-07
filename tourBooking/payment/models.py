from django.db import models
from django.utils.timezone import now


class Tour(models.Model):
    name = models.CharField(max_length=255)  # Tên tour
    description = models.TextField()  # Mô tả về tour (lịch trình, chi tiết, etc.)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá tour
    duration = models.IntegerField()  # Số ngày tour (3 ngày, 5 ngày,...)
    start_date = models.DateField()  # Ngày bắt đầu tour
    end_date = models.DateField()  # Ngày kết thúc tour
    available_slots = models.IntegerField()  # Số chỗ trống còn lại cho tour
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian tạo tour
    updated_at = models.DateTimeField(auto_now=True)  # Thời gian chỉnh sửa tour

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date})"

    def is_available(self):
        """Kiểm tra xem tour còn slot hay không."""
        return self.available_slots > 0


class DiscountCode(models.Model):
    PERCENTAGE = 'PERCENTAGE'
    FIXED = 'FIXED'
    DISCOUNT_TYPE_CHOICES = [
        (PERCENTAGE, 'Percentage'),
        (FIXED, 'Fixed'),
    ]

    code = models.CharField(max_length=50, unique=True)  # Mã giảm giá
    discount_type = models.CharField(
        max_length=20,
        choices=DISCOUNT_TYPE_CHOICES,
        default=PERCENTAGE,
    )  # Loại giảm: PERCENTAGE/FIXED
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)  # Giá trị giảm
    max_uses = models.PositiveIntegerField(null=True, blank=True)  # Số lần dùng tối đa
    uses_left = models.PositiveIntegerField(null=True, blank=True)  # Số lần còn lại
    min_order_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Giá trị tối thiểu
    valid_from = models.DateTimeField(default=now)  # Ngày có hiệu lực
    valid_until = models.DateTimeField()  # Ngày hết hạn
    eligible_tours = models.ManyToManyField(Tour, related_name="discounts", blank=True)  # Mối quan hệ với Tour
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    def is_valid(self):
        """
        Kiểm tra xem mã giảm giá còn hiệu lực không:
        - Hiệu lực về thời gian.
        - Còn lượt sử dụng.
        """
        if now() < self.valid_from or now() > self.valid_until:
            return False
        if self.uses_left is not None and self.uses_left <= 0:
            return False
        return True