from django.urls import path
from . import views

urlpatterns = [
    path('', views.holliday, name='feriados'),
    path('cadastro', views.cadastro, name='cadastro'),
]