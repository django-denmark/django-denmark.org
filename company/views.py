from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import Company
from .models import CompanyForm
from jobpost.models import Jobpost

# Create your views here.

# CreateView
class CompanyFormView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = "company/createCompanyProfile.html"
    form_class = CompanyForm
    success_url = "/company/detailViewEditUpdateProfile"

    # Checks if data input is valid and saves object
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class CompanyView(ListView):
    model = Company
    template_name = "company/companyoverview.html"


# DetailView
# CompanyDetailViewEditUpdate takes 2 parameters LoginRequiredMixin to secure different
# functionalities for users when signed in or not and ListView.
class CompanyDetailView(DetailView):
    model = Company
    template_name = "company/detailViewCompanyProfile.html"
    fields = "__all__"


class CompanyDetailViewEditUpdate(LoginRequiredMixin, ListView):
    model = Company
    template_name = "company/detailViewEditUpdateProfile.html"
    fields = "__all__"

    # get_queryset(self) secures to display Company profiles that the User is creater/owner of.
    def get_queryset(self):
        return (
            super(CompanyDetailViewEditUpdate, self)
            .get_queryset()
            .filter(user=self.request.user)
        )

    # get_context_data(self, **kwargs) makes it possible for two ListViews containing different
    # sets of data to be displayed on the same html page. In this case objects from jobpost.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myJobposts = Jobpost.objects.filter(user=self.request.user)
        context["jobpost_list"] = myJobposts
        return context


# UpdateView
class UpdateCompanyFormView(LoginRequiredMixin, UpdateView):
    model = Company
    template_name = "company/updateCompanyProfile.html"
    form_class = CompanyForm
    success_url = "/company/detailViewEditUpdateProfile"


# DeleteView
class DeleteCompanyFormView(DeleteView):
    model = Company
    template_name = "company/detailViewEditUpdateProfile.html"
    success_url = "/company/detailViewEditUpdateProfile"
