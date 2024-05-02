from django.views import View
from django.shortcuts import render, redirect
from piloto.models import Estudante
from piloto.forms import EditForm

class EditarEstudanteView(View):
    def post(self, request, estudante_id):
        estudante = Estudante.objects.get(pk=estudante_id)
        form = EditForm(request.POST, instance=estudante)
        if form.is_valid():
            form.save()
            return redirect('/listar/')
        else:
            print(form.errors)
        context = {
            "form": form
        }
        return render(request, 'piloto/pages/Listar.html', context=context)
