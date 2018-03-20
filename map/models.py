from django.utils.translation import gettext as _
from django.contrib.gis.db import models





class MapEntry(models.Model):
    
    location = models.PointField(
        verbose_name=_("Location(click on the marker to select your location on map)"),
    )
    
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    name = models.CharField(
        verbose_name=_("Name of Company"),
        help_text=_("Leave blank if it's yourself"),
        null=True,
        blank=True,
        max_length=256,
    )
    
        
    def __str__(self):
        return self.name or str(self.owner)

    class Meta:
        unique_together = ('owner', 'name')
    
    