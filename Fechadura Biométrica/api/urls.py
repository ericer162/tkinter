from django.urls import path
from . import views

urlpatterns = [
    path('verificar/', views.verificar_acesso, name='verificar_acesso'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
]