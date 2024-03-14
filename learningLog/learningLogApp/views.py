from django.shortcuts import render
from .models import Assunto

def index(request):
    """A página inicial de Learning Log"""
    return render(request, 'learningLogApp/index.html')

def assuntos(request):
    """Página de assuntos"""
    assuntos = Assunto.objects.order_by('data_inicial')
    contexto = {'assuntos' : assuntos}
    return render(request, 'learningLogApp/assuntos.html', contexto)

def assunto(request, assunto_id):
    """Página de assuntos"""
    assunto = Assunto.objects.get(id=assunto_id)
    entradas = assunto.entrada_set.order_by('-data_inicial')
    contexto = {'assunto' : assunto, 'entradas  ' : entradas}
    return render(request, 'learningLogApp/assunto.html', contexto)


