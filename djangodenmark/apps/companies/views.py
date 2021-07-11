from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import CompanyForm
from .models import Company
from djangodenmark.apps.jobposts.models import Jobpost


# CreateView
class CompanyFormView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = "companies/createCompanyProfile.html"
    form_class = CompanyForm
    success_url = "/companies/detailViewEditUpdateProfile"

    # Checks if data input is valid and saves object
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class CompanyView(ListView):
    model = Company
    template_name = "companies/companyoverview.html"


# DetailView
# CompanyDetailViewEditUpdate takes 2 parameters LoginRequiredMixin to secure different
# functionalities for users when signed in or not and ListView.
class CompanyDetailView(DetailView):
    model = Company
    template_name = "companies/detailViewCompanyProfile.html"
    fields = "__all__"


class CompanyDetailViewEditUpdate(LoginRequiredMixin, ListView):
    model = Company
    template_name = "companies/detailViewEditUpdateProfile.html"
    fields = "__all__"

    # get_queryset(self) secures to display Company profiles that the User is creater/owner of.
    def get_queryset(self):
        return (
            super(CompanyDetailViewEditUpdate, self)
            .get_queryset()
            .filter(user=self.request.user)
        )

    # get_context_data(self, **kwargs) makes it possible for two ListViews containing different
    # sets of data to be displayed on the same html page. In this case objects from jobposts.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_jobposts = Jobpost.objects.filter(user=self.request.user)
        context["jobpost_list"] = my_jobposts
        return context


# UpdateView
class UpdateCompanyFormView(LoginRequiredMixin, UpdateView):
    model = Company
    template_name = "companies/updateCompanyProfile.html"
    form_class = CompanyForm
    success_url = "/companies/detailViewEditUpdateProfile"


# DeleteView
class DeleteCompanyFormView(DeleteView):
    model = Company
    template_name = "companies/detailViewEditUpdateProfile.html"
    success_url = "/companies/detailViewEditUpdateProfile"
