from django import forms
from trains.models import Train
from cities.models import City

class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Номер поезда', widget=forms.TextInput())
    travel_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput())
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(), widget=forms.Select())
    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(), widget=forms.Select())
    class Meta:
        model = Train
        fields = '__all__'