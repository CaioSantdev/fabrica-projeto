from django import forms
from piloto.models import Curso


class CursosForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Digite o nome do curso.'
    }))
    class Meta:
        model = Curso
        fields = ["nome",
                  "campus"]
        help_texts = {
            'campus': 'Selecione o campus onde o curso é ministrado.'
        }
        widgets = {
            'campus':forms.Select(attrs={
                "class":"form-control"
            })
        }
