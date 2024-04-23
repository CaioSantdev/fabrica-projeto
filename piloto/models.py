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

class Student(models.Model):
    registration = models.CharField(max_length=9,unique=True)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14,unique=True)
    brith_date = models.DateField()
    image = models.ImageField(upload_to='piloto/img/%Y/%m/%d/')
    # problema de d0n_delete CASCADE -> RESOLVER!!
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)


    VINCULADO ="Vinculado"
    FORMADO= "Formado"
    JUBILADO="Jubilado"
    EVADIDO= "Evadido"

    VESTIBULAR="Vestibular"
    SISU="SISU"
    PSENEM="PSEnem"

    situacao = {
    VINCULADO: "Vinculado",
    FORMADO: "Formado",
    JUBILADO: "Jubilado",
    EVADIDO: "Evadido",
    }
    modo_de_entrada ={
        VESTIBULAR: "Vestibular",
        SISU: "SISU",
        PSENEM: "PSEnem",
    }
    situation = models.CharField(max_length=10,choices=situacao,default="VINCULADO")
    entry_mode = models.CharField(max_length=10,choices=modo_de_entrada,default="SISU")

    def __str__(self):
        return self.name