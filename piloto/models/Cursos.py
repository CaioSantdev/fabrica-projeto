from django.db import models
from piloto.models import Campus


class Cursos(models.Model):
    nomeCurso = models.CharField(verbose_name="Nome do curso",max_length=100)
    campus = models.ForeignKey(Campus,verbose_name="Campus", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nomeCurso} - {self.campus}"
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"