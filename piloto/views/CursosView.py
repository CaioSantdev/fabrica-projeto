from django.views import View
from piloto.forms import CursosForm
from django.contrib import messages
from django.shortcuts import render, redirect

class CursosView(View):
    def get(self,request):
        form = CursosForm()
        context = {
            "form": form
        }
        return render(request,'piloto/pages/Cursos.html',context=context)

    def post(self,request):
        form = CursosForm(request.POST)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request, "Curso cadastrado com sucesso.")
            form.save()
            return redirect("/cursos/")
        else:
            print(form.errors)
        context = {
            "form":form
        }
        return render(request,'piloto/pages/Cursos.html',context=context)