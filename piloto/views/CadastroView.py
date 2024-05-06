from django.views import View
from piloto.forms import EstudanteForm
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect

class CadastroView(View):
    formClass = EstudanteForm
    nomeTemplate = "piloto/pages/Cadastro.html"
    def get(self,request):
        form = EstudanteForm()
        context = {
            "form": form
        }
        return render(request,self.nomeTemplate,context=context)

    def post(self,request):
        form = self.formClass(request.POST,request.FILES)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request, "Estudante cadastrado com sucesso.")
            form.save()
            return HttpResponseRedirect("/cadastro/")
        else:
            messages.error(request, "Erro ao cadastrar estudante.")
            print(form.errors)
        context = {
            "form":form
        }
        return render(request,self.nomeTemplate,context=context)