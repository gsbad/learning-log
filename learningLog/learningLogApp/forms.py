from django import forms

from .models import Assunto, Entrada

class AssuntoForm(forms.ModelForm):
    class Meta:
        model  = Assunto
        fields = ['texto']
        labels = {'texto' : 'Título'}

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['texto']
        labels = {'texto': 'Título'}
        widgets ={'texto': forms.Textarea(attrs={'cols': 80})}