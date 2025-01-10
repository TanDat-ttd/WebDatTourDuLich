from main.models import Tour, Schedule
from datetime import datetime

# Thêm Tour
tour = Tour.objects.create(
    name="Hà Nội - Lào Cai - Quảng Ninh - Ninh Bình",  # Tên tour
    description="""
Hà Nội - Lào Cai - Quảng Ninh - Ninh Bình: Sapa - Bản Cát Cát - Fansipan Hạ Long - Động Thiên Cung - Yên Tử - KDL Tràng An - Bái Đính

--Ngày 1: TPHCM - SB Nội Bài (Hà Nội) - Sapa--

 02 bữa ăn (trưa, chiều)

Quý khách tập trung tại sân bay Tân Sơn Nhất, hướng dẫn viên hỗ trợ làm thủ tục đáp chuyến bay đi Hà Nội... (Nội dung đầy đủ bạn thêm vào đây)

...
(Nội dung tiếp theo của mô tả)
...
""",
    start_date=datetime.strptime("2023-12-01", "%Y-%m-%d"),  # Ngày bắt đầu của tour (thay đổi nếu cần)
    end_date=datetime.strptime("2023-12-06", "%Y-%m-%d"),  # Ngày kết thúc tour
    price=11790000.00,  # Giá tour
    capacity=45,  # Sức chứa tối đa khách
    remaining_capacity=45,  # Số chỗ còn lại ban đầu
)

# Thêm Lịch trình (Schedule) cho tour
schedules = [
    # Ngày 1
    {"day": 1, "period": "Sáng",
     "activity": "Quý khách tập trung tại sân bay Tân Sơn Nhất, làm thủ tục bay đi Hà Nội."},
    {"day": 1, "period": "Trưa",
     "activity": "Di chuyển theo cao tốc Hà Nội - Lào Cai, dùng cơm trưa tại nhà hàng địa phương."},
    {"day": 1, "period": "Chiều",
     "activity": "Tham quan bản Cát Cát - ngôi làng cổ đẹp nhất Sapa, xem biểu diễn văn nghệ dân tộc."},
    {"day": 1, "period": "Tối",
     "activity": "Tự do dạo phố, ngắm nhà thờ đá Sapa và thưởng thức đặc sản vùng cao tại chợ đêm Sapa."},

    # Ngày 2
    {"day": 2, "period": "Sáng", "activity": "Trải nghiệm tàu hỏa leo núi Mường Hoa và khám phá Fansipan."},
    {"day": 2, "period": "Chiều", "activity": "Chinh phục Đèo Ô Quy Hồ, tham quan Cổng Trời Ô Quy Hồ (săn mây)."},
    {"day": 2, "period": "Tối", "activity": "Nghỉ ngơi tự do tại Sapa sau bữa cơm tối."},

    # Ngày 3
    {"day": 3, "period": "Sáng", "activity": "Khởi hành về Hà Nội, trên đường dừng chân mua đặc sản."},
    {"day": 3, "period": "Chiều", "activity": "Tự do tham quan Hồ Hoàn Kiếm, Tháp Rùa tại Hà Nội."},

    # Ngày 4
    {"day": 4, "period": "Sáng",
     "activity": "Tham quan Lăng Bác, Nhà Sàn Bác Hồ, Chùa Một Cột, tìm hiểu văn hóa lịch sử Việt Nam."},
    {"day": 4, "period": "Chiều", "activity": "Tham quan thắng cảnh Đông Yên Tử bằng cáp treo và chùa Hoa Yên."},
    {"day": 4, "period": "Tối", "activity": "Buổi tối tự do khám phá phố cổ Bãi Cháy tại Hạ Long."},

    # Ngày 5
    {"day": 5, "period": "Sáng",
     "activity": "Du ngoạn Vịnh Hạ Long, khám phá Động Thiên Cung và ngắm Hòn Gà Chọi, Hòn Lư Hương."},
    {"day": 5, "period": "Chiều", "activity": "Di chuyển đến Ninh Bình, nhận phòng khách sạn tại Ninh Bình."},
    {"day": 5, "period": "Tối", "activity": "Tự do khám phá Phố cổ Hoa Lư và các hoạt động dân gian, văn hóa."},

    # Ngày 6
    {"day": 6, "period": "Sáng", "activity": "Tham quan KDL Tràng An, khám phá hệ hang động ngập nước kỳ thú."},
    {"day": 6, "period": "Trưa",
     "activity": "Viếng chùa Bái Đính, nơi có nhiều kỷ lục Việt Nam như pho tượng Phật Di Lặc khổng lồ."},
    {"day": 6, "period": "Chiều", "activity": "Trở về sân bay Nội Bài, kết thúc hành trình du lịch tại Hà Nội."},
]

# Chạy vòng lặp để thêm các lịch trình vào hệ thống
for schedule in schedules:
    Schedule.objects.create(
        tour=tour,
        day=schedule['day'],
        period=schedule['period'],
        activity=schedule['activity']
    )

print("Đã thêm thành công dữ liệu cho tour Hà Nội - Lào Cai - Quảng Ninh - Ninh Bình!")