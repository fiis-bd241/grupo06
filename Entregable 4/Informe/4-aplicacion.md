# Entregable 4 del proyecto
## Aplicación

### Front end
Abrir en Google Chrome: [Vircatex - render](https://sistema-web-v-f.onrender.com/#/acabados/lotes) 

[Github]() 


### App Web
Despliegue Backend y PostgreSQL : [Render](https://render.com/)

[Github]() 

### Conexión Base de datos (local)
![db](../../Entregable%203/db.png)



## Versión final:
Presentamos el flujo de pantallas de la App Web: **[Sistema Vircatex](https://sistema-web-v-f.onrender.com/)**:

- [Almacén Central](#almacén-central)
- [Corte](#corte)
- [Confección](#confección)
- [Almacén_de_tránsito](#almacén-de-tránsito)
- [Acabados](#acabados)
- [Inspección_de_calidad](#inspección-de-calidad)
- [PCP - Abastecimiento](#pcp)


### Home
![Home](./pantallas/home.png)

![Home1](./gif/1.gif)

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue?style=for-the-badge)](#versión-final)

### Almacén Central

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue?style=for-the-badge)](#versión-final)

### Corte

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue?style=for-the-badge)](#versión-final)

### Confección

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue?style=for-the-badge)](#versión-final)
  
### Almacén de tránsito

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue?style=for-the-badge)](#versión-final)

### Acabados
#### Submenú 1: **General**: 
**Navegación**: Acabados > General <br>
Muestra los datos generales del área.<br>
Se realizan dos consultas a la BD.
![Acabados 1](./images/generalaca.png)

* Consulta 1: Lista de Operarios

```python
class EmpleadoListView(View):
    def get(self, request):
         with connection.cursor() as cursor:
            cursor.execute("SELECT id_empleado, nombre FROM empleado WHERE id_area = 5")
            rows = cursor.fetchall()
            result = [
                    {'id_empleado': row[0], 'nombre': row[1]}
                    for row in rows
                ]
            return JsonResponse(result, safe=False)
```

* Consulta 2: Lista de Acabados

```python
class AcabadoListView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_acabado, nombre FROM acabado")
            data = cursor.fetchall()
        
        # Formatear los resultados en un diccionario
        resultados = [{'id_acabado': row[0], 'nombre': row[1]} for row in data]
```

#### Submenú 2: **Lote-caja**: 
Muestra las cajas asignadas a los operarios de acabados.<br>


**Navegación**: Acabados > lotes > Reporte
![Acabados 22](./pantallas/reporte.png)

* Consulta: Reporte entre dos fechas
```python
class ReporteAcabadosView(View):
    def get(self, request):
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')

        query = """
        SELECT DISTINCT e.id_empleado, e.nombre, e.primer_apellido,
                        e.segundo_apellido, e.id_correo, e.dni, e.id_cargo,
                        caja_prenda.id_caja, caja_prenda.fecha_creacion,
                        tipo_prenda.nombre 
        FROM empleado e
        JOIN prenda ON e.id_empleado = prenda.id_empleado
        JOIN caja_prenda ON prenda.id_caja = caja_prenda.id_caja
        JOIN dimension_prenda ON caja_prenda.id_dim_prenda = dimension_prenda.id_dim_prenda
        JOIN dimension_confeccion ON dimension_prenda.id_dim_confeccion = dimension_confeccion.id_dim_confeccion
        JOIN guia_confeccion ON dimension_confeccion.id_guia_confeccion = guia_confeccion.id_guia_confeccion
        JOIN tipo_prenda ON dimension_confeccion.id_tipo_prenda = tipo_prenda.id_tipo_prenda
        WHERE id_area=5 AND id_cargo=2
        AND caja_prenda.fecha_creacion BETWEEN %s AND %s
        """

        with connection.cursor() as cursor:
            cursor.execute(query, [fecha_inicio, fecha_fin])
            rows = cursor.fetchall()

        resultados = [
            {
                "id_empleado": row[0],
                "nombre": row[1],
                "primer_apellido": row[2],
                "segundo_apellido": row[3],
                "id_correo": row[4],
                "dni": row[5],
                "id_cargo": row[6],
                "id_caja": row[7],
                "fecha_creacion": row[8],
                "tipo_prenda": row[9],
            }
            for row in rows
        ]

        return JsonResponse(resultados, safe=False)
```

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue?style=for-the-badge)](#versión-final)

### Inspección de calidad

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue?style=for-the-badge)](#versión-final)

### PCP

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue?style=for-the-badge)](#versión-final)


[Regresar al Índice](./indice.md)


[Regresar al Índice](./indice.md)
