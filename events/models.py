from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    total_seats = models.PositiveIntegerField()
    available_seats=models.PositiveIntegerField()
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Booking(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booked_at=models.DateTimeField(auto_now_add=True)