from django.contrib.auth.models import User
from django.db import models


class Plan(models.Model):
    """Plan model."""

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    max_leads = models.IntegerField()
    max_clients = models.IntegerField()

    def __str__(self):
        """Plan str representation."""
        return self.name


class Team(models.Model):
    """Team model."""

    plan = models.ForeignKey(
        Plan, related_name="teams", blank=True, null=True, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name="teams")
    created_by = models.ForeignKey(
        User, related_name="created_teams", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Team str representation."""
        return self.name

    def get_plan(self):
        """Get the team plan."""
        if self.plan:
            return self.plan
        else:
            if Plan.objects.count() > 0:
                self.plan = Plan.objects.all().first()
                self.save()
            else:
                plan = Plan.objects.create(
                    name="Free", price=0, max_leads=3, max_clients=3
                )
                self.plan = plan
                self.save()

            return self.plan
