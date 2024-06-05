# Entregable 3 del proyecto
## Sentencias SQL
### 1. Almacén central 
### 2. Corte
####  2.1
| Código requerimiento | RV201 |
| --- | --- |
| Codigo interfaz |  IV201 |
| Imagen interfaz  |

![Alt texasdt](Entregable%201/Mockups%20-%20Figma/Corte/corte_v2/orden_produccion.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Orden de Produccion:** Nos dirigira a la orden de produccion para el jefe de corte |
          SELECT
              o.id_orden_producción,
              o.fecha_inicio,
              o.fecha_fin,
              o.cantidad,
              o.estado AS estado_orden,
              a.nombre AS area,
              tc.nombre AS tipo_corte,
              tmp.nombre AS tipo_materia_prima,
              o.id_orden_trabajo,
              o.fecha_creacion
          FROM
              orden_producción o
          JOIN
              area a ON o.id_area = a.id_area
          JOIN
              dimension_corte dc ON o.id_dim_corte = dc.id_dim_corte
          JOIN
              tipo_corte tc ON dc.id_tipo_corte = tc.id_tipo_corte
          JOIN
              actividad_diaria ad ON o.id_orden_producción = ad.id_orden_producción
          JOIN
              registro_uso_lote rul ON ad.id_actividad = rul.id_actividad
          JOIN
              lote l ON rul.id_lote = l.id_lote
          JOIN
              dimension_materia_prima dmp ON l.id_dim_materia_prima = dmp.id_dim_materia_prima
          JOIN
              tipo_materia_prima tmp ON dmp.id_tipo_materia_prima = tmp.id_tipo_materia_prima
          WHERE
              a.nombre = 'Corte' -- Filtrar por área 'Corte'
          GROUP BY
              o.id_orden_producción, o.fecha_inicio, o.fecha_fin, o.cantidad, o.estado, a.nombre, tc.nombre, tmp.nombre,       
              o.id_orden_trabajo, o.fecha_creacion
          ORDER BY
              o.fecha_inicio DESC;

### 3. Confección 
### 4. Almacén de tránsito 
### 5. Acabados
### 6. Calidad 
### 7. PCP 

**[Ir a la seccion 4](4-carga-datos.md)**

***[Regresar al índice](./entregable%203-indice.md)***
