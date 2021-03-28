from django.urls import path
from trains.views import list_Train, TrainDetailView, TrainDeleteView

urlpatterns = [
    path('trains/', list_Train, name='list_Train'),
    path('trains/detail/<int:pk>', TrainDetailView.as_view(), name='trains_detail'),
    path('trains/delete/<int:pk>', TrainDeleteView.as_view(), name='trains_delete')
]