from django.db import models

class Assunto(models.Model):
    """ Um assunto sobre o qual o usuários está aprendendo """
    texto = models.CharField(max_length = 200)
    data_inicial = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Devolve uma representação em string do modelo """
        return self.texto

class Entrada(models.Model):
    """ Entrada específica sobre determinado assunto """
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE) # Chave estrangeira
    texto = models.TextField()
    data_inicial = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Devolve uma representação em string do modelo """
        return self.texto[:50] + "..."