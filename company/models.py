from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm

# Create your models here.

# All fields, Company should contain with string conversion, and special validators
# and additional label, exclusion of specific fields formatting


class Company(models.Model):

    # function for valid phonenumber only contains numbers
    def only_int(value):
        if value.isdigit() == False:
            raise ValidationError("Phone number must only contain numbers.")

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    logoImage = models.ImageField(upload_to="images/", null=True)
    companyName = models.CharField(max_length=145)
    description = models.TextField()
    websiteURL = models.URLField(
        max_length=100,
        blank=True,
        validators=[
            RegexValidator(
                regex="[http]",
                message="Website URL must include https:// or http://",
                code="invalid_url",
            ),
        ],
    )
    relationToDjango = models.TextField()
    phoneNumber = models.CharField(max_length=15, blank=False, validators=[only_int])
    email = models.EmailField(max_length=100)
    mainContact = models.CharField(max_length=50)
    streetName = models.CharField(max_length=45)
    houseNumber = models.IntegerField()
    postalCode = models.IntegerField()
    region = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {} {}".format(
            self.user,
            self.companyName,
            self.description,
            self.websiteURL,
            self.relationToDjango,
            self.phoneNumber,
            self.email,
            self.mainContact,
            self.streetName,
            self.houseNumber,
            self.postalCode,
            self.region,
            self.created_at,
        )


class CompanyForm(ModelForm):
    def init(self, args, **kwargs):
        super(CompanyForm, self).__init__(args, **kwargs)

    class Meta:
        model = Company
        exclude = ("user", "created_at")
        fields = "__all__"
        labels = {
            "email": ("Email"),
            "companyName": ("Company name"),
            "logoImage": ("Company logo"),
            "description": ("Describe your company"),
            "websiteURL": ("Link to your website"),
            "relationToDjango": ("Your relation to Django"),
            "phoneNumber": ("Phone number"),
            "mainContact": ("The main point of contact"),
            "streetName": ("Street name"),
            "houseNumber": ("House number"),
            "postalCode": ("Postal code"),
            "region": ("Region"),
        }
