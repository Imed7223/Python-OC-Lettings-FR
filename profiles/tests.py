"""Tests for the profiles application views.

This module contains integration tests for the profiles index
and detail views, verifying status codes, rendered templates
and expected content.
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index_view(client):
    """Test the profiles index view.

    Ensures that the profiles index page:
    - returns a 200 HTTP status code,
    - displays the created username,
    - renders the expected template.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    user = User.objects.create(username="john")
    Profile.objects.create(user=user, favorite_city="Paris")

    url = reverse("profiles:index")
    response = client.get(url)

    assert response.status_code == 200
    assert "john" in response.content.decode()
    assert "profiles/index.html" in [t.name for t in response.templates]

    # FIX Python 3.14: dicts() → values() (lignes 32-34)
    profiles_list = list(response.context["profiles"].values("user__username", "favorite_city"))
    assert len(profiles_list) == 1
    assert profiles_list[0]["user__username"] == "john"
    assert profiles_list[0]["favorite_city"] == "Paris"


@pytest.mark.django_db
def test_profile_detail_view(client):
    """Test the profile detail view.

    Ensures that the profile detail page:
    - returns a 200 HTTP status code,
    - displays the correct username and favorite city,
    - renders the expected template.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    user = User.objects.create(username="jane")
    profile = Profile.objects.create(user=user, favorite_city="Lyon")

    url = reverse("profiles:profile", kwargs={"username": profile.user.username})
    response = client.get(url)

    assert response.status_code == 200
    assert "jane" in response.content.decode()
    assert "Lyon" in response.content.decode()
    assert "profiles/profile.html" in [t.name for t in response.templates]

    # FIX Python 3.14: dicts() → accès direct (lignes 55-58)
    profile_data = response.context["profile"]
    assert profile_data.user.username == "jane"
    assert profile_data.favorite_city == "Lyon"
