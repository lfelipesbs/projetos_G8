from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Dados(models.Model):
    # Definindo as opções para o campo 'tipo'
    TIPO_USUARIO_CHOICES = (
        ('administrador', 'Administrador'),
        ('usuario', 'Usuário'),
    )

    tipo = models.CharField(max_length=50, choices=TIPO_USUARIO_CHOICES, default='usuario')
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='usuarios/', null=True, blank=True)  # Campo para armazenar a imagem do usuário

    def __str__(self):
        # Método para retornar uma string representativa do objeto
        return f"Tipo: {self.tipo} - Nome do usuário: {self.nome} - Senha: {self.senha}"

class Ocorrencia(models.Model):
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    tipo_de_lixo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='ocorrencias/', null=True, blank=True)  # Armazena na pasta /media/ocorrencias
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.endereco} - {self.tipo_de_lixo}"
    
class Dica(models.Model):
    TIPO_DICA_CHOICES = (
        ('reciclagem', 'Reciclagem'),
        ('orientacoes', 'Orientações'),
        ('cuidados', 'Cuidados'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_DICA_CHOICES)
    texto = models.TextField()

    def __str__(self):
        return self.texto

class Denuncia(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE)
    motivo = models.TextField()

class Alerta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_envio = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField()
    local = models.CharField(max_length=255, default="N/A")
    tipo = models.CharField(max_length=255, default="N/A")
    acao = models.TextField(default="N/A")

    def __str__(self):
        return f'Alerta de {self.usuario} em {self.data_envio}'