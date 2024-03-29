from django.urls import path

from .views import AboutView
from .views import IndexView


app_name = "events"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
]
