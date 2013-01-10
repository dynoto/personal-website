from django.conf.urls import patterns,url
from photographs import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^(?P<image_id>\d+)/view/$',views.view,name='view')
)