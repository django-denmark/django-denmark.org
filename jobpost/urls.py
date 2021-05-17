from django.urls import path
from django.views.generic.base import TemplateView
from .views import JobpostView, JobpostFormView, UpdateJobpostFormView, DeleteJobpostFormView, JobpostDetailView

urlpatterns = [
    path('jobpostoverview/', JobpostView.as_view(), name = "jobpostoverview"),
    path('createjobpost/', JobpostFormView.as_view(), name = "createjobpost"),
    path('<pk>/updateJobpost', UpdateJobpostFormView.as_view()),
    path('<pk>/deleteJobpost', DeleteJobpostFormView.as_view()),
    path('<pk>/detailViewJobpost', JobpostDetailView.as_view()),
]