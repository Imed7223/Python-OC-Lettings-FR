from django.contrib import admin
from django.urls import path, include
from . import views
from django.http import HttpRequest, HttpResponse


def trigger_error(request: HttpRequest) -> HttpResponse:
    """
       Vue pour tester Sentry, déclenche une erreur 500
       """
    raise ZeroDivisionError("Test Sentry - division par zéro")


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include(("lettings.urls", "lettings"), namespace="lettings")),
    path("profiles/", include(("profiles.urls", "profiles"), namespace="profiles")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]

handler404 = "oc_lettings_site.views.custom_404"
handler500 = "oc_lettings_site.views.custom_500"
