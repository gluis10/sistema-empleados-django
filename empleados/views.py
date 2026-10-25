from django.shortcuts import render

# Create your views here.
from .models import Departamento


def lista_departamentos(request):
    departamentos = Departamento.objects.all().order_by("nombre")

    return render(
        request,
        "empleados/lista_departamentos.html",
        {"departamentos": departamentos},
    )

