from django.views.generic import ListView
from piloto.models import Estudante
from piloto.forms import FiltroForm, EstudanteForm, EditForm
from django.shortcuts import render

class Listar(ListView):
    model = Estudante
    template_name = 'piloto/pages/Listar.html'
    context_object_name = 'estudantes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filterCampus = self.request.GET.get('campus', None)
        filterNomeCurso = self.request.GET.get('nomeCurso', None)
        # print(f'Nome: {filterNomeCurso} e Campus: {filterCampus}')
        
        print(f'Request: {self.request.GET}')
        
        if filterCampus:
            self.object_list = self.object_list.filter(cursoEstudante__campus__id=filterCampus)
        
        if filterNomeCurso:
            self.object_list = self.object_list.filter(cursoEstudante__id=filterNomeCurso)
            
        form = FiltroForm()
        formEstudante = EditForm()
        context = {
            "form": form,
            "estudanteForm": formEstudante,
            "estudantes": self.object_list
        }
        return context