from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


#TASTYPIE APIS
from photographs.api import PhotographImageResource
from portfolios.api import ProjectResource , ProjectImageResource
photographimage_resource = PhotographImageResource()
project_resource = ProjectResource()
projectImage_resource = ProjectImageResource()

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'django_tut.views.home', name='home'),
    # url(r'^django_tut/', include('django_tut.foo.urls')),
    url(r'^$','portfolios.views.index',name="home"),
    url(r'^photographs/',include('photographs.urls',namespace="photographs")),
    url(r'^projects/',include('portfolios.urls',namespace="projects")),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(project_resource.urls)),
    url(r'^api/', include(projectImage_resource.urls)),
    url(r'^api/', include(photographimage_resource.urls)),
)

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
