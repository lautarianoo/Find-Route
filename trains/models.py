from django.db import models
from cities.models import City

class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name = 'Название поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name = 'Время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set', verbose_name='Из какого города')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city_set', verbose_name='В какой город')

    def __str__(self):
        return f'Поезд №{self.name} из города {self.from_city} в город {self.to_city}'

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']