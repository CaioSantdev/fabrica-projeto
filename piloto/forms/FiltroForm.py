from django import forms
from piloto.models import Cursos, Campus


class FiltroForm(forms.ModelForm):
    nomeCurso = forms.ModelChoiceField(queryset=Cursos.objects.all(),empty_label=None)
    
    class Meta:
        model = Cursos
        fields = ["nomeCurso",
                  "campus"]