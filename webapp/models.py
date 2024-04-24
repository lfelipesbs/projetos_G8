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

    def __str__(self):
        # Método para retornar uma string representativa do objeto
        return f"Tipo: {self.tipo} - Nome do usuário: {self.usuario} - Senha: {self.senha}"
