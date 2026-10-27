from django.urls import path

from . import views

app_name = "empleados"

urlpatterns = [
    path("departamentos/", views.lista_departamentos, name="lista_departamentos"),
    path(
        "departamentos/nuevo/",
        views.crear_departamento,
        name="crear_departamento",
    ),
    path(
        "departamentos/<int:pk>/editar/",
        views.editar_departamento,
        name="editar_departamento",
    ),
    path(
        "departamentos/<int:pk>/eliminar/",
        views.eliminar_departamento,
        name="eliminar_departamento",
    ),
    path("empleados/",
        views.lista_empleados, 
        name="lista_empleados"
    ),
    path("empleados/nuevo/", 
         views.crear_empleado, 
         name="crear_empleado"
    ),
    path("empleados/<int:pk>/editar/",
        views.editar_empleado,
        name="editar_empleado",
    ),
]

