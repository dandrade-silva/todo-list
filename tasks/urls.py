from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path('cadastrar_tarefa/', views.cadastrar_tarefa, name="cadastrar_tarefa"),
    path('excluir_tarefa/<int:id>', views.excluir_tarefa, name="excluir_tarefa"),
    path('editar_tarefa/', views.editar_tarefa, name="editar_tarefa"),
    path('atualiza_status/<int:id>/<str:status>',
         views.atualiza_status, name="atualiza_status")

]
