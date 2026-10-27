## 1. Creación del repositorio

Se creó un repositorio público en GitHub para almacenar el código fuente, cumplir el requisito de entrega y mantener control de versiones con Git.

## 2. Entorno virtual

Se creó un entorno virtual llamado `.venv` para aislar las dependencias del proyecto, como Django, sin afectar otras instalaciones de Python del equipo.


## 3. Instalación de Django

Se instaló Django dentro del entorno virtual. Django será el framework principal para desarrollar el backend, los modelos, las vistas, las rutas y la interacción con la base de datos.

## 4. Creación del proyecto Django

Se creó el proyecto Django con el nombre técnico `config`. Esta carpeta contendrá la configuración general: rutas principales, ajustes, base de datos y configuración de la aplicación.

## 5. Prueba del servidor local

Se inició el servidor de desarrollo con `python manage.py runserver` y se verificó que la aplicación responde en `http://127.0.0.1:8000/`. Este servidor permite probar el sistema localmente durante el desarrollo.

## 6. Aplicación empleados

Se creó la aplicación `empleados`, que contendrá la lógica, modelos, vistas y rutas necesarias para administrar los departamentos y empleados del sistema.

## 7. Definición de modelos

Se definieron los modelos `Departamento` y `Empleado` en `empleados/models.py`. Cada modelo representa una tabla de la base de datos SQLite y sus atributos representan columnas.

Se estableció una relación de uno a muchos: un departamento puede tener varios empleados, pero cada empleado pertenece a un solo departamento.

## 8. Código correlativo de empleados

Se sobrescribió el método `save()` del modelo `Empleado` para generar automáticamente códigos correlativos con el formato `EMP-0001`, `EMP-0002`, etc.

El código se genera en el backend antes de guardar un empleado y no puede ser ingresado ni modificado por el usuario.


## 9. Migraciones y creación de tablas

Se ejecutó `python manage.py makemigrations` para que Django detectara los modelos creados y generara el archivo de migración `0001_initial.py`. Este archivo describe los cambios necesarios para crear las tablas.

Se ejecutó `python manage.py sqlmigrate empleados 0001` para visualizar el código SQL que Django usaría para crear las tablas de `Departamento` y `Empleado`. Este comando no modifica la base de datos.

Finalmente, se ejecutó `python manage.py migrate` para aplicar las migraciones pendientes y crear físicamente las tablas en la base de datos SQLite, incluyendo las tablas propias del proyecto y las tablas internas necesarias de Django.

## 10. Panel administrativo de Django

Se registraron los modelos `Departamento` y `Empleado` en el panel administrativo de Django.

Se creó un superusuario para ingresar a `/admin/` y comprobar de forma rápida que los modelos, tablas y relaciones funcionan correctamente. El panel administrativo se utilizará solo durante el desarrollo y no forma parte de las pantallas finales del sistema.

## 11. Pruebas de modelos y validaciones

Desde el panel administrativo se verificó que los campos obligatorios de Departamento y Empleado se validan correctamente.

También se comprobó que el código de Departamento no permite valores repetidos y que el código de Empleado se genera automáticamente con el formato correlativo `EMP-0001`.

## 12. Listado público de departamentos

Se creó la vista `lista_departamentos`, que consulta los departamentos almacenados en la base de datos y los ordena por nombre.

Se creó el archivo de rutas de la aplicación `empleados/urls.py` y se conectó desde `config/urls.py` mediante la ruta `/departamentos/`.

También se creó la plantilla `lista_departamentos.html`, que muestra los departamentos en una tabla o un mensaje si no existen registros.


## 13. Creación y validación de departamentos

Se creó `DepartamentoForm` usando `ModelForm`, enlazado al modelo `Departamento`. El formulario permite ingresar código, nombre y descripción.

Se agregó la vista `crear_departamento`, que muestra el formulario con solicitudes GET y procesa los datos enviados con solicitudes POST.

La validación se realiza en Django: Código y Nombre son obligatorios, y el código no permite valores duplicados. Si los datos son correctos, el departamento se guarda en SQLite y el usuario es redirigido al listado.

Se utilizó `{% csrf_token %}` para proteger el formulario frente a solicitudes no autorizadas.


## 14. Edición de departamentos

Se creó la vista `editar_departamento`, que obtiene un departamento mediante su identificador interno (`pk`) y carga sus datos en el formulario existente.

Al enviar el formulario, Django valida los datos y actualiza el mismo registro en SQLite. Si el identificador no existe, se muestra automáticamente una respuesta 404 mediante `get_object_or_404`.

Se agregó un enlace Editar en cada fila del listado de departamentos.


## 15. Eliminación segura de departamentos

Se agregó la opción para eliminar departamentos mediante una pantalla de confirmación y una solicitud POST protegida con `{% csrf_token %}`.

La relación con Empleado utiliza `on_delete=models.PROTECT`. Por ello, un departamento solo puede eliminarse si no tiene empleados asignados; esto evita eliminar datos relacionados por accidente.

## 16. Listado público de empleados

Se creó la vista `lista_empleados`, que consulta los empleados registrados y muestra su código, nombres, apellidos, fecha de nacimiento y departamento asignado.

La consulta utiliza `select_related("departamento")` para obtener eficientemente la información de cada empleado junto con su departamento.

Se agregó la ruta `/empleados/` y una plantilla HTML para mostrar el listado.

## 17. Creación y validación de empleados

Se creó `EmpleadoForm` mediante `ModelForm`. El formulario solicita Nombres, Apellidos, Fecha de nacimiento y Departamento, pero excluye el campo Código porque este se genera automáticamente en el backend.

Se agregó la vista y ruta para crear empleados. Django valida que Nombres, Apellidos y Departamento sean obligatorios.

Al guardar un empleado válido, el método `save()` del modelo asigna automáticamente un código correlativo con formato `EMP-0001`, `EMP-0002`, etc.

## 18. Edición de empleados

Se creó la vista `editar_empleado`, que obtiene un empleado mediante su identificador interno (`pk`) y carga sus datos en el formulario.

El formulario permite modificar Nombres, Apellidos, Fecha de nacimiento y Departamento. El código del empleado se muestra únicamente como lectura y no puede ser modificado.

También se agregó un enlace Editar en cada fila del listado de empleados.

## 19. Eliminación de empleados

Se agregó la eliminación de empleados mediante una pantalla de confirmación y una solicitud POST protegida con `{% csrf_token %}`.

Después de eliminar un empleado, el sistema redirige al listado y muestra un mensaje de confirmación usando el framework de mensajes de Django.


## 20. Plantilla base con Bootstrap

Se creó la plantilla `base.html` para centralizar la estructura visual del sistema.

La plantilla incorpora Bootstrap mediante CDN, una barra de navegación hacia Departamentos y Empleados, un contenedor adaptable para el contenido y alertas para los mensajes de Django.

Las demás páginas heredarán esta plantilla para evitar duplicar código HTML y mantener un diseño consistente.

## 21. Mejora visual del listado de departamentos

Se actualizó el listado de departamentos para heredar la plantilla base y utilizar componentes de Bootstrap: tabla adaptable, botones de acción, tarjetas y estado vacío.

También se ajustó la plantilla base con un encabezado y footer del mismo color institucional, mensajes que desaparecen automáticamente después de dos segundos y un diseño que mantiene el footer al final de la pantalla.

## 22. Formulario de departamentos con Bootstrap

Se mejoró el formulario de creación y edición de departamentos mediante componentes de Bootstrap.

Se configuraron estilos, etiquetas, textos de ayuda y mensajes de error para los campos Código, Nombre y Descripción. La plantilla reutiliza el mismo formulario para crear y editar, manteniendo las validaciones de Django.

## 23. Interfaz de empleados con Bootstrap

Se mejoraron el listado y el formulario de empleados mediante Bootstrap.

El listado ahora presenta una tabla adaptable con acciones para editar y eliminar. El formulario incorpora estilos, etiquetas y mensajes de validación para cada campo.

Durante la edición, el código autogenerado se muestra en un campo de solo lectura, asegurando que el usuario no pueda modificarlo.

## 24. Confirmaciones de eliminación con Bootstrap

Se actualizaron las pantallas de confirmación para eliminar departamentos y empleados.

Cada pantalla utiliza una tarjeta Bootstrap, una alerta de advertencia y botones diferenciados para cancelar o confirmar la eliminación. Las acciones de eliminación continúan utilizando solicitudes POST protegidas con `{% csrf_token %}`.

## 25. Análisis técnico del módulo de asistencia

Se creó el archivo obligatorio `analisis.MD` con una propuesta para implementar un futuro módulo de asistencia.

El documento incluye objetivo, supuestos, modelo de datos, diagrama entidad-relación, pantallas, procesos, preguntas para el encargado, reportes y conclusión.