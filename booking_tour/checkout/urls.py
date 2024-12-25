from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the checkout index.")

def payment(request):
    return HttpResponse(
        "Hello, world. You're at the checkout payment."
    )


urlpatterns = [
  #  path('admin/', admin.site.urls),  # Thêm quản lý admin nếu cần
 #path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('blog/', views.blog, name='blog'),
    # path('blog_detail/', views.blog_detail, name='blog_detail'),
    # path('contact/', views.contact, name='contact'),
    # path('destination/', views.destination, name='destination'),
    # path('destination2/', views.destination2, name='destination2'),
    # path('destination3/', views.destination3, name='destination3'),
    # path('destination_BinhDinh/', views.destination_BinhDinh, name='destination_BinhDinh'),
    # path('destination_CaoBang/', views.destination_CaoBang, name='destination_CaoBang'),
    # path('destination_DaLat/', views.destination_DaLat, name='destination_DaLat'),
    # path('destination_HaNoi/', views.destination_HaNoi, name='destination_HaNoi'),
    # path('destination_HoiAn/', views.destination_HoiAn, name='destination_HoiAn'),
    # path('destination_NinhBinh/', views.destination_NinhBinh, name='destination_NinhBinh'),
    # path('destination_VinhHaLong/', views.destination_VinhHaLong, name='destination_VinhHaLong'),
    # path('destination_VungTau/', views.destination_VungTau, name='destination_VungTau'),
    # path('detail/', views.detail, name='detail'),
    # path('faq/', views.faq, name='faq'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    # path('tour/', views.tour, name='tour'),


    path('payment/', views.payment_view, name='payment'),
    path('apply-discount/', views.apply_discount, name='apply_discount'),  # Định nghĩa URL endpoint
    path('success/<int:booking_id>/', views.success_view, name='success'),
    path('failed/', views.failed_view, name='failed'),
]