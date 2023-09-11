from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from .serializers import InfoSerializer, ShowInfoSerializer
from .models import Scraper
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup

def post_data(request):

    url = 'https://www.elpais.com.co/cali/habra-solucion-a-los-lios-ocasionados-por-obra-del-mio-en-valle-del-lili-abandonada-hace-mas-de-6-anos-0853.html'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_element = soup.find('h1', class_='text-smoke-700')
        title = title_element.text.strip() if title_element else 'No encontrado'

    data = {
        'mensaje': 'Este es el mensaje enviado desde Django',
        'info': 'informacion recibida con exito',
        'scraped': title,
    }

    return JsonResponse(data)


'''
class ScraperView(generics.ListAPIView):
    queryset = Scraper.objects.all()
    serializer_class = InfoSerializer

class ShowInfoView(APIView):

    serializer_class = ShowInfoSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request)
        if serializer.is_valid():
            idCode = serializer.data.get('idCode')
            price = serializer.data.get('price')
            neighborhood = serializer.data.get('neighborhood')
            commune = serializer.data.get('commune')
            address = serializer.data.get('address')

            scrapedInfo = Scraper(idCode = idCode, price = price, neighborhood = neighborhood, commune = commune, address = address)

            scrapedInfo.save()


        return Response(InfoSerializer(scrapedInfo).data, status=status.HTTP_202_ACCEPTED)
'''