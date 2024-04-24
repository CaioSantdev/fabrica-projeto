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
    return render(request,'piloto/pages/404.html')