
from django.shortcuts import render, HttpResponse 
from datetime import date

from .models import FeriadoModel
from modules.forms import FeriadoForm
from .FeriadosAPI import FeriadosAPI
from .models import FeriadoModelApi

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

    
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html', {'formulario': FeriadoForm()})
    else:
        formulario = FeriadoForm(request.POST)
        if formulario.is_valid():
            dados = formulario.cleaned_data
            FeriadoModel.objects.create(**dados)
            contexto = {'feriado': dados.get('nome')}
            return render(request, 'sucess.html', contexto)
        else:
            contexto = {'formulario': formulario}
            return render(request, 'cadastro.html', contexto)

def home(request):
    return render(request, 'index.html')

def cadastra_api(request):
    api = FeriadosAPI(2022)

    for feriado in api.feriados:
        nome, data = feriado
        cadastro = FeriadoModelApi(nome=nome, data=data)
        cadastro.save()

    return HttpResponse('')
    

# Create your views here.
