"""Define padrões de URL para learningLogApp"""

from django.urls import path

# Importa o modúlo viws para a pasta do app "."
from . import views

# variavel reservada
app_name="learningLogApp"

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),

    # Assuntos
    path('assuntos/', views.assuntos, name='assuntos'),

    # Lista entradas por assunto
    path('assuntos/<int:assunto_id>/', views.assunto, name='assunto'),

     # Página de criação de Novos assuntos
    path('assuntos/novo_assunto/', views.novo_assunto, name='novo_assunto'),   

    # Página de ediçao de assuntos
    path('editar_assunto/<int:assunto_id>/', views.editar_assunto, name='editar_assunto'),  

    # Página de exclusão de assuntos
    path('excluir_assunto/<int:assunto_id>/', views.excluir_assunto, name='excluir_assunto'),  

     # Página de criação de Novas entradas
    path('nova_entrada/<int:assunto_id>/', views.nova_entrada, name='nova_entrada'),     

    # Página de ediçao de entradas
    path('editar_entrada/<int:entrada_id>/', views.editar_entrada, name='editar_entrada'),  

    # Página de exclusao de entradas
    path('excluir_entrada/<int:entrada_id>/', views.excluir_entrada, name='excluir_entrada'),
]
