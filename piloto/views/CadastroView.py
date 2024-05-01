from django.views import View
from piloto.forms import EstudanteForm
from django.shortcuts import render

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
            form.save()
        else:
            print(form.errors)
        context = {
            "form":form
        }
        return render(request,'piloto/pages/Cadastro.html',context=context)