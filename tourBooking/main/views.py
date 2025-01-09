from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Tour

# Trang chủ
def index(request):
    # Lấy tất cả các tour từ cơ sở dữ liệu
    tours = Tour.objects.all()
    
    # Trả về trang index.html và truyền danh sách tours vào context
    return render(request, 'index.html', {'tours': tours})


# Trang giới thiệu
def about(request):
    return render(request, 'about.html')  # Trả về about.html


# Trang liên hệ
def contact(request):
    return render(request, 'contact.html')  # Trả về contact.html


# Trang blog (danh sách bài viết)
def blog(request):
    return render(request, 'blog.html')  # Trả về blog.html


# Trang chi tiết bài viết
def blog_detail(request):
    return render(request, 'blog_detail.html')  # Trả về blog_detail.html


# Các trang điểm đến chính
def destination(request):
    return render(request, 'destination.html')  # Trả về destination.html


def destination2(request):
    return render(request, 'destination2.html')  # Trả về destination2.html


def destination3(request):
    return render(request, 'destination3.html')  # Trả về destination3.html


# Các trang điểm đến cụ thể
def destination_BinhDinh(request):
    return render(request, 'destination_BinhDinh.html')  # Trả về destination_BinhDinh.html


def destination_CaoBang(request):
    return render(request, 'destination_CaoBang.html')  # Trả về destination_CaoBang.html


def destination_DaLat(request):
    return render(request, 'destination_DaLat.html')  # Trả về destination_DaLat.html


def destination_HaNoi(request):
    return render(request, 'destination_HaNoi.html')  # Trả về destination_HaNoi.html


def destination_HoiAn(request):
    return render(request, 'destination_HoiAn.html')  # Trả về destination_HoiAn.html


def destination_NinhBinh(request):
    return render(request, 'destination_NinhBinh.html')  # Trả về destination_NinhBinh.html


def destination_VinhHaLong(request):
    return render(request, 'destination_VinhHaLong.html')  # Trả về destination_VinhHaLong.html


def destination_VungTau(request):
    return render(request, 'destination_VungTau.html')  # Trả về destination_VungTau.html


# Trang FAQ (câu hỏi thường gặp)
def faq(request):
    return render(request, 'faq.html')  # Trả về faq.html


# Trang Gallery (bộ sưu tập)
def gallery(request):
    return render(request, 'gallery.html')  # Trả về gallery.html


# Trang tour du lịch
def tour(request):
    return render(request, 'tour.html')  # Trả về tour.html


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')





# View hiển thị chi tiết tour và lịch trình
# def destination_payment(request, pk):
#     """
#     View hiển thị chi tiết về một tour cụ thể.
#     """
#     # Lấy thông tin tour theo id (primary key - pk)
#     tour = get_object_or_404(Tour, pk=pk)
#
#     # Lấy toàn bộ lịch trình của tour, sắp xếp theo ngày và buổi
#     schedules = tour.schedules.order_by("day", "period")
#
#     # Render tour_detail.html với dữ liệu
#     return render(request, 'tour_detail.html', {'tour': tour, 'schedules': schedules})
