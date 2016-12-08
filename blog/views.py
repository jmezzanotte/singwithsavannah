#from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
# Create your views here.
def index(request):
	all_blog_posts = BlogPost.objects.all()
	html = ''
	for blog_post in all_blog_posts:
		url='/blog/' + str(blog_post.id)
		html += '<a href="' + url + '"> '+ blog_post.title +'</a>'
	return HttpResponse(html)

def show(request, blogpost_id):
	return HttpResponse("<h1>This page is to check blog_post link to database. id: " + str(blogpost_id) + "</h1>")
