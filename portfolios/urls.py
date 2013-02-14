from django.conf.urls import patterns, url
from portfolios import views

urlpatterns = patterns('',
	url(r'^$',views.work,name='work'),
)