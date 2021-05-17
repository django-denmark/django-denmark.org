from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Event
from company.models import Company

# Create your views here.
class LandingpageView(ListView):
    model = Event
    template_name = "event/landingpage.html"
    ordering = ['date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        LandingpageCompany = Company.objects.all()[0:3]
        context['company_list'] = LandingpageCompany
        return context
