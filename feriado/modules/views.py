
from django.shortcuts import render, HttpResponse 
from datetime import date

from .models import FeriadoModel


def holliday(request):
    hoje = date.today()
    
    if FeriadoModel.objects.filter(ano=hoje.year, mes=hoje.month, dia=hoje.day).exists():
        contexto = {
            'ehferiado': True,
        }
    else:
        contexto = {
            'ehferiado': False,
        }
    
    return render(request, 'index.html', contexto)

# Create your views here.
