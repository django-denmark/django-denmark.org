from django.urls import path

from . import views

urlpatterns = [
    path("jobpostoverview/", views.JobpostView.as_view(), name="jobpostoverview"),
    path("createjobpost/", views.JobpostFormView.as_view(), name="createjobpost"),
    path("<pk>/updateJobpost", views.UpdateJobpostFormView.as_view()),
    path(
        "<pk>/deleteJobpost",
        views.DeleteJobpostFormView.as_view(),
        name="delete_jobpost",
    ),
    path("<pk>/detailViewJobpost", views.JobpostDetailView.as_view()),
]
