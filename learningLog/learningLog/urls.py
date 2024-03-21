from django.contrib import admin
from django.urls import path, include

# Importa o módulo views do app 'learningLogApp'.
from learningLogApp import views

# Importa o DefaultRouter do Django Rest Framework, que é utilizado para criar rotas para a API de forma automática.
from rest_framework.routers import DefaultRouter

# Cria uma instância do DefaultRouter.
router = DefaultRouter()
# Registra o viewset AssuntoViewSet com a rota 'assuntos'. Isso cria todas as URLs necessárias para operações CRUD no modelo Assunto via API.
router.register('assuntos', views.AssuntoViewSet, basename='assunto')
# Registra o viewset EntradaViewSet com a rota 'entradas'. Isso cria todas as URLs necessárias para operações CRUD no modelo Entrada via API.
router.register('entradas', views.EntradaViewSet, basename='entrada')

urlpatterns = [
    # Rota para o Django admin. O Django fornece uma interface de administração pronta para gerenciar os modelos do seu projeto.
    path('admin/', admin.site.urls),
    
    # Rota base para a API, que inclui todas as rotas criadas automaticamente pelo router do DRF.
    # Por exemplo, esta configuração torna a API acessível em 'http://<dominio>/api/assuntos/' e 'http://<dominio>/api/entradas/'.
    path('api/', include(router.urls)),
    
    # Inclui as URLs definidas no arquivo urls.py do app 'users'. Geralmente, estas seriam rotas para autenticação de usuários, como registro, login e logout.
    path('users/', include('users.urls')),
    
    # Inclui as URLs definidas no arquivo urls.py do app 'learningLogApp'. Este app é o núcleo do projeto, e suas URLs podem incluir rotas para visualizar, criar, editar e deletar assuntos e entradas.
    path('', include('learningLogApp.urls')),
]
