from django import forms
from .models import Assunto, Entrada

class AssuntoForm(forms.ModelForm):
    """
    Formulário para a criação e edição de objetos Assunto.
    
    Este formulário é associado ao modelo Assunto e permite ao usuário inserir ou modificar dados.
    Os campos 'texto' e 'public' são incluídos no formulário.
    
    Atributos:
    - model: Define o modelo ao qual o formulário está associado.
    - fields: Especifica quais campos do modelo devem ser incluídos no formulário.
    - labels: Fornece rótulos personalizados para os campos do formulário. O rótulo para 'texto' é deixado em branco
      para não exibir um rótulo acima do campo, enquanto 'public' é rotulado como 'Tornar públic' para clareza.
    """
    class Meta:
        model = Assunto
        fields = ['texto', 'public']
        labels = {'texto': '', 'public': 'Tornar públic'}

class EntradaForm(forms.ModelForm):
    """
    Formulário para a criação e edição de objetos Entrada.
    
    Este formulário é vinculado ao modelo Entrada e permite ao usuário inserir ou modificar dados de uma entrada específica.
    Somente o campo 'texto' é incluído no formulário.
    
    Atributos:
    - model: Especifica o modelo Entrada ao qual o formulário está associado.
    - fields: Indica que apenas o campo 'texto' deve ser incluído no formulário.
    - labels: Define um rótulo personalizado para o campo 'texto'. Neste caso, o rótulo é deixado em branco.
    - widgets: Permite definir widgets personalizados para um ou mais campos do formulário. Aqui, o widget para o campo 'texto'
      é configurado como um elemento Textarea com 80 colunas de largura, proporcionando uma área maior para a entrada de texto
      pelo usuário.
    """
    class Meta:
        model = Entrada
        fields = ['texto', 'status']
        labels = {'texto': ''}
        widgets = {
            'texto': forms.Textarea(attrs={'cols': 80}),
            'status': forms.HiddenInput(),  # Faz o campo status ser oculto
        }
