from django.shortcuts import render, redirect
from .models import Tarefa
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime


def index(request):
    tarefas = Tarefa.objects.all().order_by('data_criacao')

    return render(request, 'tasks/index.html', {'tarefas': tarefas})


def teste(request):
    return render(request, 'tasks/teste.html')


def cadastrar_tarefa(request):
    tarefa = request.POST.get('tarefa')

    if Tarefa.objects.filter(tarefa=tarefa).exists():
        messages.add_message(request, constants.ERROR,
                             'Essa tarefa já está cadastrada')
        return redirect('/')

    tarefa = Tarefa(
        tarefa=tarefa,
        status="pd",
        data_criacao=datetime.now()
    )

    tarefa.save()

    messages.add_message(request, constants.INFO,
                         'Tarefa cadastrada com sucesso')

    return redirect('/')
