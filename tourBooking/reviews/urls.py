from django.urls import path
from .views import tour_list, tour_detail

urlpatterns = [
    path('tours/', tour_list, name='tour_list'),
    path('tours/<int:tour_id>/', tour_detail, name='tour_detail'),
]
