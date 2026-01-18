"""Admin configuration for the lettings- application."""

from django.contrib import admin
from lettings.models import Address, Letting


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Admin interface options for Address.

    Displays key address fields in the Django admin list view.
    """

    list_display = ("number", "street", "city", "state", "zip_code", "country_iso_code")


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):

    """Admin interface options for Letting.

        Displays the letting title and associated address in the admin list view.
        """

    def get_queryset(self, request):
        return super().get_queryset(request)
    list_display = ("title", "get_address")
    def get_address(self, obj):
        return str(obj.address)
    get_address.short_description = "Address"

