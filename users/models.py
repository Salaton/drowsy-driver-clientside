from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class DrowsyDriverUser(AbstractUser):
    """Custom drowsy driver that inherits form User."""

    car_registration_number = models.CharField(max_length=10)
    next_of_kin_name = models.CharField(max_length=31, default="")
    next_of_kin_number = models.CharField(max_length=30, blank=False, default="")
