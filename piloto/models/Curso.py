from django.db import models
from piloto.models import Campus


class Curso(models.Model):
    nome = models.CharField(verbose_name="Nome do curso",max_length=100)
    campus = models.ForeignKey(Campus,verbose_name="Campus", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nome} - {self.campus}"
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"