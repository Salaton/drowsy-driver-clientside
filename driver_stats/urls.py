from django.urls import path
from . import views

urlpatterns = [path("", views.StatisticsListView.as_view(), name="stats")]
