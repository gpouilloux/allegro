from django.conf.urls import patterns, include, url
from django.contrib import admin
from allegro import views

urlpatterns = patterns('allegro.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^list/$', 'list', name='list'),
)
