from django.shortcuts import get_object_or_404, redirect, render
from .forms import DepartamentoForm, EmpleadoForm
from .models import Departamento, Empleado
from django.contrib import messages
from django.db.models.deletion import ProtectedError

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


def eliminar_departamento(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)

    if request.method == "POST":
        try:
            departamento.delete()
            messages.success(request, "Departamento eliminado correctamente.")
        except ProtectedError:
            messages.error(
                request,
                "No se puede eliminar el departamento porque tiene empleados asignados.",
            )

        return redirect("empleados:lista_departamentos")

    return render(
        request,
        "empleados/confirmar_eliminacion_departamento.html",
        {"departamento": departamento},
    )


def lista_empleados(request):
    empleados = Empleado.objects.select_related("departamento").order_by(
        "apellidos",
        "nombres",
    )

    return render(
        request,
        "empleados/lista_empleados.html",
        {"empleados": empleados},
    )


def crear_empleado(request):
    if request.method == "POST":
        formulario = EmpleadoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("empleados:lista_empleados")
    else:
        formulario = EmpleadoForm()

    return render(
        request,
        "empleados/formulario_empleado.html",
        {
            "formulario": formulario,
            "titulo": "Crear empleado",
        },
    )


