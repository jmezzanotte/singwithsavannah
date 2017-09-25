from .models import Services, ServicesLandingPage, About, Album, Home, Contact, SocialMediaURLs, Testimonials
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.http import Http404
from .forms import ContactForm


def process_contact_form(request, contact_form, redirect_target):

    form = contact_form(data=request.POST)

    if form.is_valid():
        contact_name = request.POST.get('name', '')
        contact_email = request.POST.get('email', '')
        message_subject = request.POST.get('subject', '')
        email_message = request.POST.get('message', '')
        message_format = 'Email from %s\n\nEmail: %s\n\nMessage:\n\n%s\n\n\nSent through singwithsavannah.com'

        final_message = message_format % (contact_name, contact_email, email_message)

        email = EmailMessage(
            message_subject,
            final_message,
            "singwithsavannah.com" + '',
            ["singwithsavannah@gmail.com"],
            headers={'Reply-To': contact_email}
        )

        email.send()
        messages.success(request, "Thank you for your email!")
        return redirect(redirect_target)
    else:
        messages.error(request, "Oops! Your email was not sent.")
        return redirect(redirect_target)


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

    form = ContactForm

    if request.method == 'POST':
        print ("Request method POST")
        print (request)
        return process_contact_form(request, form, "contact/#id_message")

    context = {
        'contact': contact,
        'form': form,
        'services': get_services()
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
        # raise Http404("Cannot find data")
        about = None
    except Home.DoesNotExist:
        home = None
    except SocialMediaURLs.DoesNotExist:
        social_media = None

    context = {
        'services': get_services(),
        'about': about,
        'home': home,
        'social_media': social_media,
    }

    return render(request, 'home.html', context)


def music(request):
    # We are going to have to get all the related objects from Album
    # Get all objects from the database
    # I think you can get the related items within the template using this
    # {% for album in album.albumtrack_set.all %}
    # album.albumtrack_set.all()#
    albums = Album.objects.all()

    context = {
        'albums': albums,
        'services': get_services()
    }

    return render(request, 'music.html', context)


def testimonials(request):
    try:
        testimonies = Testimonials.objects.all()
    except:
        testimonies = None

    context = {
        'services': get_services(),
        'testimonies': testimonies
    }

    return render(request, 'testimonials.html', context)


def about(request):
    try:
        about = About.objects.latest()
    except About.DoesNotExist:
        # raise Http404("Cannot find data")
        about = None

    context = {
        'services': get_services(),
        'about': about
    }

    return render(request, 'about.html', context)


def services(request):
    try:
        services_details = ServicesLandingPage.objects.latest()
    except ServicesLandingPage.DoesNotExist:
        services_details = None

    context = {
        'services': get_services(),
        'services_details': services_details
    }

    return render(request, 'services.html', context)


def service_detail(request, slug=None):
    service = get_object_or_404(Services, slug=slug)

    context = {
        'target_service': service,
        'services': get_services()
    }

    return render(request, 'service_detail.html', context)


def page_not_found(request):
    context = {
        'services': get_services()
    }

    return render(request, "404.html", context, status=400)


def server_error(request):
    context = {
        'services': get_services()
    }

    return render(request, "500.html", context, status=500)


def bad_request(request):
    context = {
        'services': get_services()
    }

    return render(request, "403.html", context, status=500)
