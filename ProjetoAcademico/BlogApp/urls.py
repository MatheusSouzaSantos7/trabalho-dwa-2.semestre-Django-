from django.urls import path, include
from BlogApp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('usuario/',views.usuarios_api),
    path('postagem/', views.postagens_api),
    path('login/',views.usuarios_api),
    path('cadastro/', views.usuarios_api),
]