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
        
class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ["name",
                  "campus"]
        
class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ["name",]