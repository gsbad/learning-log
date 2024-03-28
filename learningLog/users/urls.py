"""Define padrões de URL para users"""

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path

# Importa o modúlo viws para a pasta do app "."
from . import views

app_name = "users"

urlpatterns = [
    path('login/' , LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='learningLogApp:index'), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('registrar/', views.registrar, name='registrar'), 
    path('editar/', views.editar_usuario, name='editar_usuario'),   
    path('mudar_senha/', PasswordChangeView.as_view(success_url='learningLogApp:index'), name='mudar_senha'),   

]
