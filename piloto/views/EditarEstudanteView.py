from django.views import View
from django.shortcuts import render
from piloto.models import Estudante
from piloto.forms import EditForm
from django.http import HttpResponseRedirect

class EditarEstudanteView(View):
    formClass = EditForm
    nomeTemplate = "piloto/pages/Listar.html"
    def post(self, request, estudante_id):
        estudante = Estudante.objects.get(pk=estudante_id)
        form = self.formClass(request.POST, instance=estudante)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/listar/')
        else:
            print(form.errors)
        context = {
            "form": form
        }
        return render(request, self.nomeTemplate, context=context)
