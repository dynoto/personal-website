from django.db import models
from datetime import datetime, date, time

class Tag(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField(default=datetime.now(),blank=True);	


	def __unicode__(self):
		return self.name

class Article(models.Model):
	tags = models.ManyToManyField(Tag,blank=True)
	title = models.CharField(max_length=400)
	content = models.TextField()
	created = models.DateTimeField(default=datetime.now(),blank=True);
	script = models.FileField(upload_to="media/blogs/",blank=True)
	stylesheet = models.FileField(upload_to="media/blogs",blank=True)
	like = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	comment = models.CharField(max_length=10000)
	created = models.DateTimeField(default=datetime.now(),blank=True);

	def __unicode__(self):
		return self.comment