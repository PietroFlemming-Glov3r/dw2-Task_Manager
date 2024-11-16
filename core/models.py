from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return ''

class Tarefa(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="tarefas")
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    prazo = models.DateField()
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('em progresso', 'Em Progresso'), ('concluída', 'Concluída')])

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return ''

class Comentario(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} em {self.tarefa}"
    
    def get_absolute_url(self):
        return ''

class Anexo(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name="anexos")
    arquivo = models.FileField(upload_to="anexos/")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return ''