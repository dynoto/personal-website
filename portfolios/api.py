from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from portfolios.models import Technology,Project,ProjectImage

class TechnologyResource(ModelResource):
	class Meta:
		queryset = Technology.objects.all()
		resource_name = 'technology'

class ProjectResource(ModelResource):
	technologies = fields.ToManyField(TechnologyResource,'technologies',full=True)
	images = fields.ToManyField('portfolios.api.ProjectImageResource','projectImages',full=True)
	class Meta:
		queryset = Project.objects.all()
		resource_name = 'project'
		ordering = ['id']
		allowed_methods = ['get']
		limit = 6
		authorization = Authorization()
		include_resource_uri = False

class ProjectImageResource(ModelResource):
	project = fields.ToOneField('portfolios.api.ProjectResource','project')

	class Meta:
		queryset = ProjectImage.objects.all()
		resource_name = 'projectImage'