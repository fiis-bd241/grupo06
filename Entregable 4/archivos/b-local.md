## Crear Backend Local
**Indicaciones**

1. Crear una carpeta e instala en VSC

2. Creación del Proyecto Django

***Instalación de Django y psycopg2***

Crea un entorno virtual y activa dicho entorno.

* **En Linux y macOS:**
```
python3 -m venv myenv
source myenv/bin/activate
```

* **En Windows:**
```
python -m venv myenv
myenv\Scripts\activate
```
Si hay un error de PSSecurityException:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```
***Instala Django y psycopg2-binary (conector de PostgreSQL para Python).***

```
pip install django psycopg2-binary
```

3. Crea un nuevo proyecto Django.

```
django-admin startproject myproject . 
cd myproject
```

4. Configuración de Django para Usar PostgreSQL

Abre el archivo settings.py dentro del directorio del proyecto (por ejemplo, myproject/settings.py) y modifica la sección DATABASES para usar PostgreSQL

```sql
# myproject/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vircatex',
        'USER': 'postgres',
        'PASSWORD': 'prueba',
        'HOST': 'localhost',  # O la IP del servidor de PostgreSQL
        'PORT': '5432',  # El puerto por defecto de PostgreSQL
    }
}

```

5. Ejecuta las migraciones iniciales y crea un superusuario para la administración.
```sql
python manage.py migrate
```

6. Ejecutar el Servidor de Desarrollo
```sql
python manage.py runserver

```

7. Creación de una Aplicación Django
```sql
python manage.py startapp myapp
```

* Añade la nueva aplicación a la lista de aplicaciones instaladas en settings.py.
```sql
# myproject/settings.py

INSTALLED_APPS = [
    # ...
    'myapp',
    # ...
]
```


8. Instalar Django REST Framework

```python
pip install djangorestframework
```
9. Configurar

```python
# myproject/settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'myapp',  # tu aplicación
]
```


10. Autogenerar Models (Opcional)
```
python manage.py inspectdb > myapp/models.py
```

**Crea y aplica las migraciones para estos modelos.**

```python
python manage.py makemigrations myapp
python manage.py migrate
```

11. Agregar el model en models.py
```python
from django.db import models

class Acabado(models.Model):
    id_acabado = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'acabado'
```

12. Modificar el Views.py
```python
# myapp/views.py

from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def acabado_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM acabado")
        results = cursor.fetchall()

        # Extraer los nombres de las columnas
        columns = [col[0] for col in cursor.description]

    # Convertir los resultados en una lista de diccionarios
    acabados = [dict(zip(columns, row)) for row in results]

    return Response(acabados)
```

13. Modificar el urls.py en myproject

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('sistema/', include('myapp.urls')),  # Incluye las URLs de tu aplicación
]
```
14. Modificar el urls.py en myapp

```python
from django.urls import path
from .views import acabado_list

urlpatterns = [
    path('acabado/', acabado_list, name='acabado_list'),
]

```
15. Ejecutar el Servidor de Desarrollo
```sql
python manage.py runserver

```

16. Abrir enlace compuesto para acceder a la API:

http://127.0.0.1:8000/sistema/acabado/
