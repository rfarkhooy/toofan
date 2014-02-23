"""Mapping URLs for Bookmarks service accross UrlsBunch"""
__author__ = 'roozbeh'

from django.conf.urls.defaults import patterns, url

# Apps
from bookmarks import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),)
