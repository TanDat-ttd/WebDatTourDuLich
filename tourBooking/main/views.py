from django.shortcuts import render


# Trang chủ
def index(request):
    return render(request, 'index.html')  # Trả về index.html


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
    return render(request, 'destinations/destination_BinhDinh.html')  # Trả về destination_BinhDinh.html


def destination_CaoBang(request):
    return render(request, 'destinations/destination_CaoBang.html')  # Trả về destination_CaoBang.html


def destination_DaLat(request):
    return render(request, 'destinations/destination_DaLat.html')  # Trả về destination_DaLat.html


def destination_HaNoi(request):
    return render(request, 'destinations/destination_HaNoi.html')  # Trả về destination_HaNoi.html


def destination_HoiAn(request):
    return render(request, 'destinations/destination_HoiAn.html')  # Trả về destination_HoiAn.html


def destination_NinhBinh(request):
    return render(request, 'destinations/destination_NinhBinh.html')  # Trả về destination_NinhBinh.html


def destination_VinhHaLong(request):
    return render(request, 'destinations/destination_VinhHaLong.html')  # Trả về destination_VinhHaLong.html


def destination_VungTau(request):
    return render(request, 'destinations/destination_VungTau.html')  # Trả về destination_VungTau.html


# Trang FAQ (câu hỏi thường gặp)
def faq(request):
    return render(request, 'faq.html')  # Trả về faq.html


# Trang Gallery (bộ sưu tập)
def gallery(request):
    return render(request, 'gallery.html')  # Trả về gallery.html


# Trang tour du lịch
def tour(request):
    return render(request, 'tour.html')  # Trả về tour.htmlgit remote add origin https://github.com/TanDat-ttd/WebDatTourDuLich.git