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
	nombre = models.CharField(max_length = 200, verbose_name = 'Nombre del Candidato')
	descripcion = models.TextField(verbose_name = 'Descripción personal:')
	fotografia = models.ImageField(upload_to = 'candidato_foto', verbose_name = 'Fotografía del Candidato')
	banner = models.ImageField(upload_to = 'candidato_banner', verbose_name = 'Banner de micrositio')
	estilo = models.IntegerField(default = 1, choices = tipos_estilos, verbose_name = 'Estilo del micrositio')
	partido_politico = models.CharField(max_length = 50, verbose_name = 'Partido Político')
	facebook = models.URLField(blank = True, verbose_name = 'URL de Facebook')
	twitter = models.URLField(blank = True, verbose_name = 'URL de Twitter')
	conoceme_foto = models.ImageField(upload_to = 'candidato_conoceme_foto', verbose_name = 'Fotografía del Perfíl')
	tipo_candidato = models.IntegerField(default = 1, choices = tipos_candidatos, verbose_name = 'Tipo de candidato')
	municipio = models.CharField(max_length =  30, verbose_name = 'Municipio')
	distrito = models.CharField(max_length = 30, blank = True, verbose_name = 'Distrito')
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
	candidato = models.ForeignKey(Candidato, verbose_name = 'Compromiso del candidato')
	imagen = models.ImageField(upload_to = 'compromiso_imagen', verbose_name = 'Imagen de la sección')
	texto = models.TextField(verbose_name = 'Texto del Compromiso')

	def __unicode__(self):
		return "Compromiso de " + self.candidato.__unicode__()

#modelo Noticia
class Noticia(models.Model):
	candidato = models.ForeignKey(Candidato, verbose_name='Noticia del Candidato')
	titulo = models.CharField(max_length = 100, verbose_name='Título de la noticia')
	texto = models.TextField(verbose_name='Texto de la noticia')
	destacada = models.BooleanField(verbose_name='¿La noticia es destacada?')
	imagen = models.ImageField(upload_to = 'noticia_imagen', blank = True, verbose_name='Imagen de la noticia')
	fecha_publicacion = models.DateField(auto_now = True, auto_now_add = True, verbose_name='Fecha de publicación')
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
	candidato = models.ForeignKey(Candidato, verbose_name = 'Galeria del candidato')
	nombre = models.CharField(max_length = 100, verbose_name = 'Nombre de la galeria')
	imagen = models.ImageField(upload_to = 'galeria_imagen', verbose_name = 'Imagen de portada')
	destacada = models.BooleanField(verbose_name = '¿La galeria es destacada?')	
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if self.nombre:
			self.slug = slugify(self.nombre)
		super(GaleriaImagenes, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.candidato.nombre + ':' + self.nombre

#modelo ItemImagen
class ItemImagen(models.Model):
	galeria = models.ForeignKey(GaleriaImagenes, verbose_name='Imagen de la Galería:')
	imagen = models.ImageField(upload_to = 'galeria_imagen', verbose_name='Imagen')
	texto = models.TextField(verbose_name='Texto de la imagen')
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if self.imagen:
			self.slug = slugify(self.imagen)
		super(ItemImagen, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.galeria.nombre + '(' + self.galeria.candidato.nombre + '):' + self.slug

#modelo ItemVideo
class Video(models.Model):
	candidato = models.ForeignKey(Candidato, verbose_name='Video del candidato:')
	titulo = models.CharField(max_length = 30, verbose_name='Título del Video')
	texto = models.TextField(verbose_name='Descripción del Video')
	destacado = models.BooleanField(verbose_name = '¿El video es destacado?')
	url = models.URLField(verbose_name='URL del video de youtube')
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

	

