from django.shortcuts import render
from piloto.models import Estudante,Campus,Cursos
from piloto.forms import EstudanteForm, CursosForm,CampusForm

# Create your views here.

def home(request):
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

def listar(request):
    alunos = Estudante.objects.all()
    
    context = {
        'alunos':alunos
    }
    return render(request,'piloto/pages/Listar.html',context=context)

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