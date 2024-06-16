from django.db import models

# Create your models here.

class usuario(models.Model):
  nome =  models.CharField(max_length=100) 
  email = models.EmailField()
  senha = models.IntegerField()
  
  def __str__ (self):
    nome = self.nome
    email = self.email
    senha = self.senha
    return f"{nome}, {email}, {senha}"
