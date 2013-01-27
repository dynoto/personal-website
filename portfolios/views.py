from django.shortcuts import render
from django.conf import settings
from photographs.models import *
import os


def index(request):
	image_list = Image.objects.order_by('-uploaded')[:5]
	context = {
		'home_active':'active',
		'image_list':image_list
	}
	return render(request,'portfolios/index.html',context)