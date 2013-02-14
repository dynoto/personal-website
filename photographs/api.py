from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from photographs.models import PhotographImage,Category

class PhotographImageResource(ModelResource):
	class Meta:
		queryset = PhotographImage.objects.all()
		#optional, if resource name not included it is generated from the Class Name minus 'resource'
		resource_name = 'photographs' 
		# excludes = ['uploaded']
		ordering = ['uploaded','name','likes','star']
		allowed_methods = ['get','put','patch']
		limit = 6
		authorization = Authorization()
		include_resource_uri = False

	def hydrate_likes(self,bundle):
		primarykey = bundle.obj.id
		imagelikes = PhotographImage.objects.get(pk=primarykey)
		bundle.data['likes'] = imagelikes.likes + 1
		return bundle