from django.contrib import admin

# Register your models here.

from .models import Company, Address, ContactInformation

admin.site.register(Company)
admin.site.register(Address)
admin.site.register(ContactInformation)