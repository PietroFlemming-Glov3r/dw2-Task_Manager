from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('criar', views.criar_projeto, name='criar_projeto'),
    path('criarTarefa', views.criar_tarefa, name='criar_tarefa'),
    path('excluir_projeto/<int:projeto_id>/', views.excluir_projeto, name='excluir_projeto'),
    path('excluir_tarefa/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),
]
