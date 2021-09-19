
from users.views import dptos
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from departamento.views import index, dptos, dptos2

urlpatterns = [
    path('index', index),
    path('dptos', dptos),
    path('dptos2', dptos2),
]