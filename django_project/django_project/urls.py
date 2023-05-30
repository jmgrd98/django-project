from django.urls import path
from django_app import views
from django_app.views import home
from django_app.views import usuarios

urlpatterns = [
    path('', home, name='home'),
    path('usuarios/', usuarios, name='listagem_usuarios'),
]
