from django.contrib import admin
from .models import Dados, Ocorrencia,Denuncia,Dica,Avaliacao,Alerta

# Configuração básica para Dados
admin.site.register(Dados)
admin.site.register(Denuncia)
admin.site.register(Dica)
admin.site.register(Avaliacao)
admin.site.register(Alerta)

# Configuração personalizada para Ocorrencia
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'tipo_de_lixo', 'descricao')  # Campos que aparecerão na lista
    list_filter = ('tipo_de_lixo',)  # Filtros que serão adicionados à barra lateral
    search_fields = ('descricao', 'endereco')  # Campos pesquisáveis
    fields = ('descricao', 'endereco', 'tipo_de_lixo', 'imagem')  # Ordem e quais campos editar no formulário

admin.site.register(Ocorrencia, OcorrenciaAdmin)
