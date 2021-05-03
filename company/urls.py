from django.urls import path
from django.views.generic.base import TemplateView
from .views import CompanyView

urlpatterns = [
    path('companyoverview/', CompanyView.as_view(), name = "companyoverview"),
]