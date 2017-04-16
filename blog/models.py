from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save
import uuid

# Create your models here.
#user refrences User.id as foreign key
#another comment
class BlogMain(models.Model):
	 blog_header=models.CharField(max_length=250)
	 timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

	 def __str__(self):
	 	return self.blog_header

	 class Meta:
	 	get_latest_by='timestamp'
	 	verbose_name='Blog Main'
	 	verbose_name_plural='Blog Main'


class BlogPost(models.Model):
	usr = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True, default=uuid.uuid4)
	blog_text = models.TextField(max_length=10000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# image = models.ImageField(upload_to='blog',blank=True)

	#you are going want to set up the urls as slugs


	#following function is sort of a to_string function for the admin page
	#	admin will see BlogPost objects displayed like below
	def __str__(self):
		return 'Title: ' + self.title + ', ID: ' + str(self.id) 


@receiver(pre_save, sender=BlogPost)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
	print("firex")
	# slugify ther service title
	slug = slugify(instance.title)
	exists = BlogPost.objects.filter(slug=slug).exists()
	# If the slug already exists append the slug with the id. This ensures we have no duplicate slugs
	
	if exists:
		slug = "%s-%s" % (slugify(instance.title), instance.id)
	
	instance.slug = slug