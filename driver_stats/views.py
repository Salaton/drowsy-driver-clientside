from django.shortcuts import render
from django.views.generic import ListView
from driver_stats.models import Stats
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# @login_required()
# def statistics_page(request):
#     fetched_statistics = Stats.objects.filter(username=request.user.username)
#     context = {"fetched_statistics": fetched_statistics}

#     return render(request, "stats.html", context)


class StatisticsListView(LoginRequiredMixin, ListView):
    template_name = "stats.html"
    context_object_name = "fetched_statistics"
    paginate_by = 10
    login_url = "login"

    def get_queryset(self):
        """Filter by the username.."""
        return Stats.objects.filter(user=self.request.user)
