from django.db import models

class Dados(models.Model):
    # Definindo as opções para o campo 'tipo'
    TIPO_USUARIO_CHOICES = (
        ('administrador', 'Administrador'),
        ('usuario', 'Usuário'),
    )

    tipo = models.CharField(max_length=50, choices=TIPO_USUARIO_CHOICES, default='usuario')
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='usuarios/', null=True, blank=True)  # Campo para armazenar a imagem do usuário

    def __str__(self):
        # Método para retornar uma string representativa do objeto
        return f"Tipo: {self.tipo} - Nome do usuário: {self.usuario} - Senha: {self.senha}"

class Ocorrencia(models.Model):
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    tipo_de_lixo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='ocorrencias/', null=True, blank=True)  # Armazena na pasta /media/ocorrencias

    def __str__(self):
        return f"{self.endereco} - {self.tipo_de_lixo}"