from django.contrib import admin
from portfolios.models import Project,ProjectImage,Technology

class TechnologyAdmin(admin.ModelAdmin):
	list_display = ('name','description')

class ImageAdmin(admin.ModelAdmin):
	list_display = ('project','name','url')

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name','url')
	

admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectImage,ImageAdmin)
admin.site.register(Technology,TechnologyAdmin)