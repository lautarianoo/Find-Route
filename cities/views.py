from django.shortcuts import render, get_object_or_404
from cities.models import City
from cities.forms import HtmlForm, CityForm
from django.views.generic import DeleteView, DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    form = CityForm()
    context = {'form': form}
    return render(request, 'cities/index.html', context)

def list_city(request, pk=None):
    qs = City.objects.all()
    lst = Paginator(qs, 6)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'cities/cities.html', context)

class CityDetailView(DetailView):
    model = City
    qs = City.objects.all()
    template_name = 'cities/detail.html'

class CityDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:cities')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город удален')
        return self.post(request, *args, **kwargs)