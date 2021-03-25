from django.urls import path
from cities.views import index, list_city

urlpatterns = [
    path('', index, name='index'),
    path('cities/', list_city, name='cities'),
    path('cities/<int:pk>/', list_city, name='city'),
]
