"""Admin configuration for the profiles application."""

from django.contrib import admin
from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin interface options for Profile.

    Displays the user and favorite city in the list view and
    enables searching by username and favorite city.
    """

    list_display = ("user", "favorite_city")
    search_fields = ("user__username", "favorite_city")
