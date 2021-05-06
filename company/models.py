from django.db import models
from django.forms import ModelForm
from django import forms
from django.core.validators import RegexValidator

# Create your models here.

class Company(models.Model):
    companyName = models.CharField(max_length = 145)
    description = models.TextField()
    websiteURL = models.CharField(max_length = 100)
    relationToDjango = models.TextField()
    # phoneNumber = models.CharField(max_length = 11)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="fejl")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    email = models.EmailField(max_length = 100)
    mainContact = models.CharField(max_length = 50)
    streetName = models.CharField(max_length = 45)
    houseNumber = models.IntegerField()
    postalCode = models.IntegerField()
    region = models.CharField(max_length = 45)    

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {}'.format(self.companyName, self.description, self.websiteURL, self.relationToDjango, self.phoneNumber, self.email, self.mainContact, self.streetName, self.houseNumber, self.postalCode, self.region)


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = '__all__'