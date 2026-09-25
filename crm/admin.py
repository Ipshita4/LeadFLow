from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company_name",
        "stage",
        "score",
        "source",
        "created_at",
    )

    list_filter = (
        "stage",
        "source",
        "company_size",
    )

    search_fields = (
        "name",
        "email",
        "company_name",
    )