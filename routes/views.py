from django.shortcuts import render
from routes.forms import RouteForm
from django.contrib import messages
from routes.utils import get_routes

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
a = 1