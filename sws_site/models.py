from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.
class ServicesLandingPage(models.Model):
	services_headline=models.CharField(max_length=250)
	services_desc=models.TextField()
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
		'''	
			The reason we need get latest by is because the user 
			can ultimately enter many different headlines or content 
			text to this table. We want them to have record of the old 
			entries but also be able only to use the newest ones. 
			Specifying get latest by will allow us to use only the 
			latest record later on. 
			
		'''
		verbose_name = "Services Landing Page"
		verbose_name_plural="Services Landing Page"
		get_latest_by="timestamp"


class Services(models.Model):
	service = models.CharField(max_length=50, unique=True, blank=True)
	slug = models.SlugField(unique=True, default=uuid.uuid4)
	service_desc = models.TextField()
	service_headline = models.CharField(max_length=250)
	service_image=models.ImageField() 
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.service

	def __str__(self):
		return self.service

	class Meta:
		verbose_name = "Services"
		verbose_name_plural = "Services"



