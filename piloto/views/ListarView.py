from django.views.generic import ListView
from piloto.models import Estudante
from piloto.forms import FiltroForm, EstudanteForm, EditForm
from django.shortcuts import render

class ListarView(ListView):
    model = Estudante
    template_name = 'piloto/pages/Listar.html'
    context_object_name = 'estudantes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filterCampus = self.request.GET.get('campus', None)
        filterNomeCurso = self.request.GET.get('nome', None)
        filterSituacao = self.request.GET.get('situacao', None)
        print(f'Nome: {filterNomeCurso} e Campus: {filterCampus}, situacao: {filterSituacao}')
        
        print(f'Request: {self.request.GET}')
        
        if filterCampus:
            self.object_list = self.object_list.filter(curso__campus__id=filterCampus)
        
        if filterNomeCurso:
            self.object_list = self.object_list.filter(curso__id=filterNomeCurso)
        
        if filterSituacao:
            self.object_list = self.object_list.filter(situacao=filterSituacao)
            
        form = FiltroForm()
        formEstudante = EditForm()
        totalEstudantesFiltro = self.object_list.count()
        context = {
            "form": form,
            "estudanteForm": formEstudante,
            "estudantes": self.object_list,
            "totalEstudantes": totalEstudantesFiltro
        }
        return context