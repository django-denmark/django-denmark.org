from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class Address(models.Model):
    streetName = models.CharField(max_length = 45)
    houseNumber = models.CharField(max_length = 25)
    postalCode = models.CharField(max_length = 4)
    region = models.CharField(max_length = 45)

    def __str__(self):
        return '{} {} {} {}'.format(self.streetName, self.houseNumber, self.postalCode, self.region)

class ContactInformation(models.Model):
    phoneNumber = models.CharField(max_length = 11)
    email = models.CharField(max_length = 100)
    mainContact = models.CharField(max_length = 50)

    def __str__(self):
        return '{} {} {}'.format(self.phoneNumber, self.email, self.mainContact)

class Company(models.Model):
    companyName = models.CharField(max_length = 145)
    companyAddress = models.ForeignKey(Address, on_delete = models.CASCADE)
    #companyAddress = models.OneToOneField(Address, on_delete = models.CASCADE)
    description = models.TextField()
    companyContactInformation = models.ForeignKey(ContactInformation, on_delete = models.CASCADE)
    websiteURL = models.CharField(max_length = 100)
    relationToDjango = models.TextField()

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.companyName, self.companyAddress, self.description, self.companyContactInformation, self.websiteURL, self.relationToDjango)

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class ContactInformationForm(ModelForm):
    class Meta:
        model = ContactInformation
        fields = '__all__'

class CompanyForm(ModelForm):
    #companyAddress = AddressForm
    #companyContactInformation = ContactInformationForm
    class Meta:
        model = Company
        exclude = ('companyAddress', 'companyContactInformation')
        #fields = ['companyName', 'companyAddress', 'description', 'companyContactInformation', 'websiteURL', 'relationToDjango']
        fields = '__all__'



