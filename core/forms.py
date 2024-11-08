from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao']

from django import forms
from .models import Tarefa  # Importe o modelo 'Tarefa' que o formulário usa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'  # Ou defina campos específicos

from .models import Comentario  # Importe o modelo 'Comentario'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'  # Ou especifique os campos necessários

from django import forms
from .models import Anexo  # Importe o modelo 'Anexo'

class AnexoForm(forms.ModelForm):
    class Meta:
        model = Anexo
        fields = '__all__'  # Ou especifique os campos necessários
