from django import forms

from .models import Assunto

class AssuntoForm(forms.ModelForm):
    class Meta:
        model  = Assunto
        fields = ['texto']
        labels = {'texto' : 'Título'}