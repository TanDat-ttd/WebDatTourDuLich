# views.py
from django.shortcuts import render
from main.models import Tour
from django.db.models import Q  # Để thực hiện tìm kiếm linh hoạt

def tour(request):
    search_query = request.GET.get('search', '')  # Lấy từ khóa tìm kiếm từ query params
    tours = Tour.objects.all()  # Mặc định là lấy tất cả các tour
    
    if search_query:
        # Lọc tour theo tên hoặc mô tả chứa từ khóa tìm kiếm
        tours = tours.filter(
            Q(name__icontains=search_query) |  # Tìm kiếm theo tên tour
            Q(description__icontains=search_query)  # Tìm kiếm theo mô tả tour
        )
    
    context = {
        'tours': tours,
        'search_query': search_query  # Để hiển thị lại từ khóa tìm kiếm trong form
    }
    
    return render(request, 'tour.html', context)

def tour_detail(request, id):
    tour = Tour.objects.get(id=id)
    context = {
        'tour': tour
    }
    return render(request, 'tour.html', context)
