
from django.contrib import admin
from django.urls import path, include
from routes.views import list_routes, find_routes, add_route, save_route, RoutesListView, RouteDetailView

urlpatterns = [
    path('', list_routes, name='index'),
    path('admin/', admin.site.urls),
    path('', include(('cities.urls', 'cities'))),
    path('trains/', include(('trains.urls', 'trains'))),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('find_routes/', find_routes, name='find_routes'),
    path('add_routes/', add_route, name='add_route'),
    path('save_route/', save_route, name='save_route'),
    path('list_routes/', RoutesListView.as_view(), name='list_routes'),
    path('detail_route/<int:pk>', RouteDetailView.as_view(), name='detail_route')

]
