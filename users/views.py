from django.shortcuts import render, redirect
from .forms import DrowsyDriverUserChangeForm, DrowsyDriverUserCreationForm
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.management import call_command
from .models import DrowsyDriverUser


# Create your views here.


def Login(request):
    return render(request, "login.html", {})


# from .models import PassportPhoto


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


def status_list():
    return DrowsyDriverUser.objects.all()


# Running an external python script..
@login_required()
def RunOpenCV(request):
    call_command("video")
    return render(request, "home.html", {})


# User Profile
# @login_required()
def profile(request):
    # Create a dictionary for the details..
    args = {"User": request.user}
    return render(request, "profile.html", args)
