from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class Company(models.Model):
    
    def only_int(value): 
        if value.isdigit()==False:
            raise ValidationError('Phonenumber must not contain characters!')
    
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None)
    logoImage = models.ImageField(upload_to = 'images/', null = True)
    companyName = models.CharField(max_length = 145)
    description = models.TextField()
    websiteURL = models.URLField(max_length = 100, blank=True)
    relationToDjango = models.TextField()
    phoneNumber = models.CharField(max_length=15, blank=False, validators=[only_int])
    email = models.EmailField(max_length = 100)
    mainContact = models.CharField(max_length = 50)
    streetName = models.CharField(max_length = 45)
    houseNumber = models.IntegerField()
    postalCode = models.IntegerField()
    region = models.CharField(max_length = 45)    
    
    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {} {}'.format(self.user, self.companyName, self.description, self.websiteURL, self.relationToDjango, self.phoneNumber, self.email, self.mainContact, self.streetName, self.houseNumber, self.postalCode, self.region)


class CompanyForm(ModelForm):
    def init(self, args, **kwargs):
        super(CompanyForm, self).__init__(args, **kwargs)

    class Meta:
        model = Company
        exclude = ('user',)
        fields = '__all__'
        labels = {
            "email": ("New Email Label"),
            "companyName": ("Company name"),
            "logoImage": ("Company Logo"),
            "description": ("Describe your company"),
            "websiteURL": ("Link to your Website"),
            "relationToDjango": ("Your Relation to Django"),
            "phoneNumber": ("Phone Number"),
            "mainContact": ("The main point of contact"),
            "streetName": ("Streetname"),
            "houseNumber": ("Housenumber"),
            "postalCode": ("Postalcode"),
            "region": ("Region"),
        }
