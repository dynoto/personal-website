from django.contrib import admin
from photographs.models import Category,Image

class ImageAdmin(admin.ModelAdmin):
	#fields = ['name','filename','description']
	list_display = ('name','star','likes','uploaded','image_s','image_m','image_l')
	list_filter = ('uploaded','likes')

#class ImageInline(admin.StackedInline):
	# model = Image
	# extra = 1

#class CategoryAdmin(admin.ModelAdmin):
	#inlines = [ImageInline]
	#list_display = ['name']

admin.site.register(Category)
admin.site.register(Image,ImageAdmin)
