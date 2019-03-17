from django.db import models
from personnel_management.apps.branch.models import Branch
# Create your models here.
class Personnel(models.Model):
	branch = models.ForeignKey(Branch, models.SET_NULL, blank=True, null=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	position_title = models.CharField(max_length=100)