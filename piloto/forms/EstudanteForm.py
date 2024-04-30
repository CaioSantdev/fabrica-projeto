from django import forms
from piloto.models import Estudante

class EstudanteForm(forms.ModelForm):
    cpfEstudante= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Somente Numeros',
        'maxlenght':11
        }),
        label='CPF do Estudante',
        error_messages={'unique':"Esse CPF já foi cadastrado!"})
    class Meta:
        model = Estudante
        fields = ["nomeEstudante",
                  "cpfEstudante",
                  "dataAniversario",
                  "eImagem",
                  "cursoEstudante",
                  "situacaoEstudante",
                  "modoDeEntrada"]
        widgets = {
            "nomeEstudante": forms.TextInput(attrs={
                'placeholder': 'Seu nome aqui'
            }),
             "dataAniversario":forms.DateInput(attrs={'type':'date'}),
        }