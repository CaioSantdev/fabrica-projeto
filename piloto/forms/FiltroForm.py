from django import forms
from piloto.models import Curso, Campus, Estudante


class FiltroForm(forms.ModelForm):
    SITUACAO = {
    "":"------",
    1: "Vinculado",
    2: "Formado",
    3: "Jubilado",
    4: "Evadido",
    5: "Desvinculado",
    }
    filtro_nome_cpf = forms.CharField(required=False, label="Nome ou CPF", widget=forms.TextInput(attrs={
        'class': 'form-control ml-20'}))
    nome = forms.ModelChoiceField(required=False,label="Nome do Curso",queryset=Curso.objects.all(),empty_label="-----")
    campus = forms.ModelChoiceField(required=False,queryset=Campus.objects.all(),empty_label="------")  
    situacao = forms.ChoiceField(required=False, choices=SITUACAO, label="Situação do Estudante")

    
    def __init__(self,*args, **kwargs):
        super(FiltroForm,self).__init__(*args, **kwargs)
        self.fields["nome"].widget.attrs["id"] = "id_nomeCurso"
        self.fields["situacao"].widget.attrs["id"] = "id_situacaoEstudante"
        
        self.fields["nome"].widget.attrs["class"] = "form-control ml-20"
        self.fields["campus"].widget.attrs["class"] = "form-control ml-20"
        self.fields["situacao"].widget.attrs["class"] = "form-control ml-20"
    class Meta:
        model = Curso
        fields = ["nome","campus"]