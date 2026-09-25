from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead

        fields = [
            "name",
            "email",
            "company_name",
            "company_size",
            "timeline",
            "message",
        ]

        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "What are you looking to solve?",
                }
            ),
        }