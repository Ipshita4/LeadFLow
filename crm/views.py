from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import LeadForm


def normalize_source(utm_source):
    source_mapping = {
        "google": "organic",
        "bing": "organic",
        "facebook": "social",
        "instagram": "social",
        "linkedin": "social",
        "referral": "referral",
    }

    return source_mapping.get(utm_source.lower(), "direct")


def landing_page(request):

    if request.method == "POST":
        form = LeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)

            utm_source = request.GET.get("utm_source", "direct")
            lead.source = normalize_source(utm_source)

            lead.save()

            messages.success(
                request,
                "Thanks! We'll be in touch soon."
            )

            return redirect("landing_page")

    else:
        form = LeadForm()

    return render(
        request,
        "crm/landing.html",
        {"form": form}
    )
