from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Available titles for searching jobs
JOBTYPE_CHOICES = (
    ("PartTime", "Part-time"),
    ("FullTime", "Full-time"),
    ("Freelancer", "Freelancer"),
    ("Internship", "Internship"),
    ("Other", "Other"),
)


class Jobpost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=60, verbose_name="Job title")
    job_company_name = models.CharField(max_length=100, verbose_name="Company name")
    job_description = models.TextField(verbose_name="Describe the position")
    job_type = models.CharField(
        max_length=11, choices=JOBTYPE_CHOICES, verbose_name="Job type"
    )
    job_location = models.CharField(max_length=100, verbose_name="Location")
    job_contact_person = models.CharField(max_length=80, verbose_name="Contact person")
    job_apply_url = models.URLField(
        max_length=200,
        blank=True,
        verbose_name="Link to job application",
    )

    def __str__(self):
        return f"{self.job_title} at {self.job_company_name}"

    def get_update_url(self):
        """return URL for update view - for use in templates
        since JS is being used on frontend, making this a model method is easier
        than using url template tag to avoid showing unnecessary errors in code editors
        """
        return reverse("jobpost_update", args=[self.pk])
