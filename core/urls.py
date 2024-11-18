from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('criar', views.criar_projeto, name='criar_projeto'),
    path('criarTarefa', views.criar_tarefa, name='criar_tarefa'),
]
