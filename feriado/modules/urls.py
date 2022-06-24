from django.urls import path
from . import views

urlpatterns = [
    path('', views.holliday, name='feriados'),
    path('', views.cadastra_api),
    path('home', views.home, name='home'),
    path('cadastro', views.cadastro, name='cadastro'),
]