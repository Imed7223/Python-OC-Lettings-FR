import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index_view(client):
    user = User.objects.create(username="john")
    Profile.objects.create(user=user, favorite_city="Paris")

    url = reverse("profiles_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "john" in response.content.decode()
    # Django enregistre le template comme 'profiles_index.html'
    assert "profiles_index.html" in [t.name for t in response.templates]
    # ou : assert any("profiles_index.html" in t.name for t in response.templates)


@pytest.mark.django_db
def test_profile_detail_view(client):
    user = User.objects.create(username="jane")
    profile = Profile.objects.create(user=user, favorite_city="Lyon")

    url = reverse("profile", kwargs={"username": profile.user.username})
    response = client.get(url)

    assert response.status_code == 200
    assert "jane" in response.content.decode()
    assert "Lyon" in response.content.decode()
    # Idem ici : nom simple du template
    assert "profile.html" in [t.name for t in response.templates]
    # ou : assert any("profile.html" in t.name for t in response.templates)
