from django.shortcuts import render

from .models import Assunto
from .forms import AssuntoForm , EntradaForm

from django.http import HttpResponseRedirect
from django.urls import reverse

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
    contexto = {'assunto' : assunto, 'entradas' : entradas}
    return render(request, 'learningLogApp/assunto.html', contexto)

def novo_assunto(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = AssuntoForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = AssuntoForm(request.POST)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('learningLogApp:assuntos'))
    #atraves do contexto passa o forumario que recebeu a instancia da class AssuntoForm() de forms.py e usada com tag de template {{ form.as_p }}
    contexto = { 'form': form }
    return render(request, 'learningLogApp/novo_assunto.html', contexto)

def nova_entrada(request , assunto_id):
    """Adiciona uma nova entrada."""
    assunto = Assunto.objects.get(id = assunto_id)

    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = EntradaForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = EntradaForm(data = request.POST)
    
    if form.is_valid():
        nova_entrada = form.save(commit = False)
        nova_entrada.assunto = assunto
        nova_entrada.save()
        return HttpResponseRedirect(reverse('learningLogApp:assunto',
                                            args=[assunto_id]))
    #atraves do contexto passa o forumario que recebeu a instancia da class AssuntoForm() de forms.py e usada com tag de template {{ form.as_p }}
    contexto = { 'assunto' : assunto , 'form': form }
    return render(request, 'learningLogApp/nova_entrada.html', contexto)
   
