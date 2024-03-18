from django.contrib import admin
from django.urls import path, include

# Importa o modúlo viws para a pasta do app "."
from learningLogApp import views

# Modelo do DRF
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('assuntos', views.AssuntoViewSet)
router.register('entradas', views.EntradaViewSet, basename='entrada')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Router do DRF
    path('api/', include(router.urls)),

    path('users/', include('users.urls')),
    path('', include('learningLogApp.urls')),
]
