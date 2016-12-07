from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
#user refrences User.id as foreign key
#another comment
class BlogPost(models.Model):
	usr = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	blog_text = models.TextField(max_length=10000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	#following function is sort of a to_string function for the admin page
	#	admin will see BlogPost objects displayed like below
	def __str__(self):
		return 'Title: ' + self.title + ', ID: ' + str(self.id) 