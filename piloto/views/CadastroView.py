from django.views import View
from piloto.forms import EstudanteForm
from django.contrib import messages
from django.shortcuts import render,redirect

class CadastroView(View):
    def get(self,request):
        form = EstudanteForm()
        context = {
            "form": form
        }
        return render(request,'piloto/pages/Cadastro.html',context=context)

    def post(self,request):
        form = EstudanteForm(request.POST,request.FILES)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request, "Estudante cadastrado com sucesso.")
            form.save()
            return redirect("/cadastro/")
        else:
            messages.error(request, "Erro ao cadastrar estudante.")
            print(form.errors)
        context = {
            "form":form
        }
        return render(request,'piloto/pages/Cadastro.html',context=context)