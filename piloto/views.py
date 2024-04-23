from django.shortcuts import render
from . forms import *

# Create your views here.

def home(request):
    return render(request,'global/index.html')
def cadastro(request):
    if request.method == "GET":
        form = StudentForm()
        context = {
            'form':form
        }
        return render(request,'piloto/pages/Cadastro.html',context=context)
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            form = StudentForm()
        
        context = {
            'form':form
        }
        return render(request,'piloto/pages/Cadastro.html',context=context)


def listar(request):
    return render(request,'piloto/pages/404.html')