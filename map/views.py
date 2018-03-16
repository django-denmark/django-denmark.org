from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from . import forms
from . import models


class MapView(ListView):
    
    model = models.MapEntry
    template_name = "map/map.html"
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return ListView.dispatch(self, request, *args, **kwargs)


class MapSavedView(TemplateView):
    
    template_name = "map/saved.html"
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return ListView.dispatch(self, request, *args, **kwargs)


class MapCreateView(CreateView):
    
    model = models.MapEntry
    form_class = forms.MapEntryForm
    template_name = "map/create.html"
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return CreateView.dispatch(self, request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        
        return redirect("map:saved")
