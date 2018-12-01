from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
# Create your models here.
class Post(models.Model):
	category = models.CharField(max_length=50)
	item = models.CharField(max_length=100)
	quantity = models.IntegerField(default=0)
	document = models.FileField(upload_to='tender_docs/')
	description = models.TextField()
	elegibility = models.TextField(default='Elegibility')
	date_posted = models.DateTimeField(auto_now_add= True)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.item

	def get_absolute_url(self):
		return reverse('post-detail', kwargs= {'pk': self.pk})

class Review(models.Model):
	post = models.ForeignKey(Post, on_delete = models.PROTECT)
	document = models.FileField(upload_to='tender_docs/')
	comment = models.TextField()
	user_name = models.CharField(max_length=100)
	# author = models.ForeignKey(User, on_delete = models.CASCADE)
	date_posted = models.DateTimeField(auto_now_add= True)
	
