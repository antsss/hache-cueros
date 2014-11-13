from django.contrib import admin
from articulos.models import Articulo, Categoria

class CategoriaAdmin(admin.ModelAdmin):
	filter_horizontal = ["articulos"]
	


# Register your models here.
admin.site.register(Articulo)
admin.site.register(Categoria, CategoriaAdmin)





