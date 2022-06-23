from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import requests

def holliday(request):
  requisicao = requests.get("https://brasilapi.com.br/api/feriados/v1/2022")
  try:
        listFeriado = requisicao.json()
  except ValueError:
        print("A resposta não chegou com o formato esperado.")

  dateHollidays = []
  hoje = datetime.today().strftime('%Y-%m-%d')
  for valor in listFeriado:
        dateHollidays.append(valor['date'])

  return HttpResponse(dateHollidays)

  return render(request, "index.html", contexto)

# Create your views here.
