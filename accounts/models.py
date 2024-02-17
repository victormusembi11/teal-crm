"""Account models."""

from django.contrib.auth.models import User
from django.db import models

from team.models import Team


class UserProfile(models.Model):
    """User profile model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active_team = models.ForeignKey(
        Team,
        related_name="userprofiles",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def get_active_team(self):
        if self.active_team:
            return self.active_team
        else:
            return Team.objects.filter(members__in=[self.user.id]).first()

    def __str__(self) -> str:
        """Model str representation."""
        return self.user.username
