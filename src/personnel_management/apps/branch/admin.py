from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin

from .models import Branch


# Register your models here.
class BranchAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
admin.site.register(Branch, BranchAdmin)																																																																																																																										