from django import forms
from piloto.models import Estudante

class EditForm(forms.ModelForm):
    nome = forms.CharField(label="Nome Estudante",widget=forms.TextInput(attrs={
        'readonly':True
    }))
    matricula = forms.CharField(label="Matricula",widget=forms.TextInput(attrs={
        'readonly':True
    }))
    class Meta:
        model = Estudante
        fields = ["nome","matricula","situacao"]