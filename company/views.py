from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CompanyView(TemplateView):
    template_name = "company/companyoverview.html"