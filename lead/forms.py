"""Lead forms."""

from django import forms

from lead.models import Lead


class AddLeadForm(forms.ModelForm):
    """Add lead form."""

    class Meta:
        """Meta class."""

        model = Lead
        fields = (
            "name",
            "email",
            "description",
            "priority",
            "status",
        )
