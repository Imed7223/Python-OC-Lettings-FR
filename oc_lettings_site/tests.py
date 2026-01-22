"""Tests for the home page view of the OC Lettings site.

This module verifies that the index view is reachable and renders
the expected content and template.
"""

import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_view_status_code(client):
    """Test that the index view returns a 200 status and expected text.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    # Créer des données pour tester le contexte
    address = Address.objects.create(
        number=123, street="Test St", city="Test City",
        state="CA", zip_code="12345", country_iso_code="US"
    )
    Letting.objects.create(title="Test Home", address=address)

    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Orange County Lettings" in response.content.decode()

    # FIX Python 3.14: dicts() → values()
    lettings_list = list(response.context["lettings"].values("title"))
    assert len(lettings_list) == 1
    assert lettings_list[0]["title"] == "Test Home"


@pytest.mark.django_db
def test_index_view_template(client):
    """Test that the index view renders the correct template.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("index")
    response = client.get(url)

    assert "oc_lettings_site/index.html" in [t.name for t in response.templates]
    # FIX ligne 35: template précis (pas générique "index.html")
