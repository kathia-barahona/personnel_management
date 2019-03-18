from storages.backends.s3boto3 import S3Boto3Storage
from django.contrib.gis.db import models

# Create your models here.
class Branch(models.Model):
	name = models.CharField(max_length=120)
	facade_image = models.ImageField(storage=S3Boto3Storage(), blank=True, null=True)
	location = models.PointField()
