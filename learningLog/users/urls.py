"""Define padrões de URL para users"""

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

# Importa o modúlo viws para a pasta do app "."
from . import views

app_name = "users"

urlpatterns = [
    path('login/' , LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='learningLogApp:index'), name='logout'),
    path('registrar/', views.registrar, name='registrar'),

]
