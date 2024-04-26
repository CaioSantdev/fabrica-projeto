from django.shortcuts import render
from . forms import *

# Create your views here.

def home(request):
    return render(request,'global/index.html')
def cadastro(request):
    if request.method == "GET":
        form = EstudanteForm()
        context = {
            'form':form
        }
        return render(request,'piloto/pages/Cadastro.html',context=context)
    else:
        form = EstudanteForm(request.POST,request.FILES)

        if form.is_valid():
            print(f'Request: {request.POST}')
            # student = form.save(commit=False)
            # student.image = request.FILES['image']
            # student.save()
            form.save()
            
        else:
            print(form.errors)

        context = {
            'form':form
        }
        return render(request,'piloto/pages/Cadastro.html',context=context)


def listar(request):
    alunos = Estudante.objects.all()
    return render(request,'piloto/pages/Listar.html',{'alunos':alunos})

def cursos(request):
    if request.method == "GET":
        form = CursosForm()
        context = {
            'form':form
        }
        return render(request,'piloto/pages/Cursos.html',context=context)
    else:
        form = CursosForm(request.POST,request.FILES)

        if form.is_valid():
            print(f'Request: {request.POST}')
            # student = form.save(commit=False)
            # student.image = request.FILES['image']
            # student.save()
            form.save()
            
        else:
            print(form.errors)

        context = {
            'form':form
        }
        return render(request,'piloto/pages/Cursos.html',context=context)
def campus(request):
    if request.method == "GET":
        form = CampusForm()
        context = {
            'form':form
        }
        return render(request,'piloto/pages/Campus.html',context=context)
    else:
        form = CampusForm(request.POST,request.FILES)

        if form.is_valid():
            print(f'Request: {request.POST}')
            # student = form.save(commit=False)
            # student.image = request.FILES['image']
            # student.save()
            form.save()
            
        else:
            print(form.errors)

        context = {
            'form':form
        }
        return render(request,'piloto/pages/Campus.html',context=context)