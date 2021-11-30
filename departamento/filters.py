import django_filters 
from .models import *

class ServicioFilter(django_filters.FilterSet):
    class Meta:
        model = Servicio
        fields = '__all__'
        exclude = ['imagen']

class TransporteFilter(django_filters.FilterSet):
    class Meta:
        model = Transporte
        fields = '__all__'
        exclude = ['imagen']