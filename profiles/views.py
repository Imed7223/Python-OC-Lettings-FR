from django.shortcuts import render
from profiles.models import Profile


def profiles_index(request):
    profiles = Profile.objects.all()
    context = {"profiles_list": profiles}
    return render(request, "profiles_index.html", context)


def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
