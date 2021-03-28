from django.shortcuts import render, get_object_or_404
from trains.models import Train
from django.views.generic import DeleteView, DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def list_Train(request, pk=None):
    qs = Train.objects.all()
    lst = Paginator(qs, 6)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'trains/trains_list.html', context)

class TrainDetailView(DetailView):
    model = Train
    qs = Train.objects.all()
    template_name = 'trains/detail.html'

class TrainDeleteView(SuccessMessageMixin,DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('cities:cities')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поезд удален')
        return self.post(request, *args, **kwargs)