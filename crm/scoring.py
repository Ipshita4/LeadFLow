SIZE_POINTS = {
    "1-10": 10,
    "11-50": 20,
    "51-200": 30,
    "200+": 25,
}

SOURCE_POINTS = {
    "referral": 25,
    "organic": 20,
    "paid": 15,
    "social": 10,
    "direct": 10,
}

TIMELINE_POINTS = {
    "now": 30,
    "quarter": 15,
    "exploring": 0,
}


def score_breakdown(lead):
    """Return each reason contributing to a lead's score."""

    parts = [
        (
            f"Company size: {lead.company_size}",
            SIZE_POINTS.get(lead.company_size, 0),
        ),
        (
            f"Source: {lead.source}",
            SOURCE_POINTS.get(lead.source, 0),
        ),
        (
            f"Timeline: {lead.timeline}",
            TIMELINE_POINTS.get(lead.timeline, 0),
        ),
        (
            "Detailed message",
            10 if len(lead.message) > 50 else 0,
        ),
    ]

    return parts


def score_lead(lead):
    total = sum(
        points
        for reason, points in score_breakdown(lead)
    )

    return min(total, 100)