from django.db import models

class Campus(models.Model):
    nomeCampus = models.CharField(verbose_name="Nome do Campus",max_length=100)

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campi"

    def __str__(self):
        return self.nomeCampus