from django.shortcuts import render, redirect
from .forms import DrowsyDriverUserChangeForm, DrowsyDriverUserCreationForm
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


def Login(request):
    return render(request, 'login.html', {})


# from .models import PassportPhoto


def SignUp(request):
    if request.method == 'POST':
        # throw that data into the form...
        form = DrowsyDriverUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # save to create the user..
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # new_photo = PassportPhoto(photo=request.FILES['photo'])
            # new_photo.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = DrowsyDriverUserCreationForm()
    return render(request, 'signup.html', {'form': form})
