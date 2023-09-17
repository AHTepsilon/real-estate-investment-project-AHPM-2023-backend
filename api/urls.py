from django.urls import path
from .views import post_data
from .views import get_data

urlpatterns = [
    path('rec_system', get_data, name='get_data'),
    path('scraper', post_data, name='post_data'),
]
