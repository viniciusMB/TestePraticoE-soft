from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=15)
    sobrenome = models.CharField(max_length=40)
    apelido = models.CharField(max_length=10)
    email = models.EmailField()
    idade = models.SmallIntegerField()
    dataNascimento = models.DateField()
    obs = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('nome', 'sobrenome')
    
    
    
    def __str__(self):
        return self.nome
    
