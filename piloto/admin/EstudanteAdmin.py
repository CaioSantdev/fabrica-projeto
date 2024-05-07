from django.contrib import admin
from ..models import *
from faker import Faker
import random
# Register your models here.
@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ['id','nome','matricula','cpfFormatado','status']
    readonly_fields = ['matricula',]
    actions= ['generate_estudante']
    
    @admin.display(description='CPF Formatado')
    def cpfFormatado(self,obj):
        return f'****{obj.cpfEstudante[6:11]}**'
    
    @admin.action(description="Gerar Alunos")  
    def generate_estudante(self,queryset,obj):
        faker = Faker('pt_BR')
        SITUACAO = {
            1: "Vinculado",
            2: "Formado",
            3: "Jubilado",
            4: "Evadido",
            5: "Desvinculado",
        }
        MODO_DE_ENTRADA ={
            1: "Vestibular",
            2: "SISU",
            3: "PSEnem",
        }
        STATUS ={
            1: "Ativo",
            2: "Inativo",
        }
        for i in range(1000):
            nome = faker.name()
            cpf = faker.cpf()
            data_aniversario = faker.date()
            imagem = None  # Assuming you don't have fake image generation

            # Select a random existing Curso or create a fake one if none exists
            curso = Curso.objects.order_by('?').first()  # Random Curso
            if not curso:
                curso = Curso.objects.create(nome=f"Curso Fake {faker.word()}")

            # Random choices from pre-defined options
            situacao = random.choice(list(SITUACAO.keys()))
            status = random.choice(list(STATUS.keys()))
            modo_entrada = random.choice(list(MODO_DE_ENTRADA.keys()))
            novoEstudante = Estudante(
                nome=nome,
                cpfEstudante=cpf,
                dataAniversario=data_aniversario,
                eImagem=imagem,
                curso=curso,
                situacao=situacao,
                status=status,
                modoDeEntrada=modo_entrada
            )
            novoEstudante.save()
        return
# Generate and save a specific number of fake students