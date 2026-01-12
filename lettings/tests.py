import pytest
from django.urls import reverse
from lettings.models import Letting, Address


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

    url = reverse("lettings_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Test Letting" in response.content.decode()
    assert "lettings_index.html" in [t.name for t in response.templates]
    # ou :
    # assert any("lettings_index.html" in t.name for t in response.templates)


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

    url = reverse("letting", kwargs={"letting_id": letting.id})
    response = client.get(url)

    assert response.status_code == 200
    assert "Detail Letting" in response.content.decode()
    assert "letting.html" in [t.name for t in response.templates]
    # ou :
    # assert any("letting.html" in t.name for t in response.templates)


@pytest.mark.django_db
def test_address_str():
    address = Address.objects.create(
        number=10,
        street="Str",
        city="City",
        state="ST",
        zip_code="12345",
        country_iso_code="USA",
    )
    assert str(address) == "10 Str"


@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number=20,
        street="Another Street",
        city="City",
        state="ST",
        zip_code="67890",
        country_iso_code="USA",
    )
    letting = Letting.objects.create(title="Nice house", address=address)
    assert str(letting) == "Nice house"
