from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __unicode__(self):
		return self.name

class Image(models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=200)
	description = models.TextField()
	#filename = models.CharField(max_length=200,null=True)
	filename = models.FileField(upload_to='images/%Y/%m/%d',max_length=200,null=True)
	likes = models.IntegerField(default=0)
	uploaded = models.DateTimeField()
	star = models.NullBooleanField()

	def __unicode__(self):
		return self.name