from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Services, ServicesLandingPage, About, Album, Home
from django.http import Http404

# Create your views here.


def get_services():
	
	services = None

	try: 
		services = Services.objects.all()
	except: 
		services = None

	return services

def home(request):

	about = None
	home = None
	
	try:
		about = About.objects.latest()
		home = Home.objects.latest()
	except About.DoesNotExist:
		#raise Http404("Cannot find data") 
		about = None
	except Home.DoesNotExist:
		home = None


	context ={
		'services' : get_services(),
		'about' : about, 
		'home' : home
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
		'services' : get_services()
	}

	return render(request, 'music.html', context)

def about(request):

	about = None
	
	try:
		about = About.objects.latest()
	except About.DoesNotExist:
		#raise Http404("Cannot find data")
		about = None

	context = {
		'services' : get_services(), 
		'about' : about
	}

	return render(request, 'about.html', context)

def services(request):

	services_details = None

	try:
		services_details = ServicesLandingPage.objects.latest()
	except ServicesLandingPage.DoesNotExist:
		services_details = None

	context={
		'services' : get_services(),
		'services_details' : services_details
	}

	return render(request, 'services.html', context)



def service_detail(request, slug=None):

	service = get_object_or_404(Services, slug=slug)

	context = {
		'target_service' : service, 
		'services' : get_services()
	}
	
	return render(request, 'service_detail.html', context)


