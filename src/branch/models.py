from django.db import models
from .AS3_storage import FacadeImageStorage

# Create your models here.
class Branch(models.Model):
	name = models.CharField(max_length=120)
	facade_image = models.FileField(storage=FacadeImageStorage, blank=True, null=True)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)