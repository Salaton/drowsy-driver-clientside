from django.db import models
from users.models import DrowsyDriverUser

# Create your models here.
class Stats(models.Model):
    user = models.ForeignKey(DrowsyDriverUser, on_delete=models.CASCADE)
    eye_aspect_ratio = models.CharField(max_length=20, null=True)
    time_alarm_raised = models.DateTimeField(auto_now_add=True, null=True)


# class Stats(models.Model):
#     user = models.OneToOneField(DrowsyDriverUser, on_delete=models.CASCADE)
#     eye_aspect_ratio = models.CharField(max_length=20)
#     time_alarm_raised = models.DateTimeField(auto_now_add=True)
