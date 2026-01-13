import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_index_view(client):
    address = Address.objects.create(
        number=1,
        street="Main Street",
        city="City",
        state="ST",
        zip_code="12345",
        country_iso_code="USA",
    )
    Letting.objects.create(title="Test Letting", address=address)

    url = reverse("lettings:index")  # <-- ici
    response = client.get(url)

    assert response.status_code == 200
    assert "Test Letting" in response.content.decode()
    assert "lettings/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_letting_detail_view(client):
    address = Address.objects.create(
        number=2,
        street="Second Street",
        city="City",
        state="ST",
        zip_code="67890",
        country_iso_code="USA",
    )
    letting = Letting.objects.create(title="Detail Letting", address=address)

    url = reverse("lettings:letting", kwargs={"letting_id": letting.id})  # <-- ici
    response = client.get(url)

    assert response.status_code == 200
    assert "Detail Letting" in response.content.decode()
    assert "lettings/letting.html" in [t.name for t in response.templates]
