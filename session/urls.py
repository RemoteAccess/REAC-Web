from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
		
    url(r'^index/$', views.index),
    url(r'^logout/$', views.logout_page),
    url(r'^login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', views.register),
    url(r'^home/$', views.home),
    url(r'^api/getemail', views.getemail),
    url(r'^api/getip', views.getip),
    url(r'^api/setip', views.getip),
    url(r'^api/login', views.apilogin),
)
