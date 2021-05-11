from django.urls import path
from django.views.generic.base import TemplateView
from .views import JobpostView, JobpostFormView

urlpatterns = [
    path('jobpostoverview/', JobpostView.as_view(), name = "jobpostoverview"),
    path('createjobpost/', JobpostFormView.as_view(), name = "createjobpost"),
]