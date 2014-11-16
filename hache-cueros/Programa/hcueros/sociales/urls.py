from django.conf.urls import patterns, url

from sociales import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)