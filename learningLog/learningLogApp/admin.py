from django.contrib import admin

from learningLogApp.models import Assunto, Entrada

# Registrando os models no site de administraçãoc
admin.site.register(Assunto)
admin.site.register(Entrada)