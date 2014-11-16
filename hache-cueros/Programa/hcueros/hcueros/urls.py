from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hcueros.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sociales/', include('sociales.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
