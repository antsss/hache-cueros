from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hcueros.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sociales/', include('sociales.urls', namespace='sociales')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^deployer/', include('deployer.urls')),
    url(r'^contacto/', include('contact_form.urls')),
    url(r'^noticias/$', 'sociales.views.noticias'), # $ para que sea vista independiente
   # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)