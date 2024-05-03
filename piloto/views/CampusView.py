from django.views import View
from piloto.forms import CampusForm
from django.contrib import messages
from django.shortcuts import render, redirect

class CampusView(View):
    def get(self,request):
        form = CampusForm()
        context = {
            "form": form
        }
        return render(request,'piloto/pages/Campus.html',context=context)

    def post(self,request):
        form = CampusForm(request.POST)
        if form.is_valid():
            print(f'Request: {request.POST}')
            messages.success(request, "Campus cadastrado com sucesso.")
            form.save()
            return redirect("/campus/")
        else:
            print(form.errors)
        context = {
            "form":form
        }
        return render(request,'piloto/pages/Campus.html',context=context)