from django.shortcuts import render
from driver_stats.models import Stats
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def statistics_page(request):
    fetched_statistics = Stats.objects.filter(username=request.user.username)
    context = {"fetched_statistics": fetched_statistics}

    return render(request, "stats.html", context)
