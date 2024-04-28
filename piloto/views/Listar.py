from django.views import View
from piloto.models import Estudante
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

class Listar(View):
    def get(self,request):
        todosEstudantes = Estudante.objects.all()
        context = {
            'estudantes': todosEstudantes
        }
        return render(request,'piloto/pages/Listar.html',context=context)