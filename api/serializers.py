from rest_framework import serializers
from .models import Scraper

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scraper
        fields = ('id', 'idCode', 'price', 'neighborhood', 'commune', 'address')

class ShowInfoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Scraper
       fields = ( 'idCode', 'price', 'neighborhood', 'commune', 'address')
