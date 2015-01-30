# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import urllib
import json

#Modelo Publicidad
class Publicidad(models.Model):
	imagen = models.ImageField(upload_to = 'banners_publicidad')	
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if self.imagen:
			self.slug = slugify(self.imagen)
		super(Publicidad, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.slug

#Modelo Candidato
class Candidato(models.Model):
	tipos_estilos = (
		(1, 'Estilo Amarillo'),
		(2, 'Estilo Azul'),
		(3, 'Estilo Morado'),
		(4, 'Estilo Naranja'),
		(5, 'Estilo Verde'),
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
	facebook = models.URLField(blank = True)
	twitter = models.URLField(blank = True)
	conoceme_foto = models.ImageField(upload_to = 'candidato_conoceme_foto')
	tipo_candidato = models.IntegerField(default = 1, choices = tipos_candidatos)
	municipio = models.CharField(max_length =  30)
	distrito = models.CharField(max_length = 30, blank = True)
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if self.nombre:
			self.slug = slugify(self.nombre)
		super(Candidato, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

	def breveDescripcion(self):
		return self.descripcion.split('\n')[0]

#modelo Compromiso
class Compromiso(models.Model):
	candidato = models.ForeignKey(Candidato)
	imagen = models.ImageField(upload_to = 'compromiso_imagen')
	texto = models.TextField()

	def __unicode__(self):
		return "Compromiso " + self.candidato.__unicode__()

#modelo Noticia
class Noticia(models.Model):
	candidato = models.ForeignKey(Candidato)
	titulo = models.CharField(max_length = 100)
	texto = models.TextField()
	destacada = models.BooleanField()
	imagen = models.ImageField(upload_to = 'noticia_imagen', blank = True)
	fecha_publicacion = models.DateField(auto_now = True, auto_now_add = True)
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if self.titulo:
			self.slug = slugify(self.titulo)
		super(Noticia, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.titulo

	def breveDescripcion(self):
		return (self.texto.split('\n')[0])[:171] + '[...]'

#modelo Galeria
class GaleriaImagenes(models.Model):
	candidato = models.ForeignKey(Candidato)
	nombre = models.CharField(max_length = 100)
	imagen = models.ImageField(upload_to = 'galeria_imagen')
	destacada = models.BooleanField()	
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if self.nombre:
			self.slug = slugify(self.nombre)
		super(GaleriaImagenes, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.candidato.nombre + ':' + self.nombre

#modelo ItemImagen
class ItemImagen(models.Model):
	galeria = models.ForeignKey(GaleriaImagenes)
	imagen = models.ImageField(upload_to = 'galeria_imagen')
	texto = models.TextField()
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if self.imagen:
			self.slug = slugify(self.imagen)
		super(ItemImagen, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.galeria.nombre + '(' + self.galeria.candidato.nombre + '):' + self.slug

#modelo ItemVideo
class Video(models.Model):
	candidato = models.ForeignKey(Candidato)
	titulo = models.CharField(max_length = 30)
	texto = models.TextField()
	destacado = models.BooleanField()
	url = models.URLField()
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if self.titulo:
			self.slug = slugify(self.titulo)
		super(Video, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.titulo

	def embed_video(self):	
		embed = 'http://www.youtube.com/oembed?url={0}&format=json'.format(self.url)
		sock = urllib.urlopen(embed)
		video = json.loads(sock.read())['html']	.replace('480', '390').replace('270', '275')
		sock.close()
		return video

	def watch_video(self):	
		embed = 'http://www.youtube.com/oembed?url={0}&format=json'.format(self.url)
		sock = urllib.urlopen(embed)
		video = json.loads(sock.read())['html']	.replace('480', '583').replace('270', '328')
		sock.close()
		return video

	

