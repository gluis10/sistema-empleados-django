from django.shortcuts import get_object_or_404, redirect, render
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


def editar_departamento(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)

    if request.method == "POST":
        formulario = DepartamentoForm(request.POST, instance=departamento)

        if formulario.is_valid():
            formulario.save()
            return redirect("empleados:lista_departamentos")
    else:
        formulario = DepartamentoForm(instance=departamento)

    return render(
        request,
        "empleados/formulario_departamento.html",
        {
            "formulario": formulario,
            "titulo": "Editar departamento",
        },
    )


