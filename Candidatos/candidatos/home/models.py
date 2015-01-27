# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

#Modelo Publicidad
class Publicidad(models.Model):
	imagen = models.ImageField(upload_to = 'banners_publicidad')

	def __unicode__(self):
		return self.imagen

#Modelo Candidato
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
	tipo_candidato = models.IntegerField(default = 1, choices = tipos_candidatos)
	municipio = models.CharField(max_length =  30)
	distrito = models.CharField(max_length = 30)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		if self.nombre:
			self.slug = slugify(self.nombre)
		super(Candidato, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

#modelo Compromiso
class Compromiso(models.Model):
	candidato = models.ForeignKey(Candidato)
	imagen = models.ImageField(upload_to = 'compromiso_imagen')
	texto = models.TextField()

	def __unicode_(self):
		return self.candidado + ">" + self.texto[:15]

#modelo Noticia
class Noticia(models.Model):
	candidato = models.ForeignKey(Candidato)
	titulo = models.CharField(max_length = 100)
	texto = models.TextField()
	imagen = models.ImageField(upload_to = 'noticia_imagen')
	fecha_publicacion = models.DateField(auto_now = True, auto_now_add = True)

	def __unicode_(self):
		return self.titulo

#modelo Galeria
class Galeria(models.Model):
	niveles = (
		(1, 'Muy Importante'),
		(2, 'Importante'),
		(3, 'Normal'),
		(4, 'No tan importante'),
		(5, 'No importante'),		
	)
	tipos_galerias = (
		(1, 'Galeria de Imágenes'),
		(2, 'Galeria de Videos'),
	)
	candidato = models.ForeignKey(Candidato)
	nombre = models.CharField(max_length = 100)
	nivel = models.IntegerField(default = 3, choices = niveles)
	tipo_galeria = models.IntegerField(default = 1, choices = tipos_galerias)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		if self.nombre:
			self.slug = slugify(self.nombre)
		super(Galeria, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

#modelo ItemImagen
class ItemImagen(models.Model):
	galeria = models.ForeignKey(Galeria)
	imagen = models.ImageField(upload_to = 'galeria_imagen')
	texto = models.TextField()

#modelo ItemVideo
class ItemVideo(models.Model):
	galeria = models.ForeignKey(Galeria)
	url = models.URLField()
	texto = models.TextField()

