from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from piloto.models import Estudante
from piloto.forms import FiltroForm, EstudanteForm, EditForm
from django.shortcuts import render
from django.core.paginator import Paginator

class ListarView(ListView):
    model = Estudante
    template_name = 'piloto/pages/Listar.html'
    paginate_by = 20
    
    
    def get_queryset(self):
        qsEstudante = super().get_queryset().order_by("nome")
        filterCampus = self.request.GET.get('campus', None)
        filterNomeCurso = self.request.GET.get('nome', None)
        filterSituacao = self.request.GET.get('situacao', None)
        filterNomeCpf = self.request.GET.get('filtro_nome_cpf', None)
        
        print(f'Nome: {filterNomeCurso} e Campus: {filterCampus}, situacao: {filterSituacao}')
        if filterCampus:
            qsEstudante = qsEstudante.filter(curso__campus__id=filterCampus)
        
        if filterNomeCurso:
            qsEstudante = qsEstudante.filter(curso__id=filterNomeCurso)
        
        if filterSituacao:
            qsEstudante = qsEstudante.filter(situacao=filterSituacao)   
     
        if filterNomeCpf:
            qsEstudante = qsEstudante.filter(cpfEstudante__icontains=filterNomeCpf) or qsEstudante.filter(nome__icontains=filterNomeCpf) 
        print("1", qsEstudante)
        return qsEstudante
    
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(
                queryset, page_size
            )
            context = {
                "paginator": paginator,
                "page_obj": page,
                "is_paginated": is_paginated,
                "object_list": queryset,
            }
            
        else:
            context = {
                "paginator": None,
                "page_obj": None,
                "is_paginated": False,
                "object_list": queryset,
            }
        print(f'Request: {self.request.GET}')
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
            
        form = FiltroForm()
        formEstudante = EditForm()
        totalEstudantesFiltro = self.object_list.count()
        context = {
            "form": form,
            "estudanteForm": formEstudante,
            "totalEstudantes": totalEstudantesFiltro
        }
        return super().get_context_data(**context)
