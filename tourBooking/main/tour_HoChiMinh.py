from main.models import Tour

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
from main.models import Schedule
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




