from django.urls import path
from . import views
from .views import LandingpageView

urlpatterns = [
    path('', LandingpageView.as_view(), name='landingpage'),
]