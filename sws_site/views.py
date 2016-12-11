from django.shortcuts import render
from .models import Services
from .models import ServicesLandingPage
from .models import About

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
	return render(request, 'music.html')

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

