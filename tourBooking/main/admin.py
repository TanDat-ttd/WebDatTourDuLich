# main/admin.py
from django.contrib import admin
from .models import Tour, Schedule


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "start_date", "end_date", "price", "remaining_capacity")
    search_fields = ("name", "code")
    list_filter = ("start_date", "end_date")


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("tour", "day", "period", "activity")
    list_filter = ("day", "period", "tour")  # Bộ lọc lịch trình theo Tour, Ngày, Buổi
    search_fields = ("activity",)  # Tìm kiếm theo nội dung hoạt động