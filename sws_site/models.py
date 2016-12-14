from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid

# Create your models here.
class ServicesLandingPage(models.Model):
	services_headline=models.CharField(max_length=250)
	services_desc=models.TextField()
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.services_headline

	def __str__(self):
		return self.services_headline


	class Meta:
		'''	
			The reason we need get latest by is because the user 
			can ultimately enter many different headlines or content 
			text to this table. We want them to have record of the old 
			entries but also be able only to use the newest ones. 
			Specifying get latest by will allow us to use only the 
			latest record later on. 

			test

		'''
		verbose_name = 'Services Landing Page'
		verbose_name_plural = 'Services Landing Page'
		get_latest_by = 'timestamp'

class Services(models.Model):
	service = models.CharField(max_length=50, unique=True, blank=True, default=uuid.uuid4)
	slug = models.SlugField(unique=True, default=uuid.uuid4)
	description = models.TextField()
	headline = models.CharField(max_length=250)
	image = models.ImageField()
	icon = models.ImageField()
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.service

	def __str__(self):
		return self.service

	class Meta:
		verbose_name = 'Services'
		verbose_name_plural = 'Services'


class About(models.Model):
	headline = models.CharField(max_length=500)
	summary = models.TextField()
	description = models.TextField()
	image = models.ImageField(upload_to='about')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.headline

	def __str__(self):
		return self.headline


	class Meta:
		verbose_name = 'About'
		verbose_name_plural = 'About'
		get_latest_by = 'timestamp'






def pre_save_post_receiver(sender, instance, *args, **kwargs):
	
	# slugify ther service title
	slug = slugify(instance.service)
	exists = Services.objects.filter(slug=slug).exists()
	# If the slug already exists append the slug with the id. This ensures we have no duplicate slugs
	
	if exists:
		slug = "%s-%s" % (slugify(instance.service), instance.id)
	
	instance.slug = slug



pre_save.connect(pre_save_post_receiver, sender=Services)

