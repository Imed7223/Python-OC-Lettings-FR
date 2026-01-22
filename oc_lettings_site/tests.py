"""Tests for the home page view of the OC Lettings site.

This module verifies that the index view is reachable and renders
the expected content and template.
"""

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view_status_code(client):
    """Test that the index view returns a 200 status and expected text.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Orange County Lettings" in response.content.decode()


@pytest.mark.django_db
def test_index_view_template(client):
    """Test that the index view renders the correct template.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("index")
    response = client.get(url)

    assert "index.html" in [t.name for t in response.templates]
