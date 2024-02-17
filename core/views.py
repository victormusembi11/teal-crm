"""Core views."""

from django.shortcuts import render


def home(request):
    """Home view."""
    return render(request, "core/index.html")


def about(request):
    """About view."""
    return render(request, "core/about.html")
