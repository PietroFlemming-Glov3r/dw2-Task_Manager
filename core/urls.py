from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name="home"),
    path('criar', views.criar_projeto, name='criar_projeto'),
    path('criarTarefa', views.criar_tarefa, name='criar_tarefa'),
    path('excluir_projeto/<int:projeto_id>/', views.excluir_projeto, name='excluir_projeto'),
    path('excluir_tarefa/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('projeto/editar/<int:projeto_id>/', views.editar_projeto, name='editar_projeto'),
    path('tarefa/editar/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa'),
    path('comentario/adicionar/<int:tarefa_id>/', views.adicionar_comentario, name='adicionar_comentario'),
    path('comentario/excluir/<int:comentario_id>/', views.excluir_comentario, name='excluir_comentario'),
    path('anexo/<int:anexo_id>/', views.visualizar_anexo, name='visualizar_anexo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
