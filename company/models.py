from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class Company(models.Model):
    logoImage = models.ImageField(upload_to = 'images/', null = True)
    companyName = models.CharField(max_length = 145)
    description = models.TextField()
    websiteURL = models.CharField(max_length = 100)
    relationToDjango = models.TextField()
    phoneNumber = models.CharField(max_length = 11)
    email = models.CharField(max_length = 100)
    mainContact = models.CharField(max_length = 50)
    streetName = models.CharField(max_length = 45)
    houseNumber = models.CharField(max_length = 25)
    postalCode = models.CharField(max_length = 4)
    region = models.CharField(max_length = 45)    
    
    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {}'.format(self.companyName, self.description, self.websiteURL, self.relationToDjango, self.phoneNumber, self.email, self.mainContact, self.streetName, self.houseNumber, self.postalCode, self.region)


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = '__all__'