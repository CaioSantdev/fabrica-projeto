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