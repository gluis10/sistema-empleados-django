from django.urls import path

from . import views

app_name = "empleados"

urlpatterns = [
    path("", views.lista_departamentos, name="lista_departamentos"),
]


