from django.utils.translation import gettext as _
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry


class MapEntry(models.Model):
    
    location = models.PointField(default=GEOSGeometry("POINT(56.242 11.634)"))
    
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    name = models.CharField(
        verbose_name=_("Name of place"),
        help_text=_("Leave blank if it's yourself"),
        null=True,
        blank=True,
        max_length=256,
    )
    
    class Meta:
        unique_together = ('owner', 'name')
    
    