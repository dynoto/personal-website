# Create your views here.
from django.http import HttpResponse
#either this
from django.template import Context, loader

#or this
from django.shortcuts import render

#import models
from photographs.models import *

def index(request):
	template = loader.get_template('photographs/index.html')
	image_list = PhotographImage.objects.order_by('-uploaded')
	context  = Context({
		'image_list': image_list,
	})
	return HttpResponse(template.render(context))

def view(request,image_id):
	image = PhotographImage.objects.order_by('-uploaded')[:5]
	context = Context({
		'image_list': image,
	})
	return render(request,'photographs/index.html',context)