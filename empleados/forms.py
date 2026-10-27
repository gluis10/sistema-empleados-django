from django import forms

from .models import Departamento, Empleado


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ["codigo", "nombre", "descripcion"]
        widgets = {
            "codigo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. TI",
                }
            ),
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. Tecnología",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Descripción opcional",
                }
            ),
        }


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["nombres", "apellidos", "fecha_nacimiento", "departamento"]
        widgets = {
            "nombres": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. Ana",
                }
            ),
            "apellidos": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. López",
                }
            ),
            "fecha_nacimiento": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "departamento": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }

