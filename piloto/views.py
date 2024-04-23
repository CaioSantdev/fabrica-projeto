from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'global/index.html')
def cadastro(request):
    return render(request,'piloto/pages/blank.html')
def listar(request):
    return render(request,'piloto/pages/404.html')