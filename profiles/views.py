"""Views for the profiles application.

This module contains views responsible for displaying the list
of user profiles and the details of a single profile, with
logging for basic monitoring.
"""

import logging
from django.shortcuts import render, get_object_or_404
from profiles.models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """Display the list of profiles.

    Retrieves all Profile objects and renders the profiles index page.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        HttpResponse: The rendered profiles index page.
    """
    logger.info("Affichage de la liste des profils")
    profiles = Profile.objects.all()
    context = {"profiles_list": profiles}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Display details for a single profile.

    Retrieves a Profile instance based on the related User username
    and renders the profile detail page. Raises a 404 error if the
    profile does not exist.

    Args:
        request: HttpRequest object representing the current request.
        username: Username of the associated User.

    Returns:
        HttpResponse: The rendered profile detail page.
    """
    logger.info("Affichage du profil pour l'utilisateur %s", username)
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
