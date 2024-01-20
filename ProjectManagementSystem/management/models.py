from django.db import models
from django.contrib.auth.models import User
# Create your models here.
Status_Catagory = (
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
    ('to_be_completed','to_be_completed')
)


class Developer(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.first_name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150)
    assigned_to_developer = models.ManyToManyField(Developer)
    start_date = models.DateField(blank=True , null=True)
    end_date = models.DateField(blank=True , null=True)
    status = models.CharField(max_length=30, choices=Status_Catagory, blank=True)
    recorded_at = models.DateTimeField(auto_now_add=True, blank=True)


