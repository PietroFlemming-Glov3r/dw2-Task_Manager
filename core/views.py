from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Projeto, Tarefa, Comentario, Anexo
from .forms import ProjetoForm, TarefaForm, ComentarioForm, AnexoForm
from django.contrib.auth import views as auth_views

@login_required
def excluir_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    projeto.delete()
    return redirect('home')

@login_required
def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('home')

@login_required
def excluir_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    comentario.delete()
    return redirect('home')

def home(request):
    projetos = Projeto.objects.all()
    tarefas = Tarefa.objects.all()
    return render(request, 'base.html', {'projetos': projetos, 'tarefas': tarefas})

@login_required
def criar_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProjetoForm()
    return render(request, 'criar_projetos.html', {'form': form})

@login_required
def criar_tarefa(request):
    if request.method == "POST":
        tarefa_form = TarefaForm(request.POST)
        anexo_form = AnexoForm(request.POST, request.FILES)

        if tarefa_form.is_valid():
            tarefa = tarefa_form.save()

            if anexo_form.is_valid():
                anexo = anexo_form.save(commit=False)
                anexo.tarefa = tarefa
                anexo.save()

            return redirect('/')

    else:
        tarefa_form = TarefaForm()
        anexo_form = AnexoForm()

    context = {
        'form': tarefa_form,
        'anexo_form': anexo_form,
    }
    return render(request, 'criar_tarefas.html', context)

@login_required
def editar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'editar_projeto.html', {'form': form})

@login_required
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'editar_tarefa.html', {'form': form})

def adicionar_comentario(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        if conteudo:
            comentario = Comentario(
                tarefa=tarefa,
                conteudo=conteudo,
                autor=request.user  # Add the current user as author
            )
            comentario.save()
            return redirect('home')
    
    return redirect('home')

def visualizar_anexo(request, anexo_id):
    anexo = get_object_or_404(Anexo, id=anexo_id)
    return render(request, 'visualizar_anexo.html', {
        'anexo': anexo,
        'MEDIA_URL': settings.MEDIA_URL
    })