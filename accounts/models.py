"""Account models."""

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """User profile model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Model str representation."""
        return self.user.username
