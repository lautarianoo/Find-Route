from django.shortcuts import render, get_object_or_404
from cities.models import City

def index(request):
    return render(request, 'cities/index.html')

def list_city(request, pk=None):
    if pk:
        #city = City.objects.filter(id=pk).first()
        city = get_object_or_404(City, id=pk)
        return render(request, 'cities/detail.html', {'object': city})
    qs = City.objects.all()
    context = {'object_list': qs}
    return render(request, 'cities/cities.html', context)
