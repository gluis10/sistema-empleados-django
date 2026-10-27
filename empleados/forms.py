from django import forms

from .models import Departamento, Empleado


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ["codigo", "nombre", "descripcion"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 3}),
        }


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["nombres", "apellidos", "fecha_nacimiento", "departamento"]
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={"type": "date"}),
        }
