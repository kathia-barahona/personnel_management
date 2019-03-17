from .AS3_storage import FacadeImageStorage
from location_field.models.spatial import LocationField
from django.contrib.gis.db import models

# Create your models here.
class Branch(models.Model):
	name = models.CharField(max_length=120)
	facade_image = models.FileField(storage=FacadeImageStorage, blank=True, null=True)
	location = models.PointField()
