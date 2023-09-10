from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from .serializers import InfoSerializer, ShowInfoSerializer
from .models import Scraper
from rest_framework.views import APIView
from rest_framework.response import Response

def post_data(request):
    data = {
        'mensaje': 'Este es el mensaje enviado desde Django',
        'info': 'informacion recibida con exito',
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