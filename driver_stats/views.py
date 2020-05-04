from django.shortcuts import render
from driver_stats.models import Stats

# Create your views here.
def statistics_page(request):
    fetched_statistics = Stats.objects.filter(username=request.user.username)
    context = {"fetched_statistics": fetched_statistics}

    return render(request, "stats.html", context)
