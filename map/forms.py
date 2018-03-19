from django.contrib.gis import forms
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

from . import models


class MapEntryForm(forms.ModelForm):
    
    class Meta:
        model = models.MapEntry
        widgets = {
             'location': GooglePointFieldWidget,
         }
        fields = ('name', 'location')
