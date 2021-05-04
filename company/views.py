from django.shortcuts import render, redirect, get_object_or_404
from .models import CompanyForm, Company
from django.views.generic import FormView, ListView, TemplateView

# Create your views here.

class CompanyFormView(FormView):
    template_name = "company/createCompanyProfile.html"
    form_class = CompanyForm
    success_url = '/'

    def form_valid(self, form):
        print("Hurra det virker!!!!!! jaaaaaa det gør det hurraaaa !!!!")
        return super().form_valid(form)


class CompanyView(ListView):
    model = Company
    template_name = "company/companyoverview.html"
