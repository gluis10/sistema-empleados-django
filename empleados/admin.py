from django.contrib import admin

# Register your models here.
from .models import Departamento, Empleado

admin.site.register(Departamento)
admin.site.register(Empleado)


