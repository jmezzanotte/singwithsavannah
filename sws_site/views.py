from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Services, ServicesLandingPage, About, Album
from django.http import Http404

# Create your views here.

def home(request):

	services = None
	about = None
	
	try:
		about = About.objects.latest()
		services = Services.objects.all()
	except About.DoesNotExist:
		#raise Http404("Cannot find data") 
		about = None
	except Services.DoesNotExist:
		services = None

	context ={
		'services' : services,
		'about' : about
	}

	return render(request, 'home.html', context)

def music(request):

	# We are going to have to get all the related objects from Album
	# Get all objects from the database
	# I think you can get the related items within the template using this 
	#{% for album in album.albumtrack_set.all %}
	#album.albumtrack_set.all()#
	albums = Album.objects.all()


	context = {
		'albums' : albums,

	}

	return render(request, 'music.html', context)

def about(request):

	about = None
	services = None
	
	try:
		about = About.objects.latest()
		services = Services.objects.all()
	except About.DoesNotExist:
		#raise Http404("Cannot find data")
		about = None
	except Services.DoesNotExist:
		services = None

	context = {
		'services' : services, 
		'about' : about
	}

	return render(request, 'about.html', context)

def services(request):

	services = None
	services_details = None

	try:
		services = Services.objects.all()
		services_details = ServicesLandingPage.objects.latest()
	except Services.DoesNotExist:
		services = None
	except ServicesLandingPage.DoesNotExist:
		services_details = None

	context={
		'services' : services,
		'services_details' : services_details
	}

	return render(request, 'services.html', context)

