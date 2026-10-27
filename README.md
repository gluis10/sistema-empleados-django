# Sistema de gestión de empleados

Aplicación web desarrollada con Django para administrar departamentos y empleados.

## Funcionalidades

- CRUD de departamentos.
- Validación de código único para departamentos.
- CRUD de empleados.
- Asignación de un departamento a cada empleado.
- Código de empleado autogenerado con formato `EMP-0001`.
- Validaciones de campos obligatorios.
- Confirmación segura antes de eliminar registros.
- Interfaz adaptable creada con Bootstrap.
- Panel administrativo de Django para pruebas y administración.

## Tecnologías utilizadas

- Python 3.14
- Django 6.1.2
- SQLite
- Bootstrap 5
- HTML
- JavaScript
- Git y GitHub

## Instalación y ejecución

Clona el repositorio:

```bash
git clone https://github.com/gluis10/sistema-empleados-django.git
cd sistema-empleados-django
```

Crea y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

Aplica las migraciones:

```bash
python manage.py migrate
```

Inicia el servidor local:

```bash
python manage.py runserver
```

Abre el proyecto en el navegador:

```text
http://127.0.0.1:8000/departamentos/
```

## Rutas principales

- `/departamentos/`: gestión de departamentos.
- `/empleados/`: gestión de empleados.
- `/admin/`: panel administrativo de Django.

## Estructura del proyecto

- `config/`: configuración principal de Django.
- `empleados/`: modelos, formularios, vistas, rutas y plantillas del sistema.
- `docs/bitacora.md`: registro de decisiones y pasos del desarrollo.
- `analisis.MD`: análisis técnico del módulo futuro de asistencia.
- `requirements.txt`: dependencias necesarias para ejecutar el proyecto.

## Análisis técnico

El archivo `analisis.MD` contiene la propuesta para un futuro módulo de asistencia de empleados, incluyendo modelo de datos, procesos, pantallas, supuestos y preguntas de negocio.




