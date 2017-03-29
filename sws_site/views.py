from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Services, ServicesLandingPage, About, Album, Home, Contact, SocialMediaURLs
from django.http import Http404
from .forms import ContactForm


# Create your views here.


def process_contact_form(request, contact_form, redirect_target):

	form_class = contact_form

	form = form_class(data=request.POST)

	if form.is_valid():
		contact_name = request.POST.get('name', '')
		contact_email = request.POST.get('email', '')
		message_subject = request.POST.get('subject', '')
		email_message = request.POST.get('message', '')
		message_format = 'Email from %s\nEmail: %s\nMessage\n%s\n'

		final_message = message_format % (contact_name, contact_email, email_message)


def get_services():
	
	services = None

	try: 
		services = Services.objects.all()
	except: 
		services = None

	return services

def contact(request):

	try:
		contact = Contact.objects.latest()
	except Contact.DoesNotExist: 
		contact = None

	form = ContactForm()

	context = {
		'contact' : contact,
		'form' : form, 
		'services' : get_services()
	}

	return render(request, 'contact.html', context)


def home(request):

	social_media = None
	about = None
	home = None
	try:
		about = About.objects.latest()
		home = Home.objects.latest()
		social_media = SocialMediaURLs.objects.latest()
	except About.DoesNotExist:
		#raise Http404("Cannot find data") 
		about = None
	except Home.DoesNotExist:
		home = None
	except SocialMediaURLs.DoesNotExist:
		social_media=None


	context ={
		'services' : get_services(),
		'about' : about, 
		'home' : home, 
		'social_media' : social_media,
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


