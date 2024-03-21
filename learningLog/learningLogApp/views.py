# Importações necessárias para views, models e forms
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Assunto, Entrada, User
from .forms import AssuntoForm, EntradaForm

# Importações do Django Rest Framework para criação de APIs
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import AssuntoSerializer, EntradaSerializer

# ViewSets do Django Rest Framework para os modelos Assunto e Entrada
class AssuntoViewSet(viewsets.ModelViewSet):
    """
    Fornece as ações de listagem, criação, atualização e exclusão para o modelo Assunto.
    Utiliza DjangoFilterBackend para filtrar os assuntos com base em determinados campos.
    """
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'texto', 'data_inicial', 'owner']
    
class EntradaViewSet(viewsets.ModelViewSet):
    """
    Fornece as ações de listagem, criação, atualização e exclusão para o modelo Entrada.
    Utiliza DjangoFilterBackend para filtrar as entradas com base em determinados campos.
    """
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'assunto', 'texto', 'data_inicial']

# View para a página inicial
def index(request):
    """
    Exibe a página inicial do aplicativo.
    Lista os últimos assuntos públicos e usuários cadastrados, ambos paginados.
    """
    # Paginação para os últimos assuntos públicos
    assuntos_publicos_list = Assunto.objects.filter(public=True).order_by('-data_inicial')
    paginator_assuntos_publicos = Paginator(assuntos_publicos_list, 5)
    page_number_assuntos = request.GET.get('page_assuntos')
    page_obj_assuntos = paginator_assuntos_publicos.get_page(page_number_assuntos)

    # Paginação para os usuários cadastrados
    usuarios_list = User.objects.all().order_by('-date_joined')
    paginator_usuarios = Paginator(usuarios_list, 5)
    page_number_usuarios = request.GET.get('page_usuarios')
    page_obj_usuarios = paginator_usuarios.get_page(page_number_usuarios)

    # Combina os objetos de página no contexto para renderização
    context = {
        'page_obj_assuntos': page_obj_assuntos,
        'page_obj_usuarios': page_obj_usuarios,
    }

    return render(request, 'learningLogApp/index.html', context)


def assuntos(request):
    """
    Exibe uma lista de assuntos. Para usuários autenticados, mostra seus assuntos e assuntos públicos.
    Para usuários não autenticados, mostra apenas assuntos públicos.
    """
    if request.user.is_authenticated:
        assuntos = Assunto.objects.filter(owner=request.user) | Assunto.objects.filter(public=True)
    else:
        assuntos = Assunto.objects.filter(public=True)
    contexto = {'assuntos': assuntos}
    return render(request, 'learningLogApp/assuntos.html', contexto)


def assunto(request, assunto_id):
    """
    Exibe detalhes de um assunto específico, incluindo suas entradas associadas.
    Verifica se o assunto é público ou se pertence ao usuário antes de exibir.
    """
    assunto = get_object_or_404(Assunto, id=assunto_id)
    if not assunto.public and assunto.owner != request.user:
        raise Http404
    entradas = assunto.entrada_set.order_by('-data_inicial')
    contexto = {'assunto': assunto, 'entradas': entradas}
    return render(request, 'learningLogApp/assunto.html', contexto)

# Seguem as demais views para manipulação de assuntos e entradas, aplicando lógica similar
# com verificações de propriedade e permissões, tratamento de formulários e redirecionamentos.

@login_required
def novo_assunto(request):
    """
    Permite ao usuário logado criar um novo assunto.
    Utiliza o método POST para submissão do formulário. Um formulário em branco é exibido inicialmente.
    """
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco.
        form = AssuntoForm()
    else:
        # Dados POST submetidos; processa os dados.
        form = AssuntoForm(request.POST)
        if form.is_valid():
            novo_assunto = form.save(commit=False)
            novo_assunto.owner = request.user  # Atribui o assunto ao usuário atual.
            novo_assunto.save()
            return HttpResponseRedirect(reverse('learningLogApp:assuntos'))

    contexto = {'form': form}
    return render(request, 'learningLogApp/novo_assunto.html', contexto)

@login_required
def editar_assunto(request, assunto_id):
    """
    Permite ao usuário editar um assunto existente.
    Verifica se o assunto pertence ao usuário antes de permitir a edição.
    """
    assunto = get_object_or_404(Assunto, id=assunto_id)
    if assunto.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = AssuntoForm(instance=assunto)  # Preenche o formulário com o assunto atual.
    else:
        form = AssuntoForm(instance=assunto, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learningLogApp:assunto', args=[assunto.id]))

    contexto = {'assunto': assunto, 'form': form}
    return render(request, 'learningLogApp/editar_assunto.html', contexto)

@login_required
def excluir_assunto(request, assunto_id):
    assunto = get_object_or_404(Assunto, id=assunto_id)
    
    if assunto.owner != request.user:
        raise Http404
    
    assunto.delete()
    return HttpResponseRedirect(reverse('learningLogApp:assuntos'))


@login_required
def nova_entrada(request, assunto_id):
    """
    Permite ao usuário adicionar uma nova entrada para um assunto específico.
    Garante que o assunto pertence ao usuário antes de permitir a adição da entrada.
    """
    assunto = get_object_or_404(Assunto, id=assunto_id)
    if assunto.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntradaForm()  # Formulário em branco inicialmente.
    else:
        form = EntradaForm(data=request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.assunto = assunto  # Associa a entrada ao assunto correto.
            nova_entrada.save()
            return HttpResponseRedirect(reverse('learningLogApp:assunto', args=[assunto_id]))

    contexto = {'assunto': assunto, 'form': form}
    return render(request, 'learningLogApp/nova_entrada.html', contexto)

@login_required
def editar_entrada(request, entrada_id):
    """
    Permite ao usuário editar uma entrada existente.
    Verifica se a entrada pertence ao usuário antes de permitir a edição.
    """
    entrada = get_object_or_404(Entrada, id=entrada_id)
    assunto = entrada.assunto
    if assunto.owner != request.user:
        raise Http404

    if request.method != 'POST':  
        form = EntradaForm(instance=entrada)  # Preenche o formulário com a entrada atual.
        
    else:
        form = EntradaForm(instance=entrada, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learningLogApp:assunto', args=[assunto.id]))        

    contexto = {'entrada': entrada, 'assunto': assunto, 'form': form}
    return render(request, 'learningLogApp/editar_entrada.html', contexto)

@login_required
def excluir_entrada(request, entrada_id):
    """
    Permite ao usuário excluir uma entrada existente.
    Verifica se a entrada pertence ao usuário antes de proceder com a exclusão.
    """
    entrada = get_object_or_404(Entrada, id=entrada_id)
    if entrada.assunto.owner != request.user:
        raise Http404

    assunto_id = entrada.assunto.id
    entrada.delete()  # Exclui a entrada.
    return HttpResponseRedirect(reverse('learningLogApp:assunto', args=[assunto_id]))
