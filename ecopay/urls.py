from django.contrib import admin
from django.urls import path, include
from webapp import views  # Garanta que suas views estão corretamente importadas deste módulo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('home_aluno/', views.home_aluno, name="home_aluno"),
    path('home_adm/', views.home_adm, name="home_adm"),
    path('processar_formulario/', views.processar_formulario, name="processar_formulario"),
    path('registrar_ocorrencia/', views.registrar_ocorrencia, name="registrar_ocorrencia"),  # Adicionando a nova rota
     path('dicas/', views.dicas, name='dicas'),
]

# Adicionando as URLs de arquivos estáticos e de mídia
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
