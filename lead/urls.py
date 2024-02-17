"""Lead app urls."""

from django.urls import path

from . import views

app_name = "lead"

urlpatterns = [
    path("", views.lead_list, name="lead_list"),
    path("<int:pk>/", views.lead_detail, name="lead_detail"),
    path("<int:pk>/delete/", views.lead_delete, name="lead_delete"),
    path("<int:pk>/edit/", views.lead_edit, name="lead_edit"),
    path("add/", views.add_lead, name="add_lead"),
]
