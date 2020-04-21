from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from uploads.core.models import Document


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)
    car_registration_number = forms.CharField(max_length=10)
    photo = forms.ImageField()

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'car_registration_number', 'photo', 'password1', 'password2'
        )
