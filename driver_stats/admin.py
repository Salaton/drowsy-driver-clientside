from django.contrib import admin
from driver_stats.models import Stats

# Register your models here.


class StatsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stats, StatsAdmin)
