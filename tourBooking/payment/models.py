from django.db import models
from django.utils.timezone import now


# Loại giảm giá
class DiscountType(models.TextChoices):
    PERCENTAGE = 'PERCENTAGE', 'Percentage'
    FIXED = 'FIXED', 'Fixed Amount'


class DiscountCodeManager(models.Manager):
    def active(self):
        """Trả về danh sách mã giảm giá đang hoạt động."""
        return self.filter(valid_from__lte=now(), valid_until__gte=now(), uses_left__gt=0)

    def expired(self):
        """Trả về danh sách mã giảm giá đã hết hạn."""
        return self.filter(valid_until__lt=now())

    def used_up(self):
        """Trả về danh sách mã giảm giá đã hết lượt sử dụng."""
        return self.filter(uses_left=0)


class DiscountCode(models.Model):
    # Mã giảm giá
    code = models.CharField(max_length=50, unique=True)
    # Loại giảm (phần trăm hoặc giá cố định)
    discount_type = models.CharField(max_length=20, choices=DiscountType.choices, default=DiscountType.PERCENTAGE)
    # Giá trị giảm (10% hoặc 50000 VNĐ tùy loại)
    discount_value = models.FloatField()
    # Giá trị giảm tối đa (nếu áp dụng cho loại PERCENTAGE)
    max_discount_value = models.FloatField(null=True, blank=True)
    # Số lần tối đa có thể sử dụng
    max_uses = models.PositiveIntegerField()
    # Số lần còn lại có thể sử dụng
    uses_left = models.PositiveIntegerField(default=0)
    # Số lần đã sử dụng
    times_used = models.PositiveIntegerField(default=0)
    # Ngày bắt đầu hiệu lực
    valid_from = models.DateTimeField(default=now)
    # Ngày hết hạn
    valid_until = models.DateTimeField()
    # Ghi chú bổ sung
    description = models.TextField(null=True, blank=True)
    # Thời gian tạo và cập nhật
    created_at = models.DateTimeField(auto_now_add=True)  # Đã sửa lỗi: chỉ giữ auto_now_add
    updated_at = models.DateTimeField(auto_now=True)

    # Gán DiscountCodeManager custom
    objects = DiscountCodeManager()

    def is_valid(self):
        """Kiểm tra mã giảm giá có hợp lệ hay không."""
        return self.uses_left > 0 and self.valid_from <= now() <= self.valid_until

    def is_expired(self):
        """Kiểm tra mã giảm giá đã hết hạn hay chưa."""
        return now() > self.valid_until

    def get_status(self):
        """Trả về trạng thái mã giảm giá: Active, Expired, Used Up."""
        if self.is_expired():
            return "Expired"
        if self.uses_left <= 0:
            return "Used Up"
        return "Active"

def use_discount(self, user_email=None):
    """Cập nhật việc sử dụng mã giảm giá."""
    if not self.is_valid():
        raise ValueError("Mã giảm giá không hợp lệ hoặc đã hết hạn.")

    if self.uses_left <= 0:
        raise ValueError("Mã giảm giá đã hết số lần sử dụng.")

    # Trừ lượt và ghi lại ai đã sử dụng (nếu có)
    self.uses_left -= 1
    self.times_used += 1
    if user_email:
        self.description = f"Used by {user_email}"
    self.save()

    def calculate_discount(self, total_amount):
        """
        Tính số tiền giảm giá dựa trên tổng giá trị đơn hàng.
        total_amount: Tổng giá trị đơn hàng.
        """
        if self.discount_type == DiscountType.PERCENTAGE:
            discount = total_amount * (self.discount_value / 100)
            if self.max_discount_value:  # Giới hạn mức giảm giá tối đa
                discount = min(discount, self.max_discount_value)
            return discount
        elif self.discount_type == DiscountType.FIXED:
            return min(self.discount_value, total_amount)
        return 0

    def __str__(self):
        return f"{self.code} ({self.discount_type})"