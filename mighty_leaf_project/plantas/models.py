
from django.db import models
from django.contrib.auth.models import User

class Planta(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plantas')

    def __str__(self):
        return self.nome
