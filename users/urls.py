from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.Login, name='login'),
    path("signup/", views.SignUp, name="signup"),
    path("home/", views.RunOpenCV, name="RunOpenCV"),
    path("profile/", views.edit_profile, name="edit_profile"),
    path("profile/", views.profile, name="profile"),
]
