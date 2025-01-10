from main.models import Tour, Schedule
from datetime import datetime

# Thêm Tour
tour = Tour.objects.create(
    name="Hà Nội - Quảng Ninh - Ninh Bình",  # Tên tour
    description="""
--Ngày 1: SB Nội Bài - Hà Nội--

00 bữa ăn (tự túc ăn ngày đầu tiên)

Quý khách tập trung tại sân bay Tân Sơn Nhất (Ga nội địa), hướng dẫn viên hỗ trợ khách làm thủ tục đáp chuyến bay đi Hà Nội. Đến sân bay Nội Bài, xe và HDV Vietravel đón Quý khách đi Hà Nội nhận phòng khách sạn nghỉ ngơi hoặc tự do đi tham quan phố cổ Hà Nội.

Nghỉ đêm tại Hà Nội


--Ngày 2: Hà Nội - Yên Tử - Hạ Long--

03 bữa ăn (sáng, trưa, chiều)

Quý khách dùng bữa sáng và trả phòng khách sạn. Xe khởi hành đưa Quý khách đi tham quan:

Một vòng Hồ Hoàn Kiếm ngắm bên ngoài Tháp Rùa, Đền Ngọc Sơn, Cầu Thê Húc.
Tiếp tục hành trình, xe khởi hành đưa Quý khách đến thành phố biển Hạ Long theo quốc lộ 18, trên đường dừng tham quan Yên Tử: 

Chụp hình lưu niệm Làng Nương và dùng bữa trưa tại Cơm Quê.
Trải nghiệm cáp treo ngắm thắng cảnh thiên nhiên Yên Tử (chi phí cáp treo tự túc), nơi còn lưu giữ nhiều di tích lịch sử mệnh danh “Đất tổ Phật giáo Việt Nam”, chiêm bái chùa Một Mái, chùa Hoa Yên - nơi tu hành của phật hoàng Trần Nhân Tông.
Quý khách nhận phòng khách sạn và dùng cơm chiều tại nhà hàng địa phương. Buổi tối tự do khám phá “phố cổ” Bãi Cháy hoặc café/pub.

Nghỉ đêm tại Hạ Long.


--Ngày 3: Vịnh Hạ Long - Ninh Bình--

03 bữa ăn (sáng, trưa, chiều)

Quý khách tham quan: Chụp hình bên ngoài Bảo tàng Quảng Ninh, du ngoạn Vịnh Hạ Long, tham quan Động Thiên Cung. Quý khách tiếp tục khởi hành đi Ninh Bình - “Nơi mơ đến, chốn mong về.”

Đến nơi, quý khách nhận phòng khách sạn, khám phá Phố cổ Hoa Lư về đêm.

Nghỉ đêm tại Ninh Bình.


--Ngày 4: Ninh Bình - SB Nội Bài--

02 bữa ăn (sáng, trưa)

Quý khách khám phá KDL Tràng An và viếng Chùa Bái Đính - quần thể chùa nổi tiếng. Sau đó trả phòng và xe đưa đoàn ra sân bay Nội Bài, làm thủ tục kết thúc chuyến đi.


Lưu ý:

Hành trình có thể thay đổi thứ tự điểm đến tùy vào điều kiện thực tế.
""",
    start_date=datetime.strptime("2023-12-01", "%Y-%m-%d"),  # Ngày bắt đầu
    end_date=datetime.strptime("2023-12-04", "%Y-%m-%d"),  # Ngày kết thúc
    price=8390000.00,  # Giá tour
    capacity=30,  # Sức chứa
    remaining_capacity=30,  # Chỗ trống còn lại
)

# Thêm các lịch trình (Schedule) liên quan đến Tour
schedules = [
    # Ngày 1
    {"day": 1, "period": "Sáng",
     "activity": "Quý khách tập trung tại sân bay Tân Sơn Nhất, làm thủ tục bay đi Hà Nội."},
    {"day": 1, "period": "Chiều", "activity": "Nhận phòng khách sạn, nghỉ ngơi hoặc tự do tham quan phố cổ Hà Nội."},

    # Ngày 2
    {"day": 2, "period": "Sáng", "activity": "Tham quan Hồ Hoàn Kiếm, Đền Ngọc Sơn, Cầu Thê Húc..."},
    {"day": 2, "period": "Chiều", "activity": "Tham quan Yên Tử, cáp treo, chiêm bái chùa Đồng."},
    {"day": 2, "period": "Tối", "activity": "Tự do khám phá Hạ Long về đêm, phố cổ Bãi Cháy, café."},

    # Ngày 3
    {"day": 3, "period": "Sáng",
     "activity": "Chụp hình tại Bảo tàng Quảng Ninh, du ngoạn Vịnh Hạ Long, Động Thiên Cung."},
    {"day": 3, "period": "Chiều",
     "activity": "Di chuyển về Ninh Bình, nhận phòng khách sạn, khám phá Phố cổ Hoa Lư về đêm."},

    # Ngày 4
    {"day": 4, "period": "Sáng", "activity": "Khám phá KDL Tràng An và viếng Chùa Bái Đính."},
    {"day": 4, "period": "Chiều", "activity": "Kết thúc hành trình tại sân bay Nội Bài, trở lại Tp.HCM."},
]

# Chạy vòng lặp để thêm các lịch trình vào cơ sở dữ liệu
for schedule in schedules:
    Schedule.objects.create(
        tour=tour,
        day=schedule['day'],
        period=schedule['period'],
        activity=schedule['activity']
    )

print("Dữ liệu Tour và Lịch trình đã được thêm thành công!")