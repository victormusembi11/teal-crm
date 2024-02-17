"""Admin configuration for accounts app."""

from django.contrib import admin

from .models import UserProfile

admin.site.register(UserProfile)
