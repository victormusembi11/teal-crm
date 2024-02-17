"""Accounts views."""

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from accounts.models import UserProfile


def signup(request):
    """User create form view."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            # create a profile for the user
            UserProfile.objects.create(user=user)

            return redirect("/")  # TODO: redirect to the login page

    form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})
