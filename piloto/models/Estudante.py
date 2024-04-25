from django.db import models
from piloto.models import Cursos
import datetime, random

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
    nomeEstudante = models.CharField(verbose_name="Nome do Estudante",max_length=100)
    cpfEstudante = models.CharField(verbose_name="Cpf do Estudante",max_length=14,unique=True)
    matriculaEstudante = models.CharField(verbose_name="Matricula",max_length=9,unique=True,)
    dataAniversario = models.DateField(verbose_name="Data de aniversário",null=True)
    eImagem = models.ImageField(verbose_name="Foto do Estudante",upload_to="piloto/img/%Y/%m/%d")
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
            semestre = 1 if datetime.datetime.now().month <= 6 else 2 

            while True:
                numeroAleatorio = random.randint(1000,9999)
                matricula = f"{anoAtual}{semestre}{numeroAleatorio}"
                
                if not Estudante.objects.filter(matriculaEstudante=matricula).exists():
                    self.matriculaEstudante = matricula
                    return super(Estudante,self).save()