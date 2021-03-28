from django.urls import path
from trains.views import list_Train, TrainDetailView, TrainDeleteView, TrainUpdateView, TrainCreateView

urlpatterns = [
    path('trains/', list_Train, name='list_Train'),
    path('trains/detail/<int:pk>', TrainDetailView.as_view(), name='trains_detail'),
    path('trains/delete/<int:pk>', TrainDeleteView.as_view(), name='trains_delete'),
    path('trains/update/<int:pk>', TrainUpdateView.as_view(), name='trains_update'),
    path('trains/add', TrainCreateView.as_view(), name='trains_add')
]