from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
	usr = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	blog_text = models.TextField(max_length=10000)
	date_created = models.DateTimeField(auto_now_add=True)