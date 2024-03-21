from django.db import models
from django.contrib.auth.models import User

class Assunto(models.Model):
    """ Um assunto sobre o qual o usuários está aprendendo """
    texto = models.CharField(max_length = 200)
    data_inicial = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Chave estrangeira com usuario
    public = models.BooleanField(default=False)

    def __str__(self):
        """ Devolve uma representação em string do modelo """
        return self.texto

class Entrada(models.Model):
    """ Entrada específica sobre determinado assunto """
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE) # Chave estrangeira com assunto
    texto = models.TextField()
    data_inicial = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Devolve uma representação em string do modelo """
        if len(self.texto) >= 50:
            return self.texto[:50] + " ..."
        return self.texto
        