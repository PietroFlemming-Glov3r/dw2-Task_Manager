from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Projeto, Tarefa, Comentario, Anexo
from .forms import ProjetoForm, TarefaForm, ComentarioForm, AnexoForm  # Assumindo que criará esses forms
from django.contrib.auth import views as auth_views

def login_view(request):
    return auth_views.LoginView.as_view(template_name='core/login.html')(request)

@login_required
def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/listar_projetos.html', {'projetos': projetos})

@login_required
def criar_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'core/criar_projeto.html', {'form': form})
