import json

from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.management import call_command
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import DrowsyDriverUserChangeForm, DrowsyDriverUserCreationForm
from .models import DrowsyDriverUser

# Create your views here.


def Login(request):
    return render(request, "login.html", {})


def SignUp(request):
    if request.method == "POST":
        # throw that data into the form...
        form = DrowsyDriverUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # save to create the user..
            user = form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            # new_photo = PassportPhoto(photo=request.FILES['photo'])
            # new_photo.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
    else:
        form = DrowsyDriverUserCreationForm()
    return render(request, "signup.html", {"form": form})


# def status_list(request):
#     return DrowsyDriverUser.objects.get(request.user.username)


# Running an external python script --> the custom command (python manage.py video)..
@login_required()
def RunOpenCV(request):
    user_details = {
        "username": request.user.username,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "car_registration_number": request.user.car_registration_number,
        "next_of_kin_name": request.user.next_of_kin_name,
        "next_of_kin_number": request.user.next_of_kin_number,
    }
    call_command("video", json.dumps(user_details))
    return render(request, "home.html", {})


# User Profile
@login_required()
def profile(request):
    # Create a dictionary for the details..
    args = {"User": request.user}
    return render(request, "profile.html", {"args": args})


# Gets current user details --> User can change them anytime...
@login_required()
def edit_profile(request):
    if request.method == "POST":
        form = DrowsyDriverUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = DrowsyDriverUserChangeForm(instance=request.user)
        # args = {"form": form}
    return render(request, "profile.html", {"form": form})


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the error below.")
            # return redirect("registration/change_password")
    else:
        form = PasswordChangeForm(user=request.user)
        # args = {"form": form}
    return render(request, "registration/change_password.html", {"form": form})
