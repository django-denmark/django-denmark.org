from django.urls import path
from django.views.generic.base import TemplateView
from .views import CompanyView, CompanyFormView, UpdateCompanyFormView, DeleteCompanyFormView, CompanyDetailView
from . import views

urlpatterns = [
    path('companyoverview/', CompanyView.as_view(), name = "companyoverview"),
    path('createCompanyProfile/', CompanyFormView.as_view(), name = "createCompanyProfile"),
    path('<pk>/updateCompanyProfile', UpdateCompanyFormView.as_view()),
    path('<pk>/deleteCompanyProfile', DeleteCompanyFormView.as_view()),
    path('<pk>/detailViewCompanyProfile', CompanyDetailView.as_view()),
]