from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Advert(models.Model):
	image = models.ImageField(default= 'default_business.jpg', upload_to = 'business_pics')
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	email = models.EmailField()
	products = models.ManyToManyField('Item')
	hours = models.CharField(max_length=100, default= '10:00AM – 08:00PM (Mon-Sat)')
	details = models.TextField()
	date_posted = models.DateTimeField(auto_now_add= True)
	author = models.ForeignKey(User, on_delete = models.CASCADE)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('advert-detail', kwargs= {'pk': self.pk})


class Item(models.Model):
    item = models.CharField(max_length=30)

    def __str__(self):
    	return self.item