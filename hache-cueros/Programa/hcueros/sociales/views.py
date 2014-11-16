# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from sociales.models import Social


def index(request):
    return HttpResponse(u"Hola mundo. Estás en la seccion noticias")

def index(request):
    lista_ultimas_noticias = Social.objects.order_by('-fecha_inicio_publicacion')[:5]
    salida = ', '.join([p.titulo for p in lista_ultimas_noticias])
    return HttpResponse(salida)