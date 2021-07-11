from django.views.generic import ListView

from .models import Event
from djangodenmark.apps.companies.models import Company


class IndexView(ListView):
    model = Event
    template_name = "events/index.html"
    ordering = ["-date"]

    # Gets all Event objects and returns a sorted list by creation stamp
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        LandingpageCompany = Company.objects.all().order_by(
            "-created_at",
        )[0:3]
        context["company_list"] = LandingpageCompany
        return context


class AboutView(ListView):
    model = Event
    template_name = "events/about.html"
    ordering = ["-date"]

    # Gets all Event objects and returns a sorted list by creation stamp
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        LandingpageCompany = Company.objects.all().order_by(
            "-created_at",
        )[0:3]
        context["company_list"] = LandingpageCompany
        return context
