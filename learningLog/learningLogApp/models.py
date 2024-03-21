from django.db import models
from django.contrib.auth.models import User

class Assunto(models.Model):
    """
    Modelo para representar um assunto que o usuário deseja aprender ou monitorar.
    
    Atributos:
    - texto: Campo de texto para descrever o assunto, limitado a 200 caracteres.
    - data_inicial: Campo de data e hora que armazena automaticamente a data e hora de criação do assunto.
    - owner: Campo de chave estrangeira que associa o assunto a um usuário específico. Isso permite que o aplicativo
      identifique quem criou o assunto e implemente a lógica de permissão apropriada.
    - public: Campo booleano que indica se o assunto é público (acessível por todos os usuários) ou privado
      (visível apenas para o usuário que o criou). Por padrão, os assuntos são privados.
      
    Métodos:
    - __str__: Método especial que retorna a representação em string do assunto, facilitando a identificação dos assuntos
      quando eles são listados ou referenciados em outras partes do aplicativo.
    """
    texto = models.CharField(max_length=200)
    data_inicial = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

class Entrada(models.Model):
    """
    Modelo para representar uma entrada específica relacionada a um assunto.
    
    Atributos:
    - assunto: Campo de chave estrangeira que associa a entrada a um assunto específico. Isso estabelece uma relação
      muitos-para-um entre entradas e assuntos, permitindo que múltiplas entradas sejam relacionadas a um único assunto.
    - texto: Campo de texto para o conteúdo da entrada. Não há limite de caracteres, permitindo entradas extensas.
    - data_inicial: Campo de data e hora que armazena automaticamente a data e hora de criação da entrada.
      
    Métodos:
    - __str__: Método especial que retorna uma representação em string da entrada. Para facilitar a visualização em listas
      ou resumos, se o texto da entrada tiver 50 caracteres ou mais, ele será truncado para os primeiros 50 caracteres seguidos
      de reticências. Isso oferece uma pré-visualização da entrada sem sobrecarregar a interface com textos longos.
    """
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE)
    texto = models.TextField()
    data_inicial = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.texto) >= 50:
            return self.texto[:50] + " ..."
        return self.texto
