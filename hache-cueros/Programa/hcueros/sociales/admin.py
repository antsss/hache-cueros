from django.contrib import admin
from sociales.models import Social, Foto
from imagekit.admin import AdminThumbnail


class FotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagen_thumbnail')

# Register your models here.
admin.site.register(Social)
admin.site.register(Foto, FotoAdmin)






