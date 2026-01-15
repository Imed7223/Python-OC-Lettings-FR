"""Models for the lettings application.

This module defines the data structures used to represent
postal addresses and rental properties (lettings) in the system.
"""

from django.db import models


class Address(models.Model):
    """Represents a postal address.

    Attributes:
        number: The street number as a positive integer.
        street: The street name.
        city: The city name.
        state: The state, region or province name.
        zip_code: The postal or ZIP code.
        country_iso_code: The ISO 3166-1 alpha-3 country code.
    """

    number = models.PositiveIntegerField()
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)
    country_iso_code = models.CharField(max_length=3)

    def __str__(self):
        """Return a human-readable representation of the address.

        Returns:
            A string containing the street number and street name.
        """
        # Les tests attendent "10 Str", donc seulement number + street
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Represents a rental property.

    A letting is defined by a title and a one-to-one relationship
    with an Address instance.

    Attributes:
        title: The public title of the letting.
        address: The associated Address instance.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        """Django model metadata for Letting."""

        verbose_name_plural = "Addresses"

    def __str__(self):
        """Return the letting title as its string representation.

        Returns:
            The title of the letting.
        """
        return self.title
