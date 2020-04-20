from django.db import models
from django.forms import ModelForm

# Create your models here.


class PassportPhoto(models.Model):
    photo = models.ImageField(upload_to='pictures')
