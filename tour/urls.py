
from django.urls import path
from . import views  # Import views của app

urlpatterns = [
    path('tour/', views.tour, name='tour'),  # Trang tour
]
