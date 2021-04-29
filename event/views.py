from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.
def getLandingPage(request):
    return render(request, 'event/landingpage.html')