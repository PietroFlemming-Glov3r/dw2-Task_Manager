from django import forms
from .models import Projeto, Tarefa, Comentario, Anexo 

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao']


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['tarefa', 'conteudo']

class AnexoForm(forms.ModelForm):
    class Meta:
        model = Anexo
        fields = '__all__'  # Ou especifique os campos necessários
