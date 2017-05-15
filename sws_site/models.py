from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.conf import settings
# from django.core.files.storage import FileSystemStorage
import uuid
# import shutil
import os


# if settings.DEBUG:
# 	fs = FileSystemStorage(location=settings.STATICFILES_DIRS[0])
# else:
# 	fs = FileSystemStorage(location=settings.STATIC_ROOT)


# def get_upload_path(instance, filename):
#     """ creates unique-Path & filename for upload """
#     return os.path.join('audio', 'albums', slugify(instance.name), filename)

# def get_track_upload_path(instance, filename):
# 	return os.path.join('audio', 'albums', slugify(instance.album.name), filename)

# def get_file_name(instance, filename):
# 	return filename


class Home(models.Model):
	homepage_headline = models.CharField(max_length=500)
	mini_music_headline = models.CharField(max_length=500)
	mini_music_description = models.TextField()
	mini_music_url = models.URLField(max_length=500)
	mini_music_img = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.homepage_headline

	def __str__(self):
		return self.homepage_headline

	class Meta:
		verbose_name = 'Home Page'
		verbose_name_plural = 'Home Page'
		get_latest_by = 'timestamp'


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

		'''
		verbose_name = 'Services Landing Page'
		verbose_name_plural = 'Services Landing Page'
		get_latest_by = 'timestamp'

class Services(models.Model):
	service = models.CharField(max_length=50, unique=True, blank=True, default=uuid.uuid4)
	slug = models.SlugField(unique=True, default=uuid.uuid4)
	description = models.TextField()
	headline = models.CharField(max_length=250)
	service_img = models.CharField(max_length=200)
	service_icon = models.CharField(max_length=200)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.service

	def __str__(self):
		return self.service

	class Meta:
		verbose_name = 'Services'
		verbose_name_plural = 'Services'

class Contact(models.Model):
	headline = models.CharField(max_length=200)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	
	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = 'Contact'
		get_latest_by = 'timestamp'



class About(models.Model):
	headline = models.CharField(max_length=500)
	homepage_headline = models.CharField(max_length=500)
	summary = models.TextField()
	description = models.TextField()
	about_img = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.headline

	def __str__(self):
		return self.headline

	class Meta:
		verbose_name = 'About'
		verbose_name_plural = 'About'
		get_latest_by = 'timestamp'

class Album(models.Model):

	name = models.CharField(max_length=200)
	album_img = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	market_place = models.URLField(max_length=250, blank=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class AlbumTrack(models.Model):

	album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album')
	track_name = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return os.path.basename(self.track_name)

	def __str__(self):
		return os.path.basename(self.track_name)

class SocialMediaURLs(models.Model):

	facebook = models.URLField(max_length=350)
	twitter = models.URLField(max_length=350)
	youtube = models.URLField(max_length=350)
	instagram = models.URLField(max_length=350)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	class Meta:
		verbose_name = 'Social Media URL'
		verbose_name_plural = 'Social Media URLS'
		get_latest_by = 'timestamp'


class Testimonials(models.Model):
	testimony = models.TextField()
	written_by = models.CharField(max_length=150)
	location = models.TextField(max_length=150)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.written_by

	def __str__(self):
		return self.written_by

	class Meta:
		verbose_name = 'Testimonials'
		verbose_name_plural = 'Testimonials'


# @receiver(pre_delete, sender=AlbumTrack)
# def pre_delete_album_track(sender, instance, *args, **kwargs):
# 	instance.track.delete(False)

@receiver(pre_delete, sender=Album)
def pre_delete_album_folder(sender, instance, *args, **kwargs):
	'''This function will remove the directory of the album if the user deletes it.
		Deleting and albumn is a dangerous operation for this site. It will delete all the files 
		associated with an album.'''
	try:
		shutil.rmtree(os.path.join(settings.PROJECT_ENVIRON, 'static_cdn', 'audio', 'albums', slugify(instance.name)))
		shutil.rmtree(os.path.join(settings.PROJECT_SRC, 'static', 'audio', 'albums', slugify(instance.name)))
	except FileNotFoundError as e :
		print(e)

# @receiver(pre_delete, sender=Services)
# def pre_delete_service_image(sender, instance, *args, **kwargs):
# 	'''Method to delete the images from the server when user deletes image from admin'''
# 	try:
# 		os.remove(instance.image.path)
# 		os.remove(instance.icon.path)
# 	except FileNotFoundError as e:
# 		print(e)

# @receiver(pre_delete, sender=About)
# def pre_delete_about_image(sender, instance, *args, **kwargs):
# 	'''Method to delete images from the about folder when user deletes image from admin'''
# 	try:
# 		os.remove(instance.image.path)
# 	except FileNotFoundError as e:
# 		print(e)

@receiver(pre_save, sender=Services)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
	
	# slugify ther service title
	slug = slugify(instance.service)
	exists = Services.objects.filter(slug=slug).exists()
	# If the slug already exists append the slug with the id. This ensures we have no duplicate slugs
	
	if exists:
		slug = "%s-%s" % (slugify(instance.service), instance.id)
	
	instance.slug = slug


# The decorator is replacint this step
#pre_save.connect(pre_save_post_receiver, sender=Services)

