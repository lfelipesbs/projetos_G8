from django.urls import path
from.import views

urlpatterns = [
    path('pagina_login/', views.pagina_login, name="pagina_login"),
    path('pagina_home/', views.pagina_home, name="pagina_home"),
    path('pagina_home/', views.pagina_home, name="pagina_home"),
    path('processar_formulario/', views.processar_formulario, name="processar_formulario"),
    
]
