from django.shortcuts import render

def inicio(request):
	return render(request, 'index.html')

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

