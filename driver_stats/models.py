from django.db import models

# Create your models here.
class Stats(models.Model):
    first_name = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    eye_aspect_ratio = models.CharField(max_length=20)
    time_alarm_raised = models.DateTimeField(auto_now_add=True)
    car_registration_number = models.CharField(max_length=10, default="")
