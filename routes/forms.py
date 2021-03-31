from django import forms
from cities.models import City
from routes.models import Route, Train

class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))

    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))

    cities = forms.ModelMultipleChoiceField(label='Через города', queryset=City.objects.all(),
                                       widget=forms.SelectMultiple(attrs={'class': 'form-control js-example-basic-multiple'}), required=False)

    traveling_time = forms.IntegerField(label='Время в пути',
                                     widget=forms.NumberInput(attrs={'class': 'form-control'}))


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Название маршрута',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название маршрута'}))

    from_city = forms.ModelChoiceField(queryset=City.objects.all(),
                                       widget=forms.HiddenInput())

    to_city = forms.ModelChoiceField(queryset=City.objects.all(),
                                     widget=forms.HiddenInput())

    trains = forms.ModelMultipleChoiceField(queryset=Train.objects.all(),
                                       widget=forms.SelectMultiple(attrs={'class': 'form-control d-none'}), required=False)

    travel_times = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = '__all__'