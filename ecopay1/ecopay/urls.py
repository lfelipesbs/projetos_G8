from django.contrib import admin
from django.urls import path, include
from webapp import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('cadastrar_usuario/',views.cadastrar_usuario, name="cadastrar_usuario"),
    path('cadastro/',views.cadastro,name="cadastro"),
    path('fazer_login/', views.fazer_login, name="fazer_login"),
    path('', views.login, name="login"),
    
    path('home_aluno/', views.home_aluno, name="home_aluno"),
    path('home_adm/', views.home_adm, name="home_adm"),
    
    path('registrar_ocorrencia/', views.registrar_ocorrencia, name="registrar_ocorrencia"), 
    path('vizualizar_ocorrencia/', views.vizualizar_ocorrencia, name="vizualizar_ocorrencia"), 
    path('vizualizar_ocorrencia_user/', views.vizualizar_ocorrencia_user, name="vizualizar_ocorrencia_user"),
    path('ocorrencias/', views.listar_ocorrencias, name='listar_ocorrencias'),
    path('excluir_ocorrencia/<int:ocorrencia_id>/', views.excluir_ocorrencia, name='excluir_ocorrencia'),
    path('editar_ocorrencia/<int:ocorrencia_id>/', views.editar_ocorrencia, name='editar_ocorrencia'),
    path('denuncia_adm/', views.denuncia_adm, name='denuncia_adm'),
    path('ocorrencia/<int:ocorrencia_id>/denunciar/', views.denunciar_ocorrencia, name='denunciar_ocorrencia'),

    path('stats/', views.stats, name='stats'),
    path('estatisticas_ocorrencias/', views.estatisticas_ocorrencias, name='estatisticas_ocorrencias'),

    path('adicionar_dica/', views.adicionar_dica, name='adicionar_dica'),
    path('exibir_dica/', views.exibir_dica, name='exibir_dica'),
    path('dicas_adm/', views.dicas_adm, name="dicas_adm"),
    path('dicas/', views.dicas, name="dicas"),

    path('alerta_adm/', views.alerta_adm, name='alerta_adm'),
    path('ver_alertas/', views.ver_alertas, name='ver_alertas'),

     path('avaliar_ocorrencia/<int:ocorrencia_id>/', views.avaliar_ocorrencia, name='avaliar_ocorrencia'),
     path('ver_feedbacks/', views.ver_feedbacks, name='ver_feedbacks'),

      path('mapa/', views.mapa_ocorrencias, name='mapa_ocorrencias'),
    


]

# Adicionando as URLs de arquivos estáticos e de mídia
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
