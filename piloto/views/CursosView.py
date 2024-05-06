from django.views import View
from piloto.forms import CursosForm
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect

class CursosView(View):
    formClass = CursosForm
    nomeTemplate = "piloto/pages/Cursos.html"
    def get(self,request):
        form = CursosForm()
        context = {
            "form": form
        }
        return render(request,self.nomeTemplate,context=context)

    def post(self,request):
        form = self.formClass(request.POST)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request, "Curso cadastrado com sucesso.")
            form.save()
            return HttpResponseRedirect("/cursos/")
        else:
            messages.error(request, "Erro ao cadastrar curso.")
            print(form.errors)
        context = {
            "form":form
        }
        return render(request,self.nomeTemplate,context=context)