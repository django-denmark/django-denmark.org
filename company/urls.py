from django.urls import path
from django.views.generic.base import TemplateView
from .views import CompanyView, CompanyFormView
from . import views

urlpatterns = [
    path('companyoverview/', CompanyView.as_view(), name = "companyoverview"),
    path('createCompanyProfile/', CompanyFormView.as_view(), name = "createCompanyProfile"),
]