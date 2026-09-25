from django.db import models
from .scoring import score_lead


class Lead(models.Model):

    STAGES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("qualified", "Qualified"),
        ("proposal", "Proposal"),
        ("won", "Won"),
        ("lost", "Lost"),
    ]

    SOURCES = [
        ("organic", "Organic Search"),
        ("paid", "Paid Ads"),
        ("referral", "Referral"),
        ("social", "Social Media"),
        ("direct", "Direct"),
    ]

    COMPANY_SIZES = [
        ("1-10", "1-10 employees"),
        ("11-50", "11-50 employees"),
        ("51-200", "51-200 employees"),
        ("200+", "200+ employees"),
    ]

    TIMELINES = [
        ("now", "Ready now"),
        ("quarter", "This quarter"),
        ("exploring", "Just exploring"),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField()

    company_name = models.CharField(
        max_length=120,
        blank=True
    )

    company_size = models.CharField(
        max_length=10,
        choices=COMPANY_SIZES,
        default="1-10"
    )

    timeline = models.CharField(
        max_length=10,
        choices=TIMELINES,
        default="exploring"
    )

    message = models.TextField(blank=True)

    source = models.CharField(
        max_length=20,
        choices=SOURCES,
        default="direct"
    )

    stage = models.CharField(
        max_length=20,
        choices=STAGES,
        default="new"
    )

    score = models.PositiveIntegerField(default=0)

    deal_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.score = score_lead(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.company_name}"