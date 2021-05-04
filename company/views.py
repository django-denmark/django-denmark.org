from django.shortcuts import render
from django.views.generic import TemplateView
from company.models import companyForm, addressForm, contactInformationForm
from django.views.generic.edit import FormView

# Create your views here.
class CompanyView(TemplateView):
    template_name = "company/companyoverview.html"

class CompanyFormView(FormView):
    template_name = 'company/createCompanyProfile.html'
    form_class = companyForm
    success_url = '/'

    def form_valid(self, form):
        print("Hurra det virker!!!!!! jaaaaaa det gør det hurraaaa !!!!")
        return super().form_valid(form)