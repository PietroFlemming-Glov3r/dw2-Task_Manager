from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_projetos, name='listar_projetos'),
    path('criar', views.criar_projeto, name='criar_projeto'),
     path('login/', views.login_view, name='login'),
]
