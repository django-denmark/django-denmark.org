from django.urls import path

from . import views



app_name = 'meetup'

urlpatterns = [
    path('', views.MeetupEventListView.as_view(),),
]