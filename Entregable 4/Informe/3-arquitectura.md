# Entregable 4 del proyecto
## 1. Estructura de App Web

Se detalla la estructura que se usa para desarrollarla app web:
* **vback:** Django.
* **venv:** Entorno virtual de python.
* **virca:** Backend - Django Rest Framework y Python.
* **vircatex:** Frontend - React y Javascript.

![Estructura](estructura.png)
  
### Requirements:
Archivo de componentes de instalación necesarios para el entorno de producción.
```
asgiref==3.8.1
dj-database-url==2.2.0
Django==5.0.6
django-cors-headers==4.3.1
djangorestframework==3.15.1
gunicorn==22.0.0
packaging==24.1
psycopg2==2.9.9
python-decouple==3.8
sqlparse==0.5.0
typing_extensions==4.12.2
whitenoise==6.6.0
```
| Paquete                   | Versión  | Descripción                                                                                                              | Propósito                                                                                                                 |
|---------------------------|----------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| asgiref                   | 3.8.1    | Biblioteca de referencia para ASGI (Asynchronous Server Gateway Interface).                                               | Proporciona herramientas y utilidades para implementar servidores y aplicaciones ASGI.                                     |
| dj-database-url           | 2.2.0    | Biblioteca para configurar la conexión a la base de datos usando URLs.                                                   | Simplifica la configuración de la base de datos, útil para despliegues en plataformas de nube.                             |
| Django                    | 5.0.6    | Framework web de alto nivel para desarrollo rápido de aplicaciones web.                                                  | Proporciona herramientas para construir aplicaciones web robustas y escalables.                                            |
| django-cors-headers       | 4.3.1    | Biblioteca que permite manejar CORS (Cross-Origin Resource Sharing) en Django.                                           | Facilita la configuración de CORS, esencial para aplicaciones con frontend separado del backend.                           |
| djangorestframework       | 3.15.1   | Biblioteca potente y flexible para construir APIs web en Django.                                                        | Proporciona herramientas para crear APIs RESTful, incluyendo serializadores y vistas basadas en clases.                    |
| gunicorn                  | 22.0.0   | Servidor HTTP WSGI para aplicaciones web Python.                                                                         | Desplegar aplicaciones Django en producción, robusto y de alto rendimiento.                                                |
| packaging                 | 24.1     | Biblioteca para manejar versiones y dependencias de paquetes Python.                                                     | Ayuda a interpretar versiones de paquetes y dependencias.                                                                 |
| psycopg2                  | 2.9.9    | Adaptador de base de datos PostgreSQL para Python.                                                                       | Permite que Django se comunique con una base de datos PostgreSQL.                                                          |
| python-decouple           | 3.8      | Biblioteca para separar configuraciones y credenciales del código fuente.                                                | Facilita la gestión de configuraciones, cargándolas desde archivos de entorno.                                             |
| sqlparse                  | 0.5.0    | Biblioteca para el análisis, formateación y manipulación de sentencias SQL.                                              | Usado por Django para formatear y manejar consultas SQL.                                                                   |
| typing_extensions         | 4.12.2   | Biblioteca que proporciona funcionalidades adicionales para el módulo `typing` de Python.                                | Permite el uso de anotaciones de tipos más recientes en versiones anteriores de Python.                                    |
| whitenoise                | 6.6.0    | Biblioteca que permite servir archivos estáticos directamente desde una aplicación Django en producción.                 | Facilita el manejo de archivos estáticos, mejorando el despliegue y el rendimiento.                                        |



## 2. Arquitectura y tecnología

### Arquitectura de Software

| Aspecto de Arquitectura       | Detalle                                               |
|-------------------------------|-------------------------------------------------------|
| Frameworks de Front End      | React <br>[![React](https://img.shields.io/badge/React-17.0.2-blue.svg?style=for-the-badge&logo=react&logoColor=white)]()                                                 |
| Frameworks de Back End       | Django <br> [![Django](https://img.shields.io/badge/Django-3.2.3-blue.svg?style=for-the-badge&logo=django&logoColor=white)]()                                               |
| Frameworks de Seguridad      | Django Security <br> [![Django Security](https://img.shields.io/badge/Django%20Security-Enabled-green.svg?style=for-the-badge&logo=django&logoColor=white)]()                                      |
| Lenguaje de Programación de Base | JavaScript para el front-end (con React), Python para el back-end (con Django) <br> [![JavaScript version](https://img.shields.io/badge/JavaScript-ES6-yellow.svg?style=for-the-badge&logo=javascript&logoColor=white)]()  [![Python version](https://img.shields.io/badge/Python-3.9-blue.svg?style=for-the-badge&logo=python&logoColor=white)]()|
| Editor de código             | Visual Studio Code <br> [![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-1.65.0-blue.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)]()                                |
| Bibliotecas                  | Material UI <br> [![Material UI](https://img.shields.io/badge/Material%20UI-v5.0.0-blue.svg?style=for-the-badge&logo=material-ui&logoColor=white)]() |

### Arquitectura de Datos

| Aspecto de Arquitectura | Detalle       |
|--------------------------|---------------|
| Motor de Base de Datos   | PostgreSQL <br> [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.0-blue.svg?style=for-the-badge&logo=postgresql&logoColor=white)]()    |

### Stack
![Stack](../../Entregable%203/stack.png)

### Arquitectura
![Arquqitectura](arq.png)
***Herramienta: LucidSpark***

### Front end
[Vircatex - render](https://sistema-web-v-f.onrender.com/) <br>

### App Web
Despliegue Backend y PostgreSQL : [Render](https://render.com/)

### Conexión Base de datos (local)
![db](../../Entregable%203/db.png)

### Conexión Base de datos (render)
![db](../postgres-render.png)

### Producción
![Servicios](./render-services-1.png)

### Herramientas
#### Pruebas

* **Postman**
Es una plataforma colaborativa para el desarrollo de APIs que facilita la creación, prueba, documentación y monitoreo de APIs. Es ampliamente utilizada por desarrolladores y equipos de desarrollo debido a su robustez y a las múltiples características que ofrece.

  - Funciones Principales:

    - Colecciones: Permite organizar las solicitudes en colecciones para mantener las pruebas estructuradas y reutilizables.
Variables de Entorno: Se pueden definir variables de entorno para manejar diferentes configuraciones (desarrollo, pruebas, producción) sin necesidad de cambiar los detalles de la solicitud.
    - Pre-request Scripts y Test Scripts: Permite ejecutar scripts (usando JavaScript) antes de enviar la solicitud y después de recibir la respuesta para automatizar pruebas y validar respuestas.
    - Historial de Solicitudes: Mantiene un historial de todas las solicitudes realizadas para fácil referencia y repetición.
Autenticación: Soporta varios tipos de autenticación (Bearer Token, OAuth, API Key, etc.), facilitando las pruebas de seguridad.
    - ocumentación de API: Genera documentación de API directamente desde las colecciones, útil para compartir con otros desarrolladores y equipos.
Monitoreo y Automación: Ofrece herramientas para monitorear el rendimiento de la API y automatizar las pruebas con integraciones CI/CD.

* **Thunder Client:**
Thunder Client es una extensión ligera para Visual Studio Code diseñada para probar APIs RESTful de una manera rápida y sencilla. Es ideal para desarrolladores que prefieren no salir de su editor de código para realizar pruebas de API.

  - Funciones Principales:

    - Interfaz Integrada en VS Code: Se ejecuta directamente dentro de VS Code, eliminando la necesidad de cambiar de aplicación para probar APIs.
Solicitudes Rápidas: Facilita la creación y ejecución de solicitudes HTTP de manera rápida sin necesidad de configuraciones extensas.
    - Variables de Entorno: Permite definir variables de entorno similares a Postman para manejar diferentes configuraciones.
Historial de Solicitudes: Guarda el historial de solicitudes realizadas para fácil referencia y repetición.
    - Colecciones y Carpetas: Permite organizar las solicitudes en colecciones y carpetas para mantener el proyecto estructurado.
Pre-request y Test Scripts: Soporta scripts de pre-request y de test utilizando JavaScript.
    - Soporte de Autenticación: Soporta varios métodos de autenticación (Bearer Token, Basic Auth, etc.).
   

**Aplicación en el Desarrollo y Pruebas del Proyecto**
Para el proyecto con Django, React y PostgreSQL, hemo usado las herramientas de la siguiente manera:

- Probar Endpoints de Django: Postman o Thunder Client para enviar solicitudes GET, POST, PUT y DELETE a los endpoints de tu API Django para asegurarte de que respondan correctamente.

- Validación de Datos: Verificar que las respuestas de la API correspondan con los datos esperados almacenados en PostgreSQL.

- Documentación y Colaboración: Uso de Postman para generar documentación interactiva de la API.

[Regresar al Índice](./indice.md)
