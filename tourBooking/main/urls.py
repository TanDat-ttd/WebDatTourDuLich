
from django.urls import path, include
from . import views  # Import views của app
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),  # URL mặc định cho admin
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('destination/', views.destination, name='destination'),
    path('destination2/', views.destination2, name='destination2'),
    path('destination3/', views.destination3, name='destination3'),
    path('destination_BinhDinh/', views.destination_BinhDinh, name='destination_BinhDinh'),
    path('destination_CaoBang/', views.destination_CaoBang, name='destination_CaoBang'),
    path('destination_DaLat/', views.destination_DaLat, name='destination_DaLat'),
    path('destination_HaNoi/', views.destination_HaNoi, name='destination_HaNoi'),
    path('destination_HoiAn/', views.destination_HoiAn, name='destination_HoiAn'),
    path('destination_NinhBinh/', views.destination_NinhBinh, name='destination_NinhBinh'),
    path('destination_VinhHaLong/', views.destination_VinhHaLong, name='destination_VinhHaLong'),
    path('destination_VungTau/', views.destination_VungTau, name='destination_VungTau'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('tour/', views.tour, name='tour'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    path('payment/', include('payment.urls')),  # Đưa logic thanh toán sang app payment

    path('tour/<int:pk>/', views.destionationPayment, name='destionationPayment'),  # Chi tiết tour

]