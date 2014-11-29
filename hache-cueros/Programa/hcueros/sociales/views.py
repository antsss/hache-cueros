# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from sociales.models import Social
from django.template import RequestContext, loader


def index(request):
    return HttpResponse(u"Hola mundo. Estás en la seccion noticias")

#def index(request):
    #lista_ultimas_noticias = Social.objects.order_by('-fecha_inicio_publicacion')[:5]
    #template = loader.get_template('sociales/index.html')
    #context = RequestContext(request, {
     #   'lista_ultimas_noticias': lista_ultimas_noticias,
    #})
    #return HttpResponse(template.render(context))

def index(request):
    lista_ultimas_noticias = Social.objects.order_by('-fecha_inicio_publicacion')[:5]
    context = {'lista_ultimas_noticias': lista_ultimas_noticias}
    return render(request, 'sociales/index.html', context)    
    