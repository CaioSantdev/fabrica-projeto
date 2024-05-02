from django.db import models
from piloto.models import Curso
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
    nome = models.CharField(verbose_name="Nome do Estudante",max_length=256)
    cpfEstudante = models.CharField(verbose_name="CPF do Estudante",max_length=14,unique=True)
    matricula = models.CharField(verbose_name="Matricula",max_length=9,unique=True,)
    dataAniversario = models.DateField(verbose_name="Data de aniversário",null=True)
    eImagem = models.ImageField(verbose_name="Foto do Estudante",upload_to="piloto/img/%Y/%m/%d")
    # problema de d0n_delete CASCADE -> RESOLVER!!
    curso = models.ForeignKey(Curso,verbose_name="Curso do Estudante",on_delete=models.CASCADE)
    situacao = models.IntegerField(verbose_name="Situação do Estudante",choices=SITUACAO,default="VINCULADO")
    modoDeEntrada = models.IntegerField(verbose_name="Modo de Entrada",choices=MODO_DE_ENTRADA,default="SISU")

    def __str__(self):
        return self.nomeEstudante
    
    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"

    def save(self, *args, **kwargs):
        if not self.matricula:
            anoAtual = datetime.datetime.now().year
            semestre = 1 if datetime.datetime.now().month <= 6 else 2 
            
            # Obtendo o último número da matrícula
            ultimoNumero = Estudante.objects.filter(
                matricula__startswith=f"{anoAtual}{semestre}"
            ).aggregate(models.Max('matricula'))['matricula__max']
            if ultimoNumero:
                ultimoNumero = int(ultimoNumero[-4:])
            else:
                ultimoNumero = 0

            novoNUmero = ultimoNumero + 1

            matricula = f"{anoAtual}{semestre}{novoNUmero:04d}"
            self.matricula = matricula
            
        # if self.cpfEstudante:
        #     self.cpfEstudante = self.format_cpf(self.cpfEstudante)
            
        super().save(*args, **kwargs)
        
        
    # def format_cpf(self, cpf):
    # # Verifica se o CPF já está formatado
    #     if '.' in cpf and '-' in cpf:
    #         return cpf

    # # Formata o CPF com pontos e traços
    #     cpf = cpf.zfill(11)
    #     return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"