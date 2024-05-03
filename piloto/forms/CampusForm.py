from django import forms
from piloto.models import Campus

class CampusForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Digite o nome do campus.'
    }))
    class Meta:
        model = Campus
        fields = ["nome",]