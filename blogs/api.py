from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from blogs.models import Article,Tag

class TagResource(ModelResource):
	class Meta:
		queryset = Tag.objects.all()
		resource_name = 'tag'


class ArticleResource(ModelResource):

	class Meta:
		queryset = Article.objects.all()
		ordering = ['created']
		resource_name = 'article'
		limit = 6
		authorization = Authorization()
		include_resource_uri = False
		allowed_methods = ['get']