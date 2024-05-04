from django.db import models
from piloto.models import Curso
import datetime

SITUACAO = {
    1: "Vinculado",
    2: "Formado",
    3: "Jubilado",
    4: "Evadido",
    5: "INATIVO",
}
MODO_DE_ENTRADA ={
    1: "Vestibular",
    2: "SISU",
    3: "PSEnem",
}

class Estudante(models.Model):
    nome = models.CharField(verbose_name="Nome do Estudante",max_length=256)
    cpfEstudante = models.CharField(verbose_name="CPF do Estudante",max_length=14,unique=True)
    matricula = models.CharField(verbose_name="Matricula",max_length=9,unique=True,)
    dataAniversario = models.DateField(verbose_name="Data de aniversário",null=True)
    eImagem = models.ImageField(verbose_name="Foto do Estudante",upload_to="piloto/img/%Y/%m/%d")
    curso = models.ForeignKey(Curso,verbose_name="Curso do Estudante",on_delete=models.CASCADE)
    situacao = models.IntegerField(verbose_name="Situação do Estudante",choices=SITUACAO,default=1)
    modoDeEntrada = models.IntegerField(verbose_name="Modo de Entrada",choices=MODO_DE_ENTRADA,default=2)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"
        
    def save(self,*args, **kwargs):
        # self.cpfFormatado()
        self.matriculaUnica()
        super().save(*args, **kwargs)

    
    def matriculaUnica(self):
        if not self.matricula:
            anoAtual = datetime.datetime.now().year
            semestre = 1 if datetime.datetime.now().month <= 6 else 2 

            if Estudante.objects.exists():
                ultimaMatricula = Estudante.objects.last().matricula
                ultimoNumero = int(ultimaMatricula[-4:])
            else:
                ultimoNumero = 0

            novoNumero = ultimoNumero + 1

            matricula = f"{anoAtual}{semestre}{novoNumero:04d}"
            self.matricula = matricula

    # def cpfFormatado(self):
    #     cpfFormatado = "{}.{}.{}-{}".format(self.cpfEstudante[:3],self.cpfEstudante[3:6],
    #                                         self.cpfEstudante[6:9],self.cpfEstudante[9:])
    #     self.cpfEstudante = cpfFormatado