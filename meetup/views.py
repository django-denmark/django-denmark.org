from django.shortcuts import render
from django.utils import timezone
from .models import MeetupEvent
from django.views.generic import ListView
from datetime import datetime

# Create your views here.
class MeetupEventListView(ListView):
    template_name = 'meetup/meetup.html'
    def get_queryset(self):
        now = timezone.now()
        return MeetupEvent.objects.filter(date__gte=now).order_by('date')