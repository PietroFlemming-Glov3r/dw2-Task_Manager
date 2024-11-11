from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
#   path('', views.listar_projetos, name='listar_projetos'),
    path('criar', views.criar_projeto, name='criar_projeto'),
]
