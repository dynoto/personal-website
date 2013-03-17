from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
from blogs.models import *
import twitter

def index(request):
	return render(request,'blogs/index.html')

def view(request,blog_id):
	blog = Article.objects.select_related().get(id=blog_id)
	print blog.created
	context = Context({
		'blog':blog,
	})
	return render(request,'blogs/view.html',context)