from django.views import View
from piloto.forms import CampusForm
from piloto.models import Campus
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect

class CampusView(View):
    formClass = CampusForm
    nomeTemplate = "piloto/pages/Campus.html"
    def get(self,request):
        
        form = CampusForm()
        context = {
            "form": form,
            "campus": Campus.objects.all()
        }
        return render(request,self.nomeTemplate,context=context)

    def post(self,request):
        form = self.formClass(request.POST)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request, "Campus cadastrado com sucesso.")
            form.save()
            return HttpResponseRedirect("/campus/")
        else:
            messages.error(request, "Erro ao cadastrar campus.")
            print(form.errors)
        context = {
            "form":form
        }
        return render(request,self.nomeTemplate,context=context)