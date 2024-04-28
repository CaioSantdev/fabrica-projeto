from django import forms
from piloto.models import Estudante

class EstudanteForm(forms.ModelForm):
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
            "cpfEstudante":forms.TextInput(attrs={
                'placeholder': 'Apenas Numeros'
            }),
             "dataAniversario":forms.DateInput(attrs={'type':'date'}),
        }
        error_messages = {
            'cpfEstudante':{
                'unique': "Ja existe um estudante com este CPF"
            }
        }