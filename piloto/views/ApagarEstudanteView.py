from django.views import View
from piloto.models import Estudante
from django.http import HttpResponseRedirect

class ApagarEstudanteView(View):
    def get(self, request, estudante_id):
        print(f"id:{estudante_id}")
        estudante = Estudante.objects.get(pk=estudante_id)
        estudante.delete()
        return HttpResponseRedirect('/listar/')
