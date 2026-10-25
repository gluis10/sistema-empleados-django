from django.shortcuts import redirect, render
from .forms import DepartamentoForm
from .models import Departamento

# Create your views here.


def lista_departamentos(request):
    departamentos = Departamento.objects.all().order_by("nombre")

    return render(
        request,
        "empleados/lista_departamentos.html",
        {"departamentos": departamentos},
    )


def crear_departamento(request):
    if request.method == "POST":
        formulario = DepartamentoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("empleados:lista_departamentos")
    else:
        formulario = DepartamentoForm()

    return render(
        request,
        "empleados/formulario_departamento.html",
        {
            "formulario": formulario,
            "titulo": "Crear departamento",
        },
    )
