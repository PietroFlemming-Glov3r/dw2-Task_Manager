from django.contrib import admin
from .models import Projeto, Tarefa, Comentario, Anexo


admin.site.register(Projeto)
admin.site.register(Tarefa)
admin.site.register(Comentario)
admin.site.register(Anexo)