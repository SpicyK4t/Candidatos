from django.shortcuts import render
from home.models import Candidato

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

def candidato(request, n_candidato):
	candidato = Candidato.objects.get(slug = n_candidato)
	
	return render(request, 'micrositio/home.html', { "candidato" : candidato })

def perfil(request):
	return render(request, 'conoceme.html')

def compromisos(request):
	return render(request, 'compromisos.html')

def galerias(request):
	return render(request, 'galerias.html')

def galeria(request):
	return render(request, 'galeria01.html')

def noticias(request):
	return render(request, 'noticias.html')

def noticia(request):
	return render(request, 'noti01.html')

def videos(request):
	return render(request, 'videos.html')

def video(request):
	return render(request, 'video01.html')

