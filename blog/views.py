#from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import BlogPost, BlogMain
from django.shortcuts import render
from django.template import loader
from sws_site.models import Services
from sws_site.views import get_services
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog(request):
	#reverse the order of blog posts by created at
	#the '-' in front of created_at tells python to filter in reverse order

	all_blog_posts_list = BlogPost.objects.order_by('-created_at')

	try:
		blog_main = BlogMain.objects.latest()
	except :
		blog_main = None
		
	#archive = BlogPost.objects.filter(usr=1).order_by('-created_at')
	archive = BlogPost.objects.order_by('-created_at')

	#pagination for index of blog_posts

	query = request.GET.get("q")

	if query:
		all_blog_posts_list = all_blog_posts_list.filter(
			Q(title__icontains=query) | 
			Q(blog_text__icontains=query) 
			).distinct()

	paginator = Paginator(all_blog_posts_list, 2)
	page = request.GET.get('page')
	
	try:
		all_blog_posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		all_blog_posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		all_blog_posts = paginator.page(paginator.num_pages)


	#context dictionary standard practice for transfering necessary data to the template view
	#this makes all_blog_posts accessable from the template view
	


	context= {
		'all_blog_posts': all_blog_posts,
		'blog_main' : blog_main,
		'archive' : archive,
		'services' : get_services()
	}
	#unlike the template loader style, context needs to be the 3rd argument, not the first
	return render(request, 'blog.html', context)

#for individual 
def show(request, slug=None):

	try:
		#cant simply pass blogpost_id to get method. MUST USE 'pk =' to tell django to get by primary key 
		# blog_post = BlogPost.objects.get(pk=blogpost_id)
		blog_post = BlogPost.objects.get(slug=slug)
	except BlogPost.DoesNotExist:
		raise Http404("requested blog post does not exist.")

	context = {
		'blog_post': blog_post, 
		'services' : get_services(), 
		}


	return render(request, 'show.html', context)
