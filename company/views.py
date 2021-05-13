from django.shortcuts import render, redirect, get_object_or_404
from .models import CompanyForm, Company
from django.views.generic import FormView, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class CompanyFormView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = "company/createCompanyProfile.html"
    form_class = CompanyForm
    success_url = "/company/detailViewEditUpdateProfile"

    def form_valid(self, form):
        print("Hurra det virker!!!!!! jaaaaaa det gør det hurraaaa !!!!")
        obj = form.save(commit = False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    # def get_success_url(self, **kwargs):
    #     return "/company/" + str(self.object.pk) + "/detailViewCompanyProfile.html"

class CompanyView(ListView):
    model = Company
    template_name = "company/companyoverview.html"

# DetailView
class CompanyDetailView(DetailView):
    model = Company
    template_name = "company/detailViewCompanyProfile.html"
    fields = '__all__'

class CompanyDetailViewEditUpdate(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Company
    template_name = "company/detailViewEditUpdateProfile.html"
    fields = '__all__'

    def test_func(self):
       if self.request.user == self.request.user:
          return True
       return False

    def get_queryset(self):
        return super(CompanyDetailViewEditUpdate, self).get_queryset().filter(user=self.request.user)

    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.user == self.request.user

# UpdateView
class UpdateCompanyFormView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Company
    template_name = "company/updateCompanyProfile.html"
    form_class = CompanyForm
    success_url = './detailViewEditUpdateProfile'
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

# DeleteView
class DeleteCompanyFormView(DeleteView):
    model = Company
    template_name = "company/deleteCompanyProfile.html"
    success_url = '/company/companyoverview'
