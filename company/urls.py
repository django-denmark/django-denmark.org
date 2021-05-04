from django.urls import path
from django.views.generic.base import TemplateView
from .views import CompanyView, CompanyFormView

urlpatterns = [
    path('companyoverview/', CompanyView.as_view(), name = "companyoverview"),
    path('createCompanyProfile/', CompanyFormView.as_view() , name = "createCompanyProfile")
]