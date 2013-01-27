from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from photographs.models import Image,Category

class ImageResource(ModelResource):
	class Meta:
		queryset = Image.objects.all()
		#optional, if resource name not included it is generated from the Class Name minus 'resource'
		resource_name = 'image' 
		# excludes = ['uploaded']
		ordering = ['uploaded','name','likes','star']

		# limit = 6
		authorization = Authorization()
		include_resource_uri = False