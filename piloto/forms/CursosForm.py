from django import forms
from piloto.models import Cursos


class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ["nomeCurso",
                  "campus"]