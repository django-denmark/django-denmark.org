from django.shortcuts import render, redirect, get_object_or_404
from .models import CompanyForm, Company
from django.views.generic import FormView, ListView, UpdateView, CreateView, DeleteView, DetailView

# Create your views here.

class CompanyFormView(CreateView):
    model = Company
    template_name = "company/createCompanyProfile.html"
    form_class = CompanyForm
    success_url = '/company/companyoverview'

    def form_valid(self, form):
        print("Hurra det virker!!!!!! jaaaaaa det gør det hurraaaa !!!!")
        return super().form_valid(form)


class CompanyView(ListView):
    model = Company
    template_name = "company/companyoverview.html"

# DetailView
class CompanyDetailView(DetailView):
    model = Company
    template_name = "company/detailViewCompanyProfile.html"
    fields = '__all__'

# UpdateView
class UpdateCompanyFormView(UpdateView):
    model = Company
    template_name = "company/updateCompanyProfile.html"
    fields = '__all__'
    success_url = '/company/companyoverview'

# DeleteView
class DeleteCompanyFormView(DeleteView):
    model = Company
    template_name = "company/deleteCompanyProfile.html"
    success_url = '/company/companyoverview'
