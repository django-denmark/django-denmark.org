from django.db import models
from django.forms import ModelForm
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None)
    logoImage = models.ImageField(upload_to = 'images/', null = True)
    companyName = models.CharField(max_length = 145)
    description = models.TextField()
    websiteURL = models.CharField(max_length = 100)
    relationToDjango = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="fejl")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length = 100)
    mainContact = models.CharField(max_length = 50)
    streetName = models.CharField(max_length = 45)
    houseNumber = models.IntegerField()
    postalCode = models.IntegerField()
    region = models.CharField(max_length = 45)    
    
    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {} {}'.format(self.user, self.companyName, self.description, self.websiteURL, self.relationToDjango, self.phoneNumber, self.email, self.mainContact, self.streetName, self.houseNumber, self.postalCode, self.region)


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        exclude = ('user',)
        fields = '__all__'

        def init(self, args, **kwargs):
            super(CompanyForm, self).init(args, **kwargs)