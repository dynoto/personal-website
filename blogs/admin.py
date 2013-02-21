from django.contrib import admin
import django_tut.settings as settings
from blogs.models import Tag,Article,Comment

class TagAdmin(admin.ModelAdmin):
	list_display = ('name','created')

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','like','created','script','stylesheet')
	class Media:
		js = ['/static/js/tiny_mce/tiny_mce.js','/static/js/tiny_mce/tiny_mce_setup.js']

class CommentAdmin(admin.ModelAdmin):
	list_display = ('comment','created')

admin.site.register(Tag,TagAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)