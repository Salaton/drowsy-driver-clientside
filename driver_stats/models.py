from django.db import models
from users.models import DrowsyDriverUser

# Create your models here.
class Stats(models.Model):
    # user = models.OneToOneField(DrowsyDriverUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    username = models.CharField(max_length=10)
    last_name = models.CharField(max_length=15)
    eye_aspect_ratio = models.CharField(max_length=20)
    time_alarm_raised = models.DateTimeField(auto_now_add=True)
    car_registration_number = models.CharField(max_length=10)


# class Stats(models.Model):
#     user = models.OneToOneField(DrowsyDriverUser, on_delete=models.CASCADE)
#     eye_aspect_ratio = models.CharField(max_length=20)
#     time_alarm_raised = models.DateTimeField(auto_now_add=True)
