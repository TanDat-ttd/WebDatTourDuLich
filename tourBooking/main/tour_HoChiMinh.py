from main.models import Tour
from main.models import Schedule
tour = Tour.objects.create(
    code="SGHL2024",
    name="TP. Hồ Chí Minh - Sài Gòn hoa lệ (4 ngày 3 đêm)",
    description="Thành phố Hồ Chí Minh năng động, hiện đại và đa dạng văn hóa.",
    start_date="2024-01-01",
    end_date="2024-01-04",
    price=5000000,
    capacity=20,
    remaining_capacity=20,
)
"""

	   Tour TP. Hồ Chí Minh - Sài Gòn hoa lệ (4 ngày 3 đêm)

Hành trình: Thành phố Hồ Chí Minh

Title: Sài Gòn hoa lệ - Năng động và hiện đại

Lịch trình chi tiết:

Ngày 1: Đến TP. Hồ Chí Minh - Khám phá trung tâm

Đến sân bay Tân Sơn Nhất, xe đón và đưa về khách sạn nhận phòng.

Chiều: Tham quan Dinh Độc Lập, Nhà thờ Đức Bà, Bưu điện Thành phố, Nhà hát Thành phố.

Tối: Dạo phố đi bộ Nguyễn Huệ, thưởng thức ẩm thực Sài Gòn.

Ngày 2: TP. Hồ Chí Minh - Địa đạo Củ Chi - Bảo tàng Chứng tích Chiến tranh

Sáng: Khám phá Địa đạo Củ Chi, tìm hiểu về hệ thống địa đạo lịch sử và cuộc sống của người dân trong thời kỳ chiến tranh.

Chiều: Tham quan Bảo tàng Chứng tích Chiến tranh, tìm hiểu về lịch sử chiến tranh Việt Nam.

Tối: Thưởng thức chương trình nghệ thuật truyền thống hoặc xem phim tại rạp (tùy chọn).

Ngày 3: TP. Hồ Chí Minh - Chợ Bến Thành - Khu Chợ Lớn

Sáng: Mua sắm tại chợ Bến Thành, khám phá đa dạng các mặt hàng từ quần áo, đồ lưu niệm đến đặc sản địa phương.

Chiều: Khám phá Khu Chợ Lớn, trung tâm thương mại sầm uất của cộng đồng người Hoa. Tham quan các đền chùa, thưởng thức ẩm thực Trung Hoa.

Tối: Trải nghiệm ẩm thực đường phố Sài Gòn, hoặc tham gia lớp học nấu ăn (tùy chọn).

Ngày 4: TP. Hồ Chí Minh - Bảo tàng Mỹ thuật - Khởi hành

Sáng: Tham quan Bảo tàng Mỹ thuật TP. Hồ Chí Minh, chiêm ngưỡng các tác phẩm nghệ thuật đặc sắc. Hoặc tham gia tour khám phá ẩm thực Sài Gòn với các món ăn đặc trưng (tùy chọn).

Chiều: Tự do mua sắm quà lưu niệm. Xe đưa ra sân bay Tân Sơn Nhất, kết thúc chương trình.

Điểm nổi bật:

Khám phá thành phố Hồ Chí Minh sôi động và hiện đại.

Tìm hiểu về lịch sử và văn hóa Việt Nam qua các di tích và bảo tàng.

Trải nghiệm ẩm thực đa dạng và phong phú của Sài Gòn.

Mua sắm tại các trung tâm thương mại và chợ truyền thống.

Ghi chú:

3 địa điểm chính: Trung tâm thành phố, Địa đạo Củ Chi, Khu Chợ Lớn.

Lịch trình có thể thay đổi tùy theo yêu cầu của du khách.

Giá tour chưa bao gồm vé máy bay, chi phí cá nhân và các chi phí phát sinh khác. -->


"""
#Ngày 1: Đến TP. Hồ Chí Minh - Khám phá trung tâm


Schedule.objects.create(
    tour=tour,
    day=1,
    period="Sáng",
    activity="Đến sân bay Tân Sơn Nhất, xe đón và đưa về khách sạn nhận phòng.",
)

Schedule.objects.create(
    tour=tour,
    day=1,
    period="Chiều",
    activity="Tham quan Dinh Độc Lập, Nhà thờ Đức Bà, Bưu điện Thành phố và Nhà hát Thành phố.",
)

Schedule.objects.create(
    tour=tour,
    day=1,
    period="Tối",
    activity="Dạo phố đi bộ Nguyễn Huệ, thưởng thức ẩm thực Sài Gòn.",
)

#Ngày 2: TP. Hồ Chí Minh - Địa đạo Củ Chi - Bảo tàng Chứng tích Chiến tranh
Schedule.objects.create(
    tour=tour,
    day=2,
    period="Sáng",
    activity="Khám phá Địa đạo Củ Chi, tìm hiểu về hệ thống địa đạo và cuộc sống trong chiến tranh.",
)

Schedule.objects.create(
    tour=tour,
    day=2,
    period="Chiều",
    activity="Tham quan Bảo tàng Chứng tích Chiến tranh để tìm hiểu lịch sử chiến tranh Việt Nam.",
)

Schedule.objects.create(
    tour=tour,
    day=2,
    period="Tối",
    activity="Thưởng thức chương trình nghệ thuật truyền thống hoặc xem phim tại rạp (tùy chọn).",
)

#Ngày 3: TP. Hồ Chí Minh - Chợ Bến Thành - Khu Chợ Lớn
Schedule.objects.create(
    tour=tour,
    day=3,
    period="Sáng",
    activity="Mua sắm tại chợ Bến Thành và khám phá đa dạng mặt hàng đặc sản địa phương.",
)

Schedule.objects.create(
    tour=tour,
    day=3,
    period="Chiều",
    activity="Khám phá khu Chợ Lớn, trung tâm sầm uất của cộng đồng người Hoa, tham quan các đền chùa.",
)

Schedule.objects.create(
    tour=tour,
    day=3,
    period="Tối",
    activity="Trải nghiệm ẩm thực đường phố Sài Gòn hoặc tham gia lớp học nấu ăn (tùy chọn).",
)
#Ngày 4: TP. Hồ Chí Minh - Bảo tàng Mỹ thuật - Khởi hành

Schedule.objects.create(
    tour=tour,
    day=4,
    period="Sáng",
    activity="Tham quan Bảo tàng Mỹ thuật TP. Hồ Chí Minh hoặc tham gia tour ẩm thực đặc trưng.",
)

Schedule.objects.create(
    tour=tour,
    day=4,
    period="Chiều",
    activity="Tự do mua sắm. Xe đưa ra sân bay Tân Sơn Nhất, kết thúc chương trình.",
)




