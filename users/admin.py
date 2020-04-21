from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import DrowsyDriverUserCreationForm, DrowsyDriverUserChangeForm
from .models import DrowsyDriverUser


class DrowsyDriverUserAdmin(UserAdmin):
    """Create a custom admin for custom user."""

    model = DrowsyDriverUser
    add_form = DrowsyDriverUserCreationForm
    form = DrowsyDriverUserChangeForm


admin.site.register(DrowsyDriverUser, DrowsyDriverUserAdmin)
