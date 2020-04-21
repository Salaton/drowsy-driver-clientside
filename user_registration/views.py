# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic
# # Create your views here.


# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     # redirect user to login page upon successful registration
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import SignUpForm
# from .models import PassportPhoto


def SignUp(request):
    if request.method == 'POST':
        # throw that data into the form...
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            # save to create the user..
            user = form.save()
            # Load profile instance
            user.refresh_from_db()
            user.profile.car_registration_number = form.cleaned_data.get(
                'car_registration_number')
            user.profile.photo = form.cleaned_data.get('photo')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # new_photo = PassportPhoto(photo=request.FILES['photo'])
            # new_photo.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
