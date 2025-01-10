from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Q
from .models import Tour, Review
from .forms import ReviewForm

def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'blog.html', {'tours': tours})

def tour_detail(request, tour_id):
    """ Hiển thị chi tiết tour và xử lý đánh giá """
    tour = get_object_or_404(Tour, id=tour_id)
    reviews = tour.reviews.all()
    schedules = tour.schedules.all()

    # Tính toán điểm đánh giá trung bình của tour
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] if reviews.exists() else 0

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.tour = tour
                review.save()
                return redirect('tour_detail', tour_id=tour.id)
        else:
            return redirect('login')
    else:
        form = ReviewForm()

    return render(request, 'blog_detail.html', {
        'tour': tour, 'reviews': reviews, 'form': form, 'schedules': schedules, 'average_rating': average_rating
    })
def tour_list(request):
    tours = Tour.objects.all()

    # Calculate average rating for each tour
    for tour in tours:
        tour.average_rating = tour.reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    return render(request, 'blog.html', {'tours': tours})

def tour_list(request):
    query = request.GET.get('q', '')  # Lấy từ khóa tìm kiếm từ URL
    tours = Tour.objects.all()

    if query:
        tours = tours.filter(
            Q(name__icontains=query) | 
            Q(code__icontains=query) | 
            Q(description__icontains=query)
        )

    # Tính toán điểm đánh giá trung bình cho từng tour
    for tour in tours:
        tour.average_rating = tour.reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    return render(request, 'blog.html', {'tours': tours, 'query': query})