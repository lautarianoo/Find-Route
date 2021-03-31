from django.shortcuts import render, redirect
from routes.forms import RouteForm, RouteModelForm
from django.contrib import messages
from routes.utils import get_routes
from cities.models import City
from trains.models import Train
from django.views.generic import ListView, DetailView
from routes.models import Route

def list_routes(request):
    form = RouteForm()
    return render(request, 'routes/find_rout.html', {'form': form})

def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/find_rout.html', {'form': form})
            return render(request, 'routes/find_rout.html', context)
        return render(request, 'routes/find_rout.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')
        return render(request, 'routes/find_rout.html', {'form': form})

def add_route(request):
    if request.method == 'POST':
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split(',')
            trains_list = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_list).select_related('from_city', 'to_city')
            citites = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(initial={'from_city': citites[from_city_id], 'to_city': citites[to_city_id], 'travel_times': total_time,
                                           'trains': qs})
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, 'Невозможно сохранить несуществующий маршрут')
        return redirect('/')

def save_route(request):
    if request.method == 'POST':
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Маршрут сохранён')
            return redirect('/')
        else:
            pass
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, 'Невозможно сохранить несуществующий маршрут')
        return redirect('/')

class RoutesListView(ListView):
    paginate_by = 10
    model = Route
    template_name = 'routes/routes_list.html'

class RouteDetailView(DetailView):
    model = Route
    qs = Route.objects.all()
    template_name = 'routes/detail.html'
