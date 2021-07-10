from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import Jobpost
from .models import JobpostForm


# Create your views here.
class JobpostFormView(LoginRequiredMixin, CreateView):
    model = Jobpost
    template_name = "jobpost/createjobpost.html"
    form_class = JobpostForm
    success_url = "/company/detailViewEditUpdateProfile"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class JobpostView(ListView):
    model = Jobpost
    template_name = "jobpost/jobpostoverview.html"

    # Makes it possible to search for a specific jobpost by filtering through all jobpost objects
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query == None:
            jobpost_list = Jobpost.objects.all()
            return jobpost_list
        else:
            jobpost_list = Jobpost.objects.filter(
                Q(jobTitle__icontains=query)
                | Q(jobCompanyName__icontains=query)
                | Q(jobLocation__icontains=query)
                | Q(jobType__icontains=query)
            )
            return jobpost_list


class JobpostDetailView(DetailView):
    model = Jobpost
    template_name = "jobpost/detailViewJobpost.html"
    fields = "__all__"


# UpdateView
class UpdateJobpostFormView(LoginRequiredMixin, UpdateView):
    model = Jobpost
    template_name = "jobpost/updateJobpost.html"
    form_class = JobpostForm
    success_url = "/company/detailViewEditUpdateProfile"


# DeleteView
class DeleteJobpostFormView(DeleteView):
    model = Jobpost
    template_name = "/company/detailViewEditUpdateProfile.html"
    success_url = "/company/detailViewEditUpdateProfile"
