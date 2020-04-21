from django.contrib.auth.models import AbstractUser
from django.db import models


class DrowsyDriverUser(AbstractUser):
    """Custom drowsy driver that inherits form User."""

    car_registration_number = models.CharField(max_length=10)
    photo = models.ImageField()
