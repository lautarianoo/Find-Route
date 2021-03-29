from django.urls import path
from cities.views import index, list_city, CityDeleteView, CityDetailView

urlpatterns = [
    path('cities/', list_city, name='cities'),
    path('cities/detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('cities/delete/<int:pk>/', CityDeleteView.as_view(), name='delete')
]
