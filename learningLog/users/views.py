from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import EditarUsuarioForm

def registrar(request):
    """Faz o cadastro de um novo usuário."""
    if request.method != 'POST':
        # Exibe o formulário de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)
    if form.is_valid():
        new_user = form.save()
        # Faz login do usuário e o redireciona para a página inicial
        authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
        login(request, authenticated_user)
        return HttpResponseRedirect(reverse('learningLogApp:index'))
    context = {'form': form}
    return render(request, 'users/registrar.html', context)

@login_required
def perfil(request):
    return render(request, 'users/perfil.html')

@login_required
def editar_usuario(request):
    if request.method == 'POST':
        form = EditarUsuarioForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:perfil')  # Redirecione para a view de perfil do usuário após sucesso
    else:
        form = EditarUsuarioForm(instance=request.user)

    return render(request, 'users/editar_usuario.html', {'form': form})

@login_required
def mudar_senha(request):
    if request.method == 'POST':
        print(request.user)
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante para não deslogar o usuário após a mudança de senha
            return HttpResponseRedirect(reverse('learningLogApp:index'))
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/mudar_senha.html', {'form': form})
