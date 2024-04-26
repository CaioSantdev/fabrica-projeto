from django.views import View
from piloto.forms import EstudanteForm
from piloto.models import Estudante,Campus,Cursos
from django.shortcuts import render

class Dashboard(View):
    def get(self,request):
        print("ESTOU USANDO CBV")
        estudantes = Estudante.objects.all()
        cursos = Cursos.objects.all()
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
        
    