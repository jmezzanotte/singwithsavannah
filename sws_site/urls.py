from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^music', views.music, name='music'), 
    url(r'^about', views.about, name='about')
]