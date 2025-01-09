from django.db import models
from django.contrib.auth.models import User
from main.models import Tour

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, f"{i} ⭐") for i in range(1, 6)])  # Đánh giá từ 1-5 sao
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tour.name} - {self.rating}⭐"
