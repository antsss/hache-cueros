from django.db import models

# Create your models here.
class Social(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    tipo_social = models.CharField(max_length=1)
    def __unicode__(self):              
        return self.texto