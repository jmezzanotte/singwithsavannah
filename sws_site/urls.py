from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^music', views.music, name='music'), 
    url(r'^about', views.about, name='about'), 
    url(r'^services', views.services, name='services'),
    url(r'^(?P<slug>[\w-]+)/$', views.service_detail, name='service_detail')
]