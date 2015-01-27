from django.shortcuts import render
from home.models import Candidato

def inicio(request):
	alcaldes = Candidato.objects.all().filter(tipo_candidato = 1)
	d_locales = Candidato.objects.all().filter(tipo_candidato = 2)
	d_federales = Candidato.objects.all().filter(tipo_candidato = 3)

	return render(request, 'index.html', { "alcaldes" : alcaldes, "d_locales" : d_locales, "d_federales" : d_federales })

def inicio2(request):
	return render(request, 'index0.html')

def candidato(request):
	return render(request, 'home.html')

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

