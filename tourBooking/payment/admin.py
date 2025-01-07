from django.contrib import admin
from .models import DiscountCode  # Import model DiscountCode


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'uses_left', 'valid_from', 'valid_until')
    search_fields = ('code',)
    list_filter = ('discount_type', 'valid_from', 'valid_until')

"""
- **list_display**: Hiển thị các cột thông tin quan trọng trong bảng giảm giá.
- **search_fields**: Cho phép tìm kiếm mã giảm giá theo **code**.
- **list_filter**: Thêm bộ lọc theo loại giảm giá và thời gian hiệu lực.
"""

