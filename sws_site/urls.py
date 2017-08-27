from django.http import HttpResponseRedirect
from singwithsavannah import settings
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^music', views.music, name='music'), 
    url(r'^about', views.about, name='about'), 
    url(r'^services/$', views.services, name='services'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^testimonies', views.testimonials, name='testimonies'),
    url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL + 'favicons/favicon.ico')),
    url(r'^services/(?P<slug>[\w-]+)/$', views.service_detail, name='service_detail')
]