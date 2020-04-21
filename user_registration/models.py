from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.
# Model that stores extra details of the user


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car_registration_number = models.CharField(max_length=10)
    photo = models.ImageField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
