from django.views import View
from piloto.models import Estudante,Campus,Curso
from django.shortcuts import render

class DashboardView(View):
    def get(self,request):
        estudantes = Estudante.objects.all()
        cursos = Curso.objects.all()
        campus = Campus.objects.all()
        
        qtdEstudantes = estudantes.count()
        qtdCursos = cursos.count()
        qtdCampus = campus.count()
        
        context = {
            'estudantes':qtdEstudantes,
            'cursos':qtdCursos,
            'campus':qtdCampus
        }
        return render(request,'piloto/pages/Dashboard.html',context=context)
        
    