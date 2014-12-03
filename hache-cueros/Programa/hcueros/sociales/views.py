# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from sociales.models import Social
from django.template import RequestContext

def noticias(request):
    ultimas_noticias = Social.objects.all()
    return render_to_response('noticias.html', {'noticias_recientes': ultimas_noticias}, 
        context_instance = RequestContext(request) )

