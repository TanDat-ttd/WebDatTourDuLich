# main/models.py
from django.db import models
import uuid  # Thư viện để tạo mã UUID nếu cần
from django.templatetags.static import static


class Tour(models.Model):
    code = models.CharField(max_length=10, unique=True, default=None)  # Mã tour
    name = models.CharField(max_length=255)  # Tên của tour
    description = models.TextField(null=True, blank=True)  # Mô tả tour
    start_date = models.DateField()  # Ngày bắt đầu
    end_date = models.DateField()  # Ngày kết thúc
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá tour
    capacity = models.PositiveIntegerField()  # Sức chứa tối đa
    remaining_capacity = models.PositiveIntegerField()  # Chỗ trống còn lại
    image = models.ImageField(upload_to='tour_images/', null=True, blank=True)  # Hình ảnh tour
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian tạo
    updated_at = models.DateTimeField(auto_now=True)  # Thời gian cập nhật

    def save(self, *args, **kwargs):
        """Tự động tạo mã tour nếu chưa có."""
        if not self.code:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_code():
        """Tạo mã tour duy nhất."""
        return str(uuid.uuid4()).split('-')[0].upper()  # Ví dụ: '1A2B3C'

    def __str__(self):
        return f"{self.name} ({self.code})"

    def is_available(self):
        """Kiểm tra Tour còn chỗ không."""
        return self.remaining_capacity > 0

    def duration_days(self):
        """Tính tổng số ngày tour diễn ra."""
        return (self.end_date - self.start_date).days + 1
    
    def get_image_url(self):
        """Lấy URL đầy đủ của ảnh."""
        if self.image:
            return self.image.url
        # Nếu không có ảnh, trả về đường dẫn ảnh mặc định
        return static('images/default_tour.jpg')

    def save(self, *args, **kwargs):
        # Đảm bảo không cho phép remaining_capacity < 0
        if self.remaining_capacity < 0:
            self.remaining_capacity = 0
        super().save(*args, **kwargs)


# Thêm model Schedule
class Schedule(models.Model):
    tour = models.ForeignKey(Tour, related_name="schedules", on_delete=models.CASCADE)  # Liên kết với Tour
    day = models.PositiveIntegerField()  # Ngày thứ mấy trong lịch trình
    period = models.CharField(
        max_length=50,
        choices=[("Sáng", "Sáng"), ("Chiều", "Chiều"), ("Tối", "Tối")],
    )  # Buổi: Sáng / Chiều / Tối
    activity = models.TextField()  # Nội dung hoạt động

    def __str__(self):
        return f"Ngày {self.day} ({self.period}): {self.activity} - {self.tour.name or 'Không có'}"

    class Meta:
        verbose_name = "Lịch trình"
        verbose_name_plural = "Lịch trình"
        ordering = ["tour", "day", "period"]  # Sắp xếp theo Tour -> Ngày -> Buổi


