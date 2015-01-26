from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

#Modelo Publicidad
class Publicidad(models.Model):
	imagen = models.ImageField(upload_to = 'banners_publicidad')

class Candidato(models.Model):
	tipos_estilos = (
		(1, 'Estilo de minisitio 1'),
		(2, 'Estilo de minisitio 2'),
		(3, 'Estilo de minisitio 3'),
		(4, 'Estilo de minisitio 4'),
	)
	tipos_candidatos = (
		(1, 'Alcalde'),
		(2, 'Diputado Local'),
		(3, 'Diputado Federal'),
	)
	nombre = models.CharField(max_length = 200)
	descripcion = models.TextField()
	fotografia = models.ImageField(upload_to = 'candidato_foto')
	banner = models.ImageField(upload_to = 'candidato_banner')
	estilo = models.IntegerField(default = 1, choices = tipos_estilos)
	partido_politico = models.CharField(max_length = 50)
	tipo_candidato = models.IntegerField(default = 1, choices = tipo_candidato)
	municipio = models.CharField(max_length =  30)
	distrito = models.CharField(max_length = 30)