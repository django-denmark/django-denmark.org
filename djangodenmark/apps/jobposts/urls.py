from django.urls import path

from . import views

urlpatterns = [
    path("", views.JobpostSearchView.as_view(), name="jobpost_search"),
    path("create/", views.JobpostCreateView.as_view(), name="jobpost_create"),
    # path("<pk>/", views.JobpostDetailView.as_view(), name="jobpost_detail"),  # TBD
    path("<pk>/update", views.JobpostUpdateView.as_view(), name="jobpost_update"),
    path(
        "<pk>/delete",
        views.JobpostDeleteView.as_view(),
        name="jobpost_delete",
    ),
]
