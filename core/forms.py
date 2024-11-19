from django import forms
from .models import Projeto, Tarefa, Comentario, Anexo 

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao']


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'responsavel', 'prazo', 'status', 'projeto']  # Ensure titulo is first
        labels = {
            'titulo': 'Nome da Tarefa',  # Explicit label
            'descricao': 'Descrição',
            'prazo': 'Prazo',
            'status': 'Status',
            'projeto': 'Projeto',
            'responsavel': 'Responsável'
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']

class AnexoForm(forms.ModelForm):
    class Meta:
        model = Anexo
        fields = ['arquivo', 'nome'] 
