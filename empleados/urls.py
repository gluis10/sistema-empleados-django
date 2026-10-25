from django.urls import path

from . import views

app_name = "empleados"

urlpatterns = [
    path("", views.lista_departamentos, name="lista_departamentos"),
    path("nuevo/", views.crear_departamento, name="crear_departamento"),
    path("<int:pk>/editar/", views.editar_departamento, name="editar_departamento"),
]




