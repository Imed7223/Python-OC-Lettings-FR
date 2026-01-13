from django.shortcuts import render, get_object_or_404
from profiles.models import Profile


def index(request):
    profiles = Profile.objects.all()
    context = {"profiles_list": profiles}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
