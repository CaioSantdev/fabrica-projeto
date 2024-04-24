# from typing import Iterable
from django.db import models
from piloto.models import Cursos
import datetime

SITUACAO = {
    1: "Vinculado",
    2: "Formado",
    3: "Jubilado",
    4: "Evadido",
}
MODO_DE_ENTRADA ={
    1: "Vestibular",
    2: "SISU",
    3: "PSEnem",
}

class Estudante(models.Model):
    nomeEstudante = models.CharField("Nome do Estudante",max_length=100)
    cpfEstudante = models.CharField("Cpf do Estudante",max_length=14,unique=True)
    matriculaEstudante = models.CharField("Matricula",max_length=9,unique=True,)
    dataAniversario = models.DateField("Data de aniversário",null=True)
    eImagem = models.ImageField("Foto do Estudante",)
    # problema de d0n_delete CASCADE -> RESOLVER!!
    cursoEstudante = models.ForeignKey(Cursos,verbose_name="Curso do Estudante",on_delete=models.CASCADE)
    situacaoEstudante = models.IntegerField(verbose_name="Situação do Estudante",choices=SITUACAO,default="VINCULADO")
    modoDeEntrada = models.IntegerField(verbose_name="Modo de Entrada",choices=MODO_DE_ENTRADA,default="SISU")

    def __str__(self):
        return self.nomeEstudante
    
    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"

    def save(self):
        if not self.matriculaEstudante:
            anoAtual = datetime.datetime.now().year
            mesAtual = datetime.datetime.now().month
            semestre = 1 if mesAtual <= 6 else 2 


            Estudante.objects.filter(matriculaEstudante=matricula).exists()




        return super(Estudante,self).save()