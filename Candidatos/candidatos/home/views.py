from django.shortcuts import render
from home.models import Candidato, Noticia, Video, GaleriaImagenes, Compromiso, ItemImagen
import urllib
import json

##### Inicio Terminado #######
def inicio(request):
	alcaldes = Candidato.objects.all().filter(tipo_candidato = 1)
	d_locales = Candidato.objects.all().filter(tipo_candidato = 2)
	d_federales = Candidato.objects.all().filter(tipo_candidato = 3)
	return render(request, 'index.html', { "alcaldes" : alcaldes, "d_locales" : d_locales, "d_federales" : d_federales })

#### Iniocio 2 Terminado ######
def inicio2(request):
	candidatos = Candidato.objects.all()
	return render(request, 'index0.html', { "candidatos" : candidatos })

#### candidato Terminado ######
def candidato(request, n_candidato):
	candidato = Candidato.objects.get(slug = n_candidato)

	try:
		noticia_destacada = Noticia.objects.get(candidato = candidato, destacada = True)
	except:
		noticia_destacada = Noticia.objects.all()[0]

	noticias = Noticia.objects.all().filter(candidato = candidato, destacada = False)[0:2]

	try:
		video = Video.objects.get(candidato = candidato, destacado = True)
		video = embed_video(video.url)
		galeria = None
	except:
		try:
			video = None
			galeria = GaleriaImagenes.objects.get(candidato = candidato, destacada = True)
		except:
			galeria = None

	return render(request, 'micrositio/home.html', { "candidato" : candidato, "noticia_destacada":noticia_destacada, "noticias":noticias, "video":video, "galeria":galeria })

#### perfil Terminado ##############
def perfil(request, n_candidato):
	candidato = Candidato.objects.get(slug = n_candidato)
	return render(request, 'micrositio/conoceme.html', {"candidato":candidato})

####### compromisos Terminado #################
def compromisos(request, n_candidato):
	candidato = Candidato.objects.get(slug = n_candidato)
	compromisos = Compromiso.objects.all().filter(candidato = candidato)
	return render(request, 'micrositio/compromisos.html', {"candidato":candidato, "compromisos":compromisos })

####### galerias Terminado ###############
def galerias(request, n_candidato):
	candidato = Candidato.objects.get(slug = n_candidato)
	galerias = GaleriaImagenes.objects.all().filter(candidato = candidato)
	return render(request, 'micrositio/galerias.html', {"candidato":candidato, "galerias":galerias})

####### galeria Terminada ################
def galeria(request, n_candidato, i_galeria):
	candidato = Candidato.objects.get(slug = n_candidato)
	galeria = GaleriaImagenes.objects.all().filter(slug = i_galeria, candidato = candidato)
	imagenes = ItemImagen.objects.all().filter(galeria = galeria)
	return render(request, 'micrositio/galeria01.html', {"candidato":candidato, "galeria":galeria, "imagenes":imagenes})

###### noticias Terminado ##############
def noticias(request, n_candidato):
	candidato = Candidato.objects.get(slug = n_candidato)
	noticias = Noticia.objects.all().filter(candidato = candidato)
	return render(request, 'micrositio/noticias.html', { "candidato" : candidato, "noticias" : noticias })

###### noticia Terminado ################
def noticia(request, n_candidato, t_noticia):
	candidato = Candidato.objects.get(slug = n_candidato)
	noticia = Noticia.objects.get(slug = t_noticia, candidato = candidato)
	return render(request, 'micrositio/noti01.html', { "candidato":candidato, "noticia":noticia })

###### videos Terminado ################
def videos(request, n_candidato):
	candidato = Candidato.objects.get(slug = n_candidato)
	videos = Video.objects.all().filter(candidato = candidato)
	return render(request, 'micrositio/videos.html', {"candidato":candidato, "videos":videos})

def video(request):
	return render(request, 'video01.html')

################### HERRAMIENTAS #################3
def embed_video(url):	
	embed = 'http://www.youtube.com/oembed?url={0}&format=json'.format(url)
	sock = urllib.urlopen(embed)
	video = json.loads(sock.read())['html']	.replace('480', '390').replace('270', '275')
	sock.close()
	return video
