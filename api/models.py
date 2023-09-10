from django.db import models
import string
import random

def generateIdCode():
    length = 6

    while True:
        idCode = ''.join(random.choices(string.ascii_lowercase, k=length))
        if Scraper.objects.filter(idCode=idCode).count() == 0:
            break
    
    return idCode

# Create your models here.
class Scraper(models.Model):
    idCode = models.CharField(max_length = 20, default=generateIdCode, unique=False)
    price = models.IntegerField(default=0, unique=False)
    neighborhood = models.CharField(max_length = 40, default='', unique=False)
    commune = models.CharField(max_length = 40, default='', unique=False)
    address = models.CharField(max_length = 40, default='', unique=False)
