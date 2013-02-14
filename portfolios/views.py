from django.shortcuts import render
from django.conf import settings
#import PHOTOGRAPHS IS FOR GALLERY
from portfolios.models import *
from photographs.models import PhotographImage
import os


def index(request):
	image_list = PhotographImage.objects.order_by('-uploaded')[:5]
	context = {
		'home_active':'active',
		'image_list':image_list
	}
	return render(request,'portfolios/index.html',context)

def work(request):
	return render(request,'portfolios/work.html')