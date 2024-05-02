from django import forms
from piloto.models import Curso, Campus


class FiltroForm(forms.ModelForm):
    nome = forms.ModelChoiceField(required=False,label="Nome do Curso",queryset=Curso.objects.all(),empty_label="-----")
    # campus = forms.ModelChoiceField(queryset=Campus.objects.all(),empty_label=None)
    campus = forms.ModelChoiceField(required=False,queryset=Campus.objects.all(),empty_label="------")
    def __init__(self,*args, **kwargs):
        super(FiltroForm,self).__init__(*args, **kwargs)
        self.fields["nome"].widget.attrs["id"] = "id_nomeCurso"
    class Meta:
        model = Curso
        fields = ["nome",
                  "campus"]