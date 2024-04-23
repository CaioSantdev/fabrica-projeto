from django.db import models

# Create your models here.
class Campus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

SITUACAO = {
    'VINCULADO': "Vinculado",
    'FORMADO': "Formado",
    'JUBILADO': "Jubilado",
    'EVADIDO': "Evadido",
}
MODO_DE_ENTRADA ={
    'VESTIBULAR': "Vestibular",
    'SISU': "SISU",
    'PSENEM': "PSEnem",
}
class Student(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14,unique=True)
    registration = models.CharField(max_length=9,unique=True)
    brith_date = models.DateField()
    image = models.ImageField()
    # problema de d0n_delete CASCADE -> RESOLVER!!
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)

    situation = models.CharField(max_length=10,choices=SITUACAO,default="VINCULADO")
    entry_mode = models.CharField(max_length=10,choices=MODO_DE_ENTRADA,default="SISU")

    def __str__(self):
        return self.name