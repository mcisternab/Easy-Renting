from django.contrib import admin
from departamento.models import Zona, Departamento, Tiposervicio , Servicio , Transporte, Contacto
# Register your models here.


admin.site.register(Zona)
admin.site.register(Departamento)
admin.site.register(Tiposervicio)
admin.site.register(Servicio)
admin.site.register(Transporte)
admin.site.register(Contacto)