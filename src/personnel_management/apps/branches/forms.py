from django.contrib.gis import forms
from .models import Branch
from personnel_management.apps.personnels.models import Personnel

class BranchCreateForm(forms.Form):
	name 		 = forms.CharField(label ="Name", max_length=120)
	image_facade = forms.ImageField( label="Image Facade", required=False)
	personnels   = forms.MultipleChoiceField(label = "Personnel", choices = ( (p.id,p.first_name + " " + p.last_name) for p in Personnel.objects.filter(branch__isnull= True)), required=False)

	longitude    = forms.DecimalField(label = "Latitude", max_digits=9, decimal_places=6, required=False)
	latitude     = forms.DecimalField(label = "Longitude", max_digits=9, decimal_places=6, required=False)
	location     = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 600,
                   'map_height': 400,
                   'template_name': 'gis/openlayers-osm.html',
                   'default_lat': 42.1710962,
                   'default_lon': 18.8062112,
                   'default_zoom': 6}))
	

