from django.views import View
from django.shortcuts import render, redirect
from piloto.models import Estudante
from piloto.forms import EditForm

class ApagarEstudanteView(View):
    def get(self, request, estudante_id):
        print(f"id:{estudante_id}")
        estudante = Estudante.objects.get(pk=estudante_id)
        estudante.delete()
        return redirect('/listar/')
