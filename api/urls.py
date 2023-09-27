from django.urls import path
from .views import post_data

urlpatterns = [
    path('scraper', post_data, name='post_data'),
]
