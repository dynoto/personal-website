from django.db import models

class Technology(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(blank=True, max_length=200)
	description = models.TextField(blank=True)
	technologies = models.ManyToManyField(Technology)

	def __unicode__(self):
		return self.name


class ProjectImage(models.Model):
	project = models.ForeignKey(Project,related_name='projectImages')
	name = models.CharField(max_length=200,default='-')
	url = models.CharField(max_length=200,null=True,blank=True)

	def __unicode__(self):
		return self.name

