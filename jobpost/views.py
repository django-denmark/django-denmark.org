from django.shortcuts import render
from .models import Jobpost, JobpostForm
from django.views.generic import FormView, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q 

# Create your views here.
class JobpostFormView(LoginRequiredMixin, CreateView):
    model = Jobpost
    template_name = "jobpost/createjobpost.html"
    form_class = JobpostForm

    def form_valid(self, form):
        print("Hurra det virker!!!!!! jaaaaaa det gør det hurraaaa !!!!")
        obj = form.save(commit = False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    # def get_success_url(self, **kwargs):
    #     return "/company/" + str(self.object.pk) + "/detailViewEditUpdateProfile"


class JobpostView(ListView):
    model = Jobpost
    template_name = "jobpost/jobpostoverview.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query == None:
            pass
        else:
            jobpost_list = Jobpost.objects.filter(
                Q(jobTitle__icontains=query) | Q(jobCompanyName__icontains=query)
            )
            return jobpost_list

