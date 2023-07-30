from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'tasks/index.html')


def teste(request):
    return render(request, 'tasks/teste.html')
