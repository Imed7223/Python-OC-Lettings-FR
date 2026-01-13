from django.db import models


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)
    country_iso_code = models.CharField(max_length=3)

    def __str__(self):
        # Les tests attendent "10 Str", donc seulement number + street
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """A rental property with a title and an associated address."""
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.title
