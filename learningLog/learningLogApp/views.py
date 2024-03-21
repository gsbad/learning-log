from django.shortcuts import render, get_object_or_404

from .models import Assunto, Entrada
from .forms import AssuntoForm , EntradaForm

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from django.contrib.auth.decorators import login_required

# Django Rest Framework imports
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import AssuntoSerializer, EntradaSerializer

class AssuntoViewSet(viewsets.ModelViewSet):
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'texto', 'data_inicial', 'owner']
    

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'assunto', 'texto', 'data_inicial']

def index(request):
    """A página inicial de Learning Log"""
    return render(request, 'learningLogApp/index.html')

#@login_required
def assuntos(request):
    """Página de assuntos"""
    if request.user.is_authenticated:
        assuntos = Assunto.objects.filter(owner=request.user) | Assunto.objects.filter(public=True)
    else:
        assuntos = Assunto.objects.filter(public=True)
    contexto = {'assuntos': assuntos}   
    """A página inicial de Learning Log"""
    return render(request, 'learningLogApp/assuntos.html', contexto)
    

#@login_required
def assunto(request, assunto_id):
    """Página de assuntos"""
    assunto = get_object_or_404(Assunto, id=assunto_id)

    # Se o assunto for privado e o usuário não for o proprietário, levanta 404.
    if not assunto.public and assunto.owner != request.user:
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
def editar_assunto(request, assunto_id):
    assunto = get_object_or_404(Assunto, id=assunto_id)

    if request.method != 'POST':
        # Preenche o formulário com a instância atual.
        form = AssuntoForm(instance=assunto)
    else:
        # POST, processar dados do formulário.
        form = AssuntoForm(instance=assunto, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learningLogApp:assunto', id=assunto_id))

    context = {'assunto': assunto, 'form': form}
    return render(request, 'learningLogApp/editar_assunto.html', context)

@login_required
def nova_entrada(request , assunto_id):
    """Adiciona uma nova entrada."""
    assunto = get_object_or_404(Assunto,id = assunto_id)
    
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