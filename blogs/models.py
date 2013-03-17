from django.db import models
from datetime import datetime, date, time
from django.db.models import signals
import django_tut.settings as settings
import twitter

def tweet_to_account(sender,instance,created,**kwargs):
	if(created):
		api = twitter.Twitter(
			auth=twitter.OAuth( '156908431-RleGgAQssuDv8vgwK9Gv43tWAQKxJBg1ZOpVPPo',
						'E2tFbNSIbToJcwmK27Ax5jhOQUzfcnarUEmypaZtQ',
						'5fLRBbVCR2WGCwxttHXAhA',
						'mPWJDidNBJfDG7J0rfJUOomKBY8XL79SFTjDMGHjAU'
			)
		)
		tweet = 'BLOG: '+instance.title+'. '+settings.DJANGO_DOMAIN_NAME+'blogs/'+str(instance.id)+'/view/'
		api.statuses.update(status=tweet)

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

signals.post_save.connect(tweet_to_account,sender=Article)