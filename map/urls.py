from django.urls import path

from . import views



app_name = 'map'

urlpatterns = [
    path('', views.MapView.as_view(), name='map'),
    path('create/', views.MapCreateView.as_view(), name='create'),
    path('saved/', views.MapSavedView.as_view(), name='saved'),
]