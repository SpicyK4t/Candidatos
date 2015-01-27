from django.shortcuts import render

def inicio(request):
	return render(request, 'index.html')

def inicio_candidato(request):
	return render(request, 'home.html')

def compromisos(request):
	return render(request, 'compromisos.html')
