from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import JobpostForm
from .models import Jobpost


# Create your views here.
class JobpostCreateView(LoginRequiredMixin, CreateView):
    model = Jobpost
    template_name = "jobpost/jobpost_create.html"
    form_class = JobpostForm
    success_url = "/company/detailViewEditUpdateProfile"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class JobpostSearchView(ListView):
    model = Jobpost
    template_name = "jobpost/jobpost_search.html"

    # Makes it possible to search for a specific jobpost by filtering through all jobpost objects
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is None:
            jobpost_list = Jobpost.objects.all()
            return jobpost_list
        else:
            jobpost_list = Jobpost.objects.filter(
                Q(job_title__icontains=query)
                | Q(job_company_name__icontains=query)
                | Q(job_location__icontains=query)
                | Q(job_type__icontains=query)
            )
            return jobpost_list


# class JobpostDetailView(DetailView):
#   model = Jobpost
# there was never any template made for a detail view - commenting out for now
# currently detail is shown via a modal in JobpostSearchView / jobpost_search.html


# UpdateView
class JobpostUpdateView(LoginRequiredMixin, UpdateView):
    model = Jobpost
    template_name = "jobpost/jobpost_update.html"
    form_class = JobpostForm
    success_url = "/company/detailViewEditUpdateProfile"


# DeleteView
class JobpostDeleteView(DeleteView):
    model = Jobpost
    template_name = "/company/detailViewEditUpdateProfile.html"
    success_url = "/company/detailViewEditUpdateProfile"
