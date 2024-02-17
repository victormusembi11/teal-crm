"""Lead app views."""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from lead.forms import AddLeadForm
from lead.models import Lead


@login_required
def lead_list(request):
    """Lead list view."""
    leads = Lead.objects.filter(created_by=request.user)
    return render(request, "lead/lead_list.html", {"leads": leads})


@login_required
def lead_detail(request, pk):
    """Lead detail belonging to user view."""
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    return render(request, "lead/lead_detail.html", {"lead": lead})


@login_required
def lead_delete(request, pk):
    """Delete lead and redirect to lead list view."""
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()
    messages.success(request, "Lead deleted successfully")
    return redirect("lead:lead_list")


@login_required
def lead_edit(request, pk):
    """Lead edit view."""
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == "POST":
        form = AddLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()
            messages.success(request, "Lead updated successfully")
            return redirect("lead:lead_list")

    form = AddLeadForm(instance=lead)

    return render(request, "lead/lead_edit.html", {"form": form})


@login_required
def add_lead(request):
    """Add lead view."""
    if request.method == "POST":
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)  # set to false to set created_by
            lead.created_by = request.user
            lead.save()

            messages.success(request, "Lead added successfully")
            return redirect("lead:lead_list")

    form = AddLeadForm()

    return render(request, "lead/add_lead.html", {"form": form})
