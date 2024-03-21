from rest_framework import serializers
from .models import Assunto, Entrada

class AssuntoSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Assunto.
    
    A classe Meta dentro do serializador define especificações sobre como o serializador deve se comportar. 
    Isso inclui indicar qual modelo o serializador deve usar e quais campos do modelo devem ser incluídos na serialização.
    
    - model: Define que o serializador é para o modelo Assunto.
    - fields: Lista de campos do modelo Assunto que serão incluídos na serialização. Isso inclui 'id', 'texto',
              'data_inicial' e 'owner', proporcionando um conjunto completo de informações do assunto que pode
              ser usado em APIs para exibição ou edição de assuntos.
    """
    class Meta:
        model = Assunto
        fields = ['id', 'texto', 'data_inicial', 'owner']

class EntradaSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Entrada.
    
    Assim como o serializador AssuntoSerializer, este define um modelo específico e campos a serem incluídos.
    A inclusão do campo 'assunto' permite que a serialização das entradas inclua a relação com o assunto ao qual pertencem,
    facilitando a representação de relações entre dados em APIs.
    
    - model: Indica que o serializador é para o modelo Entrada.
    - fields: Lista os campos 'id', 'assunto', 'texto' e 'data_inicial', permitindo que entradas específicas
              sejam facilmente acessadas, criadas ou modificadas via API.
    """
    class Meta:
        model = Entrada
        fields = ['id', 'assunto', 'texto', 'data_inicial']
