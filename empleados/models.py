from django.db import models

# Modelo que representa la tabla de departamentos.
class Departamento(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

# Modelo que representa la tabla de empleados.
class Empleado(models.Model):
    codigo = models.CharField(max_length=10, unique=True, editable=False)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.PROTECT,
        related_name="empleados",
    )

    # Representación legible del empleado.
    def __str__(self):
        return f"{self.codigo} - {self.nombres} {self.apellidos}"

    #  # Genera el código correlativo antes de guardar un empleado nuevo.
    def save(self, *args, **kwargs):
        if not self.codigo:
            ultimo = Empleado.objects.order_by("-id").first()

            if ultimo is None:
                siguiente_numero = 1
            else:
                siguiente_numero = int(ultimo.codigo.split("-")[1]) + 1

            self.codigo = f"EMP-{siguiente_numero:04d}"

        super().save(*args, **kwargs)

