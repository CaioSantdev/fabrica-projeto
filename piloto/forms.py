from django import forms
from . models import *

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
