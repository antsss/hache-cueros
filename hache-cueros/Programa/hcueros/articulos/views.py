from django.shortcuts import render_to_response
from articulos.models import Articulo
from django.template import RequestContext

def catalogo_hache(request):
	productos_hache = Articulo.objects.all()
	return render_to_response('catalogo_hache.html', {'productos_hache': productos_hache}, 
		context_instance = RequestContext(request) )


def catalogo_nah(request):
	productos_nah = Articulo.objects.all()
	return render_to_response('catalogo_nah.html', {'productos_nah': productos_nah}, 
		context_instance = RequestContext(request) )


# Create your views here.
