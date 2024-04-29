from django.views import View
from piloto.models import Estudante
from piloto.forms import FiltroForm
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

class Listar(View):
    def get(self,request):
        todosEstudantes = Estudante.objects.all()
        form = FiltroForm()
        context = {
            'estudantes': todosEstudantes,
            'form': form
        }
        return render(request,'piloto/pages/Listar.html',context=context)