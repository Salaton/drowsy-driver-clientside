from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import DrowsyDriverUser


class DrowsyDriverUserCreationForm(UserCreationForm):
    class Meta:
        model = DrowsyDriverUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "car_registration_number",
            "next_of_kin_name",
            "next_of_kin_number",
        ]


class DrowsyDriverUserChangeForm(UserChangeForm):
    class Meta:
        model = DrowsyDriverUser
        # fields = UserChangeForm.Meta.fields
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "car_registration_number",
            "next_of_kin_name",
            "next_of_kin_number",
        ]
