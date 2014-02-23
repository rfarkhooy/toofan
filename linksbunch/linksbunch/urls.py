from django.conf.urls import patterns, include, url


#urlpatterns = patterns((r'^bookmarks/', include('bookmarks.urls')),)
urlpatterns = patterns('',
                      (r'^bookmarks/', include('bookmarks.urls')),)
