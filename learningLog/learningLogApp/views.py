from django.shortcuts import render, get_object_or_404

from .models import Assunto, Entrada
from .forms import AssuntoForm , EntradaForm

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from django.contrib.auth.decorators import login_required


def index(request):
    """A página inicial de Learning Log"""
    return render(request, 'learningLogApp/index.html')

@login_required
def assuntos(request):
    """Página de assuntos"""
    assuntos = Assunto.objects.filter(owner=request.user).order_by('data_inicial')
    contexto = {'assuntos' : assuntos}
    return render(request, 'learningLogApp/assuntos.html', contexto)

@login_required
def assunto(request, assunto_id):
    """Página de assuntos"""
    assunto = get_object_or_404(Assunto, id=assunto_id)
    # Garante que o assunto pertence ao usuario atual
    if assunto.owner != request.user:
        raise Http404
    entradas = assunto.entrada_set.order_by('-data_inicial')
    contexto = {'assunto' : assunto, 'entradas' : entradas}
    return render(request, 'learningLogApp/assunto.html', contexto)

@login_required
def novo_assunto(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = AssuntoForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = AssuntoForm(request.POST)
    
    if form.is_valid():
        novo_assunto = form.save(commit = False)
        novo_assunto.owner = request.user
        novo_assunto.save()
        return HttpResponseRedirect(reverse('learningLogApp:assuntos'))
    #atraves do contexto passa o formulario que recebeu a instancia da class AssuntoForm() de forms.py e usada com tag de template {{ form.as_p }}
    contexto = { 'form': form }
    return render(request, 'learningLogApp/novo_assunto.html', contexto)

@login_required
def nova_entrada(request , assunto_id):
    """Adiciona uma nova entrada."""
    assunto = Assunto.objects.get(id = assunto_id)
    
    owner_assunto = assunto.owner
    owner_request = request.user
    # Garante que o assunto pertence ao usuario atual
    if owner_assunto != owner_request:
        raise Http404     

    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = EntradaForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = EntradaForm(data = request.POST)
    
    if form.is_valid():
        # proteçao de novas entradas            
        nova_entrada.owner = request.user       
        nova_entrada = form.save(commit = False)
        nova_entrada.assunto = assunto           
        nova_entrada.save()
        return HttpResponseRedirect(reverse('learningLogApp:assunto',
                                            args=[assunto_id]))
    contexto = { 'assunto' : assunto , 'form': form }
    return render(request, 'learningLogApp/nova_entrada.html', contexto)

@login_required
def editar_entrada(request , entrada_id):
    """Editar uma entrada."""
    entrada = get_object_or_404(Entrada, id = entrada_id)
    assunto = entrada.assunto
     # Garante que o assunto pertence ao usuario atual
    if assunto.owner != request.user:
        raise Http404   
    if request.method != 'POST':
        # Requisição inicial; Preenche previamente o form com entrada atual
        form = EntradaForm(instance = entrada)
    else:
        # Dados de POST submetidos; processa os dados
        form = EntradaForm(instance = entrada, data = request.POST)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('learningLogApp:assunto',
                                            args=[assunto.id]))
    contexto = { 'entrada' : entrada , 'assunto' : assunto , 'form': form }
    return render(request, 'learningLogApp/editar_entrada.html', contexto)