from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from sociales.models import Social
from sociales import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^sociales/$', ListView.as_view(model=Social), name='sociales'),
)