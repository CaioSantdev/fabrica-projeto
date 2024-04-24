from django.db import models
from piloto.models import Campus


class Cursos(models.Model):
    name = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.campus}"
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"