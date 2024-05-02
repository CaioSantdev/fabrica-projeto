from django import forms
from piloto.models import Estudante

class EstudanteForm(forms.ModelForm):
    cpfEstudante= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Somente Numeros',
        'maxlength':11
        }),
        label='CPF do Estudante',
        error_messages={'unique':"Esse CPF já foi cadastrado!"})
    class Meta:
        model = Estudante
        fields = ["nome",
                  "cpfEstudante",
                  "dataAniversario",
                  "eImagem",
                  "curso",
                  "situacao",
                  "modoDeEntrada"]
        widgets = {
            "nome": forms.TextInput(attrs={
                'placeholder': 'Seu nome aqui'
            }),
             "dataAniversario":forms.DateInput(attrs={'type':'date'}),
        }