from rest_framework import serializers
from .models import Assunto, Entrada

class AssuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assunto
        fields = ['id', 'texto', 'data_inicial', 'owner']

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = ['id', 'assunto', 'texto', 'data_inicial']