from django.db import models
from datetime import datetime, date,time

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __unicode__(self):
		return self.name

class PhotographImage(models.Model):
	category = models.ForeignKey(Category,related_name="photographImages")
	name = models.CharField(max_length=200)
	description = models.TextField()
	image_s = models.CharField(max_length=200,null=True,blank=True)
	image_m = models.CharField(max_length=200,null=True,blank=True)
	image_l = models.CharField(max_length=200,null=True,blank=True)
	likes = models.IntegerField(default=0)
	uploaded = models.DateTimeField(default=datetime.now(),blank=True)
	star = models.NullBooleanField()

	def __unicode__(self):
		return self.name

	def save(self,*args,**kwargs):
		# USING PICASA CDN - IF SIZE 144PX IS DETECTED, SAVE AS 320PX AND PROPAGATE TO OTHER SIZES
		image_link = self.image_s.rsplit('/s144/')
		if len(image_link) > 1:
			self.image_s = image_link[0] +  '/s320/' + image_link[1]
			self.image_m = image_link[0] +  '/s1000/' + image_link[1]
			self.image_l = image_link[0] +  '/s0/' + image_link[1]

		super(PhotographImage,self).save(*args,**kwargs)