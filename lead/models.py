"""Lead models."""

from django.contrib.auth.models import User
from django.db import models


class Lead(models.Model):
    """Lead model."""

    CHOICES_PRIORITY = (
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    )

    CHOICES_STATUS = (
        ("new", "New"),
        ("contacted", "Contacted"),
        ("won", "Converted"),
        ("rejected", "Rejected"),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    priority = models.CharField(
        max_length=6, choices=CHOICES_PRIORITY, default="medium"
    )
    status = models.CharField(max_length=9, choices=CHOICES_STATUS, default="new")
    created_by = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Lead str representation."""
        return self.name
