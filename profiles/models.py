"""Models for the profiles application.

This module defines the Profile model, which extends the built-in
Django User model with additional domain-specific information.
"""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Represents an extended user profile.

    The profile is linked one-to-one with Django's built-in User
    model and stores additional information such as the user's
    favorite city.

    Attributes:
        user: One-to-one relationship to the Django User instance.
        favorite_city: Optional name of the user's favorite city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return a human-readable representation of the profile.

        Returns:
            The username associated with this profile.
        """
        return self.user.username
