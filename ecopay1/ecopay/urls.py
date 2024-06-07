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
]

# Adicionando as URLs de arquivos estáticos e de mídia
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
