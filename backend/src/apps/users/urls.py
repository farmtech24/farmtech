from django.urls import path
from . import views

urlpatterns = [
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
]
