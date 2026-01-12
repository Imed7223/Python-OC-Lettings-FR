import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view_status_code(client):
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert "Orange County Lettings" in response.content.decode()


@pytest.mark.django_db
def test_index_view_template(client):
    url = reverse("index")
    response = client.get(url)
    assert "index.html" in [t.name for t in response.templates]
