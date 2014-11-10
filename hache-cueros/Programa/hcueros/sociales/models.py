from django.db import models

# Create your models here.
class Social(models.Model):
	class Meta:
		verbose_name_plural = 'Sociales'

	TIPO_PUBILACION = (
    ('F', 'Filosofia'),
    ('N', 'Noticia'),
    )

	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	#tipo_social = models.CharField(max_length=1)
	tipo_social = models.CharField(max_length=1, choices=TIPO_PUBILACION, default='N')
	fecha_inicio_publicacion = models.DateField(auto_now=False)
	fecha_fin_publicacion = models.DateField(auto_now=False)
    
	def __unicode__(self):
		return self.titulo


class Foto(models.Model):
	class Meta:
		verbose_name_plural = 'Fotos'

	imagen = models.ImageField(upload_to='FotosSociales', verbose_name='Fotos')
	visible = models.BooleanField(default=False)
	social = models.ForeignKey(Social)