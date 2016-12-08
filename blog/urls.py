from django.conf.urls import url
from . import views


urlpatterns = [
	#singwithsavannah.com/music
    url(r'^$', views.index, name='index'),

    #routes for blog  show functionality
    #singwithsavannah.com/music/1234...n
    url(r'^(?P<blogpost_id>[0-9]+)/$', views.show, name='show'),
]