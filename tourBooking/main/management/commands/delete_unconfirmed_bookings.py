from django.core.management.base import BaseCommand
from django.utils.timezone import localtime, now
from django.core.mail import send_mail
from payment.models import Booking
from main.models import Tour


class Command(BaseCommand):
    help = 'Xóa các booking chưa được xác nhận sau một thời gian nhất định.'

    def handle(self, *args, **kwargs):
        # Lấy thời gian hiện tại
        current_time = localtime(now())

        # Lọc booking có trạng thái Paid nhưng đã quá hạn xác nhận
        expired_bookings = Booking.objects.filter(
            status='paid',  # Chỉ lấy booking với trạng thái 'paid'
            confirmation_deadline__lt=current_time,  # Đã quá hạn xác nhận
        )

        expired_count = expired_bookings.count()
        if expired_count > 0:
            for booking in expired_bookings:
                # Gửi thông báo qua email trước khi xóa
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

                # Tăng số lượng chỗ trống cho tour (vì booking này bị hủy)
                if booking.tour:
                    booking.tour.remaining_capacity += booking.number_of_people
                    booking.tour.save()

                # Xóa booking
                booking.delete()

            # Log thông tin
            self.stdout.write(self.style.SUCCESS(
                f"Đã xóa {expired_count} booking chưa được xác nhận và đã quá hạn."
            ))
        else:
            # Nếu không có booking nào cần xử lý
            self.stdout.write("Không có booking nào quá hạn cần xóa.")