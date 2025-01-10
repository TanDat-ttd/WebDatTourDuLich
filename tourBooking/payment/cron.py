from django_cron import CronJobBase, Schedule
from django.utils.timezone import localtime, now
from django.core.mail import send_mail
from payment.models import Booking
from main.models import Tour


class DeleteUnconfirmedBookingsJob(CronJobBase):
    RUN_EVERY_MINS = 5  # Chạy mỗi 5 phút

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'payment.delete_unconfirmed_bookings'  # Mã duy nhất cho cronjob này

    def do(self):
        current_time = localtime(now())  # Lấy thời gian hiện tại
        # Lọc các booking đã quá hạn và chưa xác nhận
        expired_bookings = Booking.objects.filter(
            status='paid',
            confirmation_deadline__lt=current_time
        )

        for booking in expired_bookings:
            # Gửi email thông báo trước khi xóa
            send_mail(
                subject=f"Hủy đặt Tour {booking.tour.name}",
                message=f"""
                Xin chào {booking.first_name} {booking.last_name},

                Chúng tôi rất tiếc thông báo rằng tour "{booking.tour.name}" đã bị hủy vì bạn không xác nhận kịp thời.

                Vui lòng liên hệ với đội ngũ quản lý nếu bạn cần hỗ trợ thêm.

                Trân trọng,
                Đội ngũ Quản lý Tour
                """,
                from_email='noreply@yourtourwebsite.com',
                recipient_list=[booking.email],
                fail_silently=True
            )

            # Tăng số lượng chỗ trống trong tour
            if booking.tour:
                booking.tour.remaining_capacity += booking.number_of_people
                booking.tour.save()

            # Xóa booking sau khi xử lý
            booking.delete()