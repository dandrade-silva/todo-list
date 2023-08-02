from django.shortcuts import render, redirect
from .models import Tarefa
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime


def index(request):
    tarefas = Tarefa.objects.all().order_by('data_criacao')

    return render(request, 'tasks/index.html', {'tarefas': tarefas})


def cadastrar_tarefa(request):
    tarefa = request.POST.get('tarefa')

    if not tarefa.strip():
        messages.add_message(request, constants.ERROR,
                             '[ERRO] A categoria não pode ser vazia ou conter apenas espaços')
        return redirect('/')

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

    messages.add_message(request, constants.SUCCESS,
                         'Tarefa cadastrada com sucesso')

    return redirect('/')


def excluir_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()

    messages.add_message(request, constants.SUCCESS,
                         'Tarefa removida com sucesso')

    return redirect('/')


def editar_tarefa(request):
    # tarefa = Tarefa.objects.get(id=id)
    # tarefa.delete()

    messages.add_message(request, constants.INFO,
                         'Implementar Editar Tarefa...')

    return redirect('/')


def atualiza_status(request, id, status):
    tarefa = Tarefa.objects.get(id=id)

    tarefa.status = status

    tarefa.save()

    return redirect('/')
