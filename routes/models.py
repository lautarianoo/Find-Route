from django.db import models
from cities.models import City
from trains.models import Train
from django.core.exceptions import ValidationError

class Route(models.Model):
    '''Модель для создание табличи Поездов в БД'''
    name = models.CharField(max_length=50, unique=True, verbose_name = 'Название маршрута')
    travel_times = models.PositiveSmallIntegerField(verbose_name = 'Общее время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set', verbose_name='Из какого города')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_to_city_set', verbose_name='В какой город')
    trains = models.ManyToManyField(Train, verbose_name='Список поездов для маршрута')

    def __str__(self):
        return f'Маршрут {self.name} из города {self.from_city} в город {self.to_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['travel_times']
