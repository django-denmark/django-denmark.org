from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView

from .models import Event
from company.models import Company

# Create your views here.
class LandingpageView(ListView):
    model = Event
    template_name = "event/landingpage.html"
    ordering = ["-date"]

    # Gets all Event objects and returns a sorted list by creation stamp
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        LandingpageCompany = Company.objects.all().order_by(
            "-created_at",
        )[0:3]
        context["company_list"] = LandingpageCompany
        return context
