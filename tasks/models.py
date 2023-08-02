from django.db import models
from datetime import datetime

# Create your models here.


class Tarefa(models.Model):
    lista_status = (
        ('pd', 'pendente'),
        ('ea', 'em andamento'),
        ('cc', 'concluida')
    )

    tarefa = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=lista_status)
    data_criacao = models.DateField(default=datetime.now, blank=False)

    def __str__(self):
        return self.tarefa
