from django.conf.urls import patterns, include, url
from django.contrib import admin
from allegro import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
