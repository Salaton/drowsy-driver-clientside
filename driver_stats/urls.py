from django.urls import path
from . import views

urlpatterns = [path("", views.statistics_page, name="stats")]
