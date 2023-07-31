from django.shortcuts import render
from .models import Tarefa

# Create your views here.


def index(request):
    tarefas = Tarefa.objects.all().order_by('data_criacao')

    return render(request, 'tasks/index.html', {'tarefas': tarefas})


def teste(request):
    return render(request, 'tasks/teste.html')
