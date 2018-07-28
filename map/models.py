from django.utils.translation import gettext as _
from django.contrib.gis.db import models
from pyproj import Proj, transform
from django.utils.functional import cached_property


class MapEntry(models.Model):
    
    location = models.PointField()
    
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    name = models.CharField(
        verbose_name=_("Name of place"),
        help_text=_("Leave blank if it's yourself"),
        null=True,
        blank=True,
        max_length=256,
    )
    
    def __str__(self):
        return self.name or str(self.owner)

    class Meta:
        unique_together = ('owner', 'name')

    @cached_property
    def lat_lon(self):
        inp = Proj(init="epsg:2394")
        out = Proj(init='epsg:4326')
        lat, lon = transform(inp, out, self.location.y, self.location.x)
        return lat, lon
