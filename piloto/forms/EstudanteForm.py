from django import forms
from piloto.models import Estudante

class EstudanteForm(forms.ModelForm):
    cpfEstudante= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Somente Numeros',
        'maxlength':11
        }),
        label='CPF do Estudante',
        error_messages={'unique':"Esse CPF já foi cadastrado!"})
    situacao = forms.CharField(initial='1', widget=forms.HiddenInput())
    class Meta:
        model = Estudante
        fields = ["nome",
                  "cpfEstudante",
                  "dataAniversario",
                  "eImagem",
                  "curso",
                  "modoDeEntrada"]
        widgets = {
            "nome": forms.TextInput(attrs={
                'placeholder': 'Nome completo'
            }),
             "dataAniversario":forms.DateInput(attrs={'type':'date'}),
             "situacao": forms.Select(attrs={
                 "disabled":'disabled',
             }),
            'curso':forms.Select(attrs={
                "class":"form-control"
            }),
            'modoDeEntrada':forms.Select(attrs={
                "class":"form-control"
            })
        }