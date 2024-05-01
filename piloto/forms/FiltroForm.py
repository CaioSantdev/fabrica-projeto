from django import forms
from piloto.models import Cursos, Campus


class FiltroForm(forms.ModelForm):
    nomeCurso = forms.ModelChoiceField(required=False,label="Nome do Curso",queryset=Cursos.objects.all(),empty_label="-----")
    # campus = forms.ModelChoiceField(queryset=Campus.objects.all(),empty_label=None)
    campus = forms.ModelChoiceField(required=False,queryset=Campus.objects.all(),empty_label="------")
    class Meta:
        model = Cursos
        fields = ["nomeCurso",
                  "campus"]