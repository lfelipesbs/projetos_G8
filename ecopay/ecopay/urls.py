
from django.contrib import admin
from django.urls import path, include
from webapp import views

urlpatterns = [
    path('', views.login, name="login")
 ]