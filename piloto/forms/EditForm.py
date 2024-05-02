from django import forms
from piloto.models import Estudante

class EditForm(forms.ModelForm):
    nomeEstudante = forms.CharField(label="Nome Estudante",widget=forms.TextInput(attrs={
        'readonly':True
    }))
    class Meta:
        model = Estudante
        fields = ["nomeEstudante","situacaoEstudante"]