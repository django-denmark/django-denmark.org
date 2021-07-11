from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Company(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    logo_image = models.ImageField(
        upload_to="images/",
        null=True,
        verbose_name="Company logo",
    )
    company_name = models.CharField(max_length=145, verbose_name="Company name")
    description = models.TextField(verbose_name="Describe your companies")
    website_url = models.URLField(
        max_length=200,
        blank=True,
        validators=[
            RegexValidator(
                regex="[http]",
                message="Website URL must include https:// or http://",
                code="invalid_url",
            ),
        ],
        verbose_name="Link to your website",
    )
    relation_to_django = models.TextField(
        verbose_name="Your relation to Django",
    )
    email = models.EmailField(max_length=100)
    main_contact = models.CharField(
        max_length=100,
        verbose_name="The main point of contact",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
