from django.urls import path
from django.views.generic.base import TemplateView

from .views import DeleteJobpostFormView
from .views import JobpostDetailView
from .views import JobpostFormView
from .views import JobpostView
from .views import UpdateJobpostFormView

urlpatterns = [
    path("jobpostoverview/", JobpostView.as_view(), name="jobpostoverview"),
    path("createjobpost/", JobpostFormView.as_view(), name="createjobpost"),
    path("<pk>/updateJobpost", UpdateJobpostFormView.as_view()),
    path("<pk>/deleteJobpost", DeleteJobpostFormView.as_view(), name="delete_jobpost"),
    path("<pk>/detailViewJobpost", JobpostDetailView.as_view()),
]
