from django.urls import path
from django.views.generic.base import TemplateView

from .views import CompanyDetailView
from .views import CompanyDetailViewEditUpdate
from .views import CompanyFormView
from .views import CompanyView
from .views import DeleteCompanyFormView
from .views import UpdateCompanyFormView

urlpatterns = [
    path("companyoverview/", CompanyView.as_view(), name="companyoverview"),
    path(
        "createCompanyProfile/", CompanyFormView.as_view(), name="createCompanyProfile"
    ),
    path("<pk>/updateCompanyProfile", UpdateCompanyFormView.as_view()),
    path(
        "<pk>/deleteCompanyProfile",
        DeleteCompanyFormView.as_view(),
        name="delete_company",
    ),
    path("<pk>/detailViewCompanyProfile", CompanyDetailView.as_view()),
    path("detailViewEditUpdateProfile/", CompanyDetailViewEditUpdate.as_view()),
]
