"""Dashboard views."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard_view(request):
    """Dashboard view."""
    return render(request, "dashboard/dashboard.html")
