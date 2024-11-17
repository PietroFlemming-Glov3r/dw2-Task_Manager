from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Projeto, Tarefa, Comentario, Anexo
from .forms import ProjetoForm, TarefaForm, ComentarioForm, AnexoForm  # Assumindo que criará esses forms
from django.contrib.auth import views as auth_views

def home(request):
    projetos = Projeto.objects.all()
    tarefas = Tarefa.objects.all()
    return render(request, 'base.html', {'projetos' : projetos, 'tarefa' : tarefas})

def criar_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProjetoForm()
    return render(request, 'criar_projetos.html', {'form': form})
