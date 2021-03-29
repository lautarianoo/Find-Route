
from django.contrib import admin
from django.urls import path, include
from routes.views import list_routes, find_routes

urlpatterns = [
    path('', list_routes, name='index'),
    path('admin/', admin.site.urls),
    path('', include(('cities.urls', 'cities'))),
    path('trains/', include(('trains.urls', 'trains'))),
    path('find_routes/', find_routes, name='find_routes'),
]
