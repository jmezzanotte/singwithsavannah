from django.conf.urls import url
from . import views


urlpatterns = [
	#singwithsavannah.com/blog
    url(r'^$', views.blog, name='blog'),

    #routes for blog show functional
    #singwithsavannah.com/blog/1234...n
    # url(r'^(?P<blogpost_id>[0-9]+)/$', views.show, name='show'),
    url(r'^(?P<slug>[\w-]+)/$', views.show, name='show'),
]