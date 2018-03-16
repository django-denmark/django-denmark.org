from django.contrib.gis import forms

from . import models


class MapEntryForm(forms.ModelForm):
    
    class Meta:
        model = models.MapEntry
        widgets = {
            'location': forms.OSMWidget(
                attrs={
                    'map_width': 800,
                    'map_height': 500,
                    'default_zoom': 10,
                    'default_lat': 56.242,
                    'default_lon': 11.634,
                },
            )
        }
        fields = ('name', 'location')
