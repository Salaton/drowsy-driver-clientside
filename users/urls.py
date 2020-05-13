from django.urls import path, re_path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from . import views

urlpatterns = [
    # path('login/', views.Login, name='login'),
    path("signup/", views.SignUp, name="signup"),
    path("home/", views.RunOpenCV, name="RunOpenCV"),
    path("profile/", views.edit_profile, name="edit_profile"),
    path("profile/", views.profile, name="profile"),
    path("change-password/", views.change_password, name="change_password"),
    path("reset-password/", PasswordResetView.as_view(), name="reset_password"),
    path(
        "reset-password/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset-password/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    re_path(
        "reset-password/complete/$",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
