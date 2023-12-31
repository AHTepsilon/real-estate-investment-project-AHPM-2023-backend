from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from .serializers import InfoSerializer, ShowInfoSerializer
from .models import Scraper
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup
import json

def post_data(request):

    url = 'https://www.elpais.com.co/cali/habra-solucion-a-los-lios-ocasionados-por-obra-del-mio-en-valle-del-lili-abandonada-hace-mas-de-6-anos-0853.html'
    url2 = 'https://www.elpais.com.co/cali/atencion-nuevo-incendio-forestal-en-el-sector-de-valle-del-lili-en-cali-1420.html'

    response = requests.get(url)
    response2 = requests.get(url2)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_element = soup.find('h1', class_='text-smoke-700')
        title = title_element.text.strip() if title_element else 'No encontrado'
        soup = BeautifulSoup(response.text, 'html.parser')
        title_element2 = soup.find('h1', class_='text-smoke-700')
        title2 = title_element2.text.strip() if title_element2 else 'No encontrado'

    data = {
        'mensaje': 'Este es el mensaje enviado desde Django',
        'info': 'informacion recibida con exito',
        'scraped': title,
        'scraped2': title2
    }

    return JsonResponse(data)

@csrf_exempt
def get_data(request):
    if request.method == "POST":
        return JsonResponse({"mensaje": "Datos recibidos correctamente"})
    elif request.method == "GET":
        return JsonResponse({"mensaje": "Esta es una solicitud GET"})
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)