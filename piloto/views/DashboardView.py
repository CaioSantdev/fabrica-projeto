from django.views import View
from piloto.models import Estudante,Campus,Curso
from django.shortcuts import render

import json
class DashboardView(View):
    def get(self, request):
        # <-------TODOS CURSOS E ESTUDANTES------------>
        estudantes = Estudante.objects.all().count()
        cursos = Curso.objects.all().count()
        campusQtd = Campus.objects.all().count()
        # <--------------------------------------------->
        
        # <-------TODOS ESTUDANTES POR CAMPUS------------>
        campi = Campus.objects.all()
        ## annotate aggregation 
        estudantesPorCampus = {}
        for campus in campi:
            cursoCampus = Curso.objects.filter(campus=campus)
            estudantesCampus = Estudante.objects.filter(curso__in=cursoCampus)
            estudantesCampusQtd = estudantesCampus.count()
            estudantesPorCampus[campus.nome] = estudantesCampusQtd
        nomeDoCampus = list(estudantesPorCampus.keys())
        quantidadeEstudanteCampus = list(estudantesPorCampus.values())
        
        # <----------------------------------------------->
        
        # <-------TODOS ESTUDANTES POR CURSOS------------> 
        estudantesPorCurso = {}
        todosCursos = Curso.objects.all()
        for curso in todosCursos:
            estudantesPorCurso[curso.nome] = Estudante.objects.filter(curso=curso).count()
        nomeDoCurso = list(estudantesPorCurso.keys())
        quantidadeEstudanteCurso = list(estudantesPorCurso.values())
        # <--------------------------------------------->

        dadosDash = {}
        dadosDash['qtdAlunos'] =  5
        dadosDash['qtdCampus'] = 8
        

        context = {
            'nomeDoCampus': nomeDoCampus,
            'quantidadeEstudanteCampus': quantidadeEstudanteCampus,
            'estudantesQuantidade':estudantes,
            'cursosQuantidade':cursos,
            'campusQuantidade':campusQtd,
            'nomeDoCurso': nomeDoCurso,
            'quantidadeEstudanteCurso': quantidadeEstudanteCurso,
            # 'dados': dadosDash
        }
        return render(request, 'piloto/pages/Dashboard.html', context=context)
    
    
    def das(self, qs):
        
        pass
        
    