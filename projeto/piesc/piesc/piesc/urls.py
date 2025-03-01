from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inicio/', views.home, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('login/', views.login_view, name='login'),  # Atualizado para usar login_view
    path('cadastro/', views.cadastro, name='cadastro'),
    path('user/', views.user, name='user'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),  # Nova rota para editar perfil
]
