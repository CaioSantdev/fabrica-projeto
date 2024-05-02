from django import forms
from piloto.models import Campus

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ["nome",]