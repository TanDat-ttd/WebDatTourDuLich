from django.shortcuts import render
from main.models import Tour  # Giả sử bạn có model Tour

def tour(request):
    query = request.GET.get('q', '')  # Lấy từ khóa tìm kiếm từ GET request
    start_date = request.GET.get('start_date', '')  # Lấy ngày bắt đầu
    end_date = request.GET.get('end_date', '')  # Lấy ngày kết thúc
    min_price = request.GET.get('min_price', '')  # Lấy giá tối thiểu
    max_price = request.GET.get('max_price', '')  # Lấy giá tối đa

    # Xây dựng queryset tìm kiếm
    tours = Tour.objects.all()

    if query:
        tours = tours.filter(name__icontains=query)  # Tìm kiếm theo tên

    if start_date:
        tours = tours.filter(start_date__gte=start_date)  # Tìm kiếm theo ngày bắt đầu

    if end_date:
        tours = tours.filter(end_date__lte=end_date)  # Tìm kiếm theo ngày kết thúc

    if min_price:
        tours = tours.filter(price__gte=min_price)  # Tìm kiếm theo giá tối thiểu

    if max_price:
        tours = tours.filter(price__lte=max_price)  # Tìm kiếm theo giá tối đa

    return render(request, 'tour.html', {
        'tours': tours,
        'query': query,
        'start_date': start_date,
        'end_date': end_date,
        'min_price': min_price,
        'max_price': max_price
    })
