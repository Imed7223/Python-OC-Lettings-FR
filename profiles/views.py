import logging
from django.shortcuts import render, get_object_or_404
from profiles.models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """Display the list of profiles."""
    logger.info("Affichage de la liste des profils")
    profiles = Profile.objects.all()
    context = {"profiles_list": profiles}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Display details for a single profile."""
    logger.info("Affichage du profil pour l'utilisateur %s", username)
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
