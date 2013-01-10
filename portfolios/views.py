from django.shortcuts import render
from django.conf import settings
import os


def index(request):
	context = {
		'STATIC_ROOT' : settings.STATIC_ROOT,
		'MEDIA_ROOT'  : settings.MEDIA_ROOT,
	}
	return render(request,'portfolios/index.html',context)