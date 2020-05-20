from django.db import models
from users.models import DrowsyDriverUser

# Create your models here.
class Stats(models.Model):
<<<<<<< HEAD
    # user = models.OneToOneField(DrowsyDriverUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15, null=True)
    username = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=15, null=True)
    eye_aspect_ratio = models.CharField(max_length=20, null=True)
    time_alarm_raised = models.DateTimeField(auto_now_add=True, null=True)
    car_registration_number = models.CharField(max_length=10, null=True)
=======
    user = models.ForeignKey(DrowsyDriverUser, on_delete=models.CASCADE, null=True)
    eye_aspect_ratio = models.CharField(max_length=20, null=True)
    time_alarm_raised = models.DateTimeField(auto_now_add=True, null=True)
>>>>>>> testing


# class Stats(models.Model):
#     user = models.OneToOneField(DrowsyDriverUser, on_delete=models.CASCADE)
#     eye_aspect_ratio = models.CharField(max_length=20)
#     time_alarm_raised = models.DateTimeField(auto_now_add=True)
