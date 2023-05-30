from django.urls import path
from django_app import views
from django_app.views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios', views.usuarios, name='listagem_usuarios'),
]
