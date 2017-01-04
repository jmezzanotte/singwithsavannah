#from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import BlogPost
from django.shortcuts import render
from django.template import loader
from sws_site.models import Services
from sws_site.views import get_services

# Create your views here.
def blog(request):
	#reverse the order of blog posts by created at
	#the '-' in front of created_at tells python to filter in reverse order
	all_blog_posts = BlogPost.objects.filter(usr=1).order_by('-created_at')
	#context dictionary standard practice for transfering necessary data to the template view
	#this makes all_blog_posts accessable from the template view
	context= {
		'all_blog_posts': all_blog_posts,
		'services' : get_services()
	}
	#unlike the template loader style, context needs to be the 3rd argument, not the first
	return render(request, 'blog.html', context)

#for individual 
def show(request, blogpost_id):

	try:
		#cant simply pass blogpost_id to get method. MUST USE 'pk =' to tell django to get by primary key 
		blog_post = BlogPost.objects.get(pk=blogpost_id)

	except BlogPost.DoesNotExist:
		raise Http404("requested blog post does not exist.")


	return render(request, 'show.html', {'blog_post': blog_post, 'services' : get_services()})
