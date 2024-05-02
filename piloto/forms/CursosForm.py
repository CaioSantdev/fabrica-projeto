from django import forms
from piloto.models import Curso


class CursosForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nome",
                  "campus"]