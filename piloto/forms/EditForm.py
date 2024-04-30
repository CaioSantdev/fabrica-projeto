from django import forms
from piloto.models import Estudante

class EditForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ["nomeEstudante","situacaoEstudante"]