import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index_view(client):
    user = User.objects.create(username="john")
    Profile.objects.create(user=user, favorite_city="Paris")

    url = reverse("profiles:index")  # <-- namespace + name
    response = client.get(url)

    assert response.status_code == 200
    assert "john" in response.content.decode()
    assert "profiles/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile_detail_view(client):
    user = User.objects.create(username="jane")
    profile = Profile.objects.create(user=user, favorite_city="Lyon")

    url = reverse("profiles:profile", kwargs={"username": profile.user.username})
    response = client.get(url)

    assert response.status_code == 200
    assert "jane" in response.content.decode()
    assert "Lyon" in response.content.decode()
    assert "profiles/profile.html" in [t.name for t in response.templates]
