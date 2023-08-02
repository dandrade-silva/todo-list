from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("teste/", views.teste, name='teste'),
    path('cadastrar_tarefa/', views.cadastrar_tarefa, name="cadastrar_tarefa")
]
