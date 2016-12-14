from django.shortcuts import render
from .models import Services, ServicesLandingPage, About, Album


# Create your views here.

def home(request):

	services = Services.objects.all()
	about = About.objects.latest()

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

	# Give us the latest entry, based on the timestamp of when the record was added
	services = Services.objects.all()
	about = About.objects.latest()

	context = {
		'services' : services,
		'about' : about
	}

	return render(request, 'about.html', context)

def services(request):

	services = Services.objects.all()
	services_details = ServicesLandingPage.objects.latest()
	

	context={
		'services' : services,
		'services_details' : services_details
	}

	return render(request, 'services.html', context)

