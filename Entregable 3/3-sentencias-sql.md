# Entregable 3 del proyecto
## Sentencias SQL
### 1. Almacén central 
### 2. Corte
####  2.1
| Código requerimiento | RV201 |
| --- | --- |
| Codigo interfaz |  IV201 |
| Imagen interfaz  |

![](../Entregable%201/Mockups%20-%20Figma/Corte/corte_v2/orden_produccion.png)
| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Orden de Produccion:** Nos dirigirá a la orden de produccion para el jefe de corte |
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
              
####  2.2
| Código requerimiento | RV202 |
| --- | --- |
| Codigo interfaz |  IV202 |
| Imagen interfaz  |

![](../Entregable%201/Mockups%20-%20Figma/Corte/corte_v2/asignar_actividad.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Asignar:** Nos dirigirá a asignar actividad |
|**INSERT INTO actividad_diaria (fecha_actividad, id_orden_producción) VALUES (<2>, <3>);**|
|**INSERT INTO maquina_actividad (id_actividad, id_maquina, cantidad_hecha) VALUES (1, <1>, <4>);**|

####  2.3
| Código requerimiento | RV207 |
| --- | --- |
| Codigo interfaz |  IV203 |
| Imagen interfaz  |

![](../Entregable%201/Mockups%20-%20Figma/Corte/corte_v2/actividades_maquina_dia.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Operario corte:** Nos dirigirá al detalle que el oprario debe programar la maquina |
          SELECT
              a.fecha_actividad,
              o.id_orden_producción,
              o.cantidad AS cantidad_orden,
              m.id_maquina,
              ma.cantidad_hecha AS cantidad_realizar,
              t.nombre AS tipo_corte
          FROM actividad_diaria a
          JOIN maquina_actividad ma ON a.id_actividad = ma.id_actividad
          JOIN maquina m ON ma.id_maquina = m.id_maquina
          JOIN orden_producción o ON a.id_orden_producción = o.id_orden_producción
          JOIN corte c ON o.id_dim_corte = c.id_dim_corte
          JOIN dimension_corte t ON c.id_dim_corte = t.id_dim_corte
          WHERE a.fecha_actividad = CURRENT_DATE
          ORDER BY o.id_orden_producción, m.id_maquina;

####  2.4
| Código requerimiento | RV208 |
| --- | --- |
| Codigo interfaz |  IV204 |
| Imagen interfaz  |

![](../Entregable%201/Mockups%20-%20Figma/Corte/corte_v2/operario_corte.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Operaio corte:** El oprario insertara los valores del corte que se realizaxo y la cantidad de lote usado |
|**INSERT INTO lote (id_tipo_lote, cantidad, id_dim_corte, id_dim_confeccion, id_dim_materia_prima, id_actividad, fecha_creacion) VALUES (<1>, <2>, <3>, NULL, NULL, <4>, <5>);**|
|**INSERT INTO Registro_uso_lote (id_actividad, id_lote, cantidad_usada) VALUES (<6>, <7>, <8>);**|

####  2.5
| Código requerimiento | RV203 |
| --- | --- |
| Codigo interfaz |  IV205 |
| Imagen interfaz  |

![](../Entregable%201/Mockups%20-%20Figma/Corte/corte_v2/actividad_diaria_maquina.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Detalle Corte:** El jefe de corte visualizara las actividades diarias por máquina |
          SELECT 
              ma.id_maquina,
              m.capacidad_total,
              COUNT(ad.id_actividad) AS cantidad_actividades,
              ad.fecha_actividad
          FROM 
              actividad_diaria ad
          JOIN 
              maquina_actividad ma ON ad.id_actividad = ma.id_actividad
          JOIN 
              maquina m ON ma.id_maquina = m.id_maquina
          WHERE 
              ad.fecha_actividad = '2024-06-03'  -- Aquí especificas la fecha deseada
          GROUP BY 
              ma.id_maquina, m.capacidad_total, ad.fecha_actividad
          ORDER BY 
              cantidad_actividades DESC;  -- Ordenar la cantidad de actividades de forma descendente

####  2.6
| Código requerimiento | RV204 |
| --- | --- |
| Codigo interfaz |  IV206 |
| Imagen interfaz  |

![](../Entregable%201/Mockups%20-%20Figma/Corte/corte_v2/cortes_actividad.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Ver actividad:** El jefe de corte podrá visualizar los cortes que se realizan por actividad |
          SELECT
              ad.id_actividad,
              ad.fecha_actividad,
              COUNT(c.id_corte) AS cantidad_cortes,
              op.cantidad AS cantidad_orden_preproduccion,
              (SUM(l.cantidad) / op.cantidad) * 100 AS progreso_preproduccion
          FROM actividad_diaria ad
          LEFT JOIN corte c ON ad.id_actividad = c.id_actividad
          LEFT JOIN lote l ON c.id_lote = l.id_lote
          LEFT JOIN dimension_corte dc ON l.id_dim_corte = dc.id_dim_corte
          LEFT JOIN orden_producción op ON dc.id_dim_corte = op.id_dim_corte
          LEFT JOIN dimension_prenda dp ON op.id_dim_prenda = dp.id_dim_prenda
          GROUP BY
              ad.id_actividad, ad.fecha_actividad, op.cantidad
          ORDER BY
              ad.fecha_actividad DESC;

####  2.7
| Código requerimiento | RV205 |
| --- | --- |
| Codigo interfaz |  IV207 |
| Imagen interfaz  |

![](../Entregable%201/Mockups%20-%20Figma/Corte/corte_v2/lotes_mes.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Detalle corte:** El jefe de corte podrá visualizar el numero de lotes por dia en el mes |
          SELECT 
              l.fecha_creacion::date AS dia,
              COUNT(l.id_lote) AS cantidad_lotes
          FROM 
              lote l
          JOIN 
              actividad_diaria ad ON l.id_actividad = ad.id_actividad
          JOIN 
              orden_producción op ON ad.id_orden_producción = op.id_orden_producción
          JOIN 
              area a ON op.id_area = a.id_area
          WHERE 
              a.nombre = 'Corte'  -- Suponiendo que el nombre del área de corte es 'Corte'
              AND DATE_TRUNC('month', l.fecha_creacion) = DATE_TRUNC('month', CURRENT_DATE)  -- Filtrar por el mes actual
          GROUP BY 
              l.fecha_creacion::date
          ORDER BY 
              dia DESC;

####  2.8
| Código requerimiento | RV206 |
| --- | --- |
| Codigo interfaz |  IV208|
| Imagen interfaz  |

![](../Entregable%201/Mockups%20-%20Figma/Corte/corte_v2/cortes_orden_produccion.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Detalle corte:** El jefe de corte podrá visualizar el numero de cortes por el orden de producción |
          SELECT
              op.id_orden_producción,
              op.cantidad,
              l.id_lote,
              l.cantidad AS cantidad_lote,
              t.nombre AS tipo_corte,
              COUNT(*) AS cantidad_cortes,
              e.nombre AS estado_orden,
              (SELECT
                  (SUM(l2.cantidad) / op.cantidad) * 100
              FROM lote l2
              INNER JOIN corte c2 ON l2.id_lote = c2.id_lote
              WHERE l2.id_orden_producción = op.id_orden_producción) AS progreso_produccion
          FROM orden_producción op
          INNER JOIN lote l ON op.id_orden_producción = l.id_orden_producción
          INNER JOIN corte c ON l.id_lote = c.id_lote
          INNER JOIN dimension_corte d ON c.id_dim_corte = d.id_dim_corte
          INNER JOIN tipo_corte t ON d.id_tipo_corte = t.id_tipo_corte
          INNER JOIN estado e ON op.estado = e.id_estado
          GROUP BY
              op.id_orden_producción,
              op.cantidad,
              l.id_lote,
              l.cantidad,
              t.nombre,
              e.nombre
          ORDER BY
              op.id_orden_producción,
              t.nombre,
              cantidad_cortes DESC;
          

### 3. Confección 
### 4. Almacén de tránsito 
### 5. Acabados
| Código Requerimiento    : RV001               | 
|-----------------------------------------------|
| **Código Interfaz**    : IV001        |
| **Imagen Interfaz** | 
|  ![IV001](../Entregable%203/Prototipos/acabados/caja-1.png)  | 
| **Sentencia SQL**   | 
| **Eventos:** |
```sql

-- 1. CARGA DE PÁGINA: Carga la página por defecto con los 50 primeros resultados
SELECT 
    cp.id_caja AS "ID Caja", 
    p.id_prenda AS "ID Prenda", 
    cp.cantidad AS "Cantidad", 
    cp.fecha_creacion AS "Fecha creación", 
    COALESCE(em.id_empleado::text, '-') AS "ID Operario", 
    CONCAT(em.nombre, ' ', em.primer_apellido, ' ', em.segundo_apellido) AS Operario
FROM 
    Caja_prenda cp
JOIN 
    Prenda p ON cp.id_caja = p.id_caja
JOIN 
    Empleado em ON p.id_empleado = em.id_empleado
LIMIT 50;



-- 2. BUSQUEDA POR CAJAS: Coloca ID de caja en la caja y hace click en el icono de lupa para busca,
-- luego aparece en la grilla la caja con sus atributos. 

SELECT 
    cp.id_caja AS "ID Caja", 
    p.id_prenda AS "ID Prenda", 
    cp.cantidad AS "Cantidad", 
    cp.fecha_creacion AS "Fecha creación", 
    COALESCE(em.id_empleado::text, '-') AS "ID Operario", 
    CONCAT(em.nombre, ' ', em.primer_apellido, ' ', em.segundo_apellido) AS Operario
FROM 
    Caja_prenda cp
JOIN 
    Prenda p ON cp.id_caja = p.id_caja
JOIN 
    Empleado em ON p.id_empleado = em.id_empleado
WHERE
    cp.id_caja = 30;

-- 3. ID Caja: se puede seleccionar el ID de caja que me lleva a otra pantalla
-- para el vistazo de detalle del mismo.

-- 4. OPERARIO: Se selecciona el ID Operario para ver el detalle del operario
-- a la prenda asignada.

```




| Código Requerimiento    : RV002               | 
|-----------------------------------------------|
| **Código Interfaz**    : IV002        |
| **Imagen Interfaz** | 
|   ![IV002](../Entregable%203/Prototipos/acabados/caja-2.png)   | 
| **Sentencia SQL**   | 
| **Eventos:** |
```sql

-- 1. ID caja: se resupera id de caja
SELECT
    cpren.id_caja
FROM
    Caja_prenda cpren;

-- 2. Fecha: se resupera fecha de creacion en carga de pagina
SELECT
    cpren.fecha_creacion
FROM
    Caja_prenda cpren;

-- 3.Cantidad: Se recupera cantidad de prendas por caja en carga de pagina.
SELECT
    cpren.cantidad
FROM
    Caja_prenda cpren;

-- 4. Prenda: se recupera en nombre de prenda en carga de pagina.
SELECT tipren.nombre
FROM Caja_prenda cpren
JOIN Prenda pren ON cpren.id_caja = pren.id_caja
JOIN Dimension_prenda dimpren ON pren.id_dim_prenda = dimpren.id_dim_prenda
JOIN Dimension_confeccion dimconf ON dimpren.id_dim_confeccion = dimpren.id_dim_confeccion
JOIN Tipo_prenda tipren ON dimconf.id_tipo_prenda = tipren.id_tipo_prenda


-- 5. Grilla de detalle: se recupera los datos generales de prendas sus acabados en la grilla en la carga de pagina.

SELECT
    dimconf.id_dim_confeccion,
    COALESCE(dimconf.medida_logitud, ' ') AS ml,
    COALESCE(dimconf.medida_hombro, ' ') AS mh,
    COALESCE(dimconf.medida_pecho, ' ') AS mp,
    COALESCE(dimconf.medida_manga, ' ') AS mm, C
    OALESCE(dimconf.medida_cintura, ' ') AS mc, C
    OALESCE(dimconf.medida_cadera, ' ') AS mca,
    COALESCE(dimconf.medida_muslo, ' ') AS mmu,
    estpren.nombre AS "Estilo prenda",
    ta.nombre AS "Talla", ge.nombre AS "Género",
    aca.nombre AS "Acabados"
FROM
    Orden_produccion ordpro
JOIN Dim_prenda_detalle dprende ON ordpro.id_dim_prenda = dprende.id_dim_prenda
JOIN Acabado aca ON dprende.id_acabado = aca.id_acabado
JOIN Dimension_confeccion dimconf ON ordpro.id_dim_confeccion = dimconf.id_dim_confeccion
JOIN Estilo_prenda estpren ON dimconf.id_estilo_prenda = estpren.id_estilo_prenda
JOIN Talla ta ON dimconf.id_talla = ta.id_talla
JOIN Genero ge ON dimconf.id_genero = ge.id_genero

```


| Código Requerimiento    : RV003               | 
|-----------------------------------------------|
| **Código Interfaz**    : IV003        |
| **Imagen Interfaz** | 
|   ![IV003](../Entregable%203/Prototipos/acabados/caja-3.png)  | 
| **Sentencia SQL**   | 
| **Eventos:** |
```sql
-- 1. Fechas: Seleccionar fecha inicio y fin para reporte.

-- 2. Reporte: Presentar los datos con el periodo brindado con el botón 'Buscar'.



```


| Código Requerimiento    : RV004               | 
|-----------------------------------------------|
| **Código Interfaz**    : IV003        |
| **Imagen Interfaz** | 
|  ![IV003](../Entregable%203/Prototipos/acabados/caja-3.png)   | 
| **Sentencia SQL**   | 
| **Eventos:** |
```sql
-- 3. Imprimir: Realizar impresión de reporte del periodo seleccionado en pdf con el botón 'Imprimir'.
```

| Código Requerimiento    : RV001               | 
|-----------------------------------------------|
| **Código Interfaz**    : IV004        |
| **Imagen Interfaz** | 
| ![IV004](../Entregable%203/Prototipos/acabados/caja-4.png)    | 
| **Sentencia SQL**   | 
| **Eventos:** |
```sql
--1. Carga Operario: Ver datos básico del Operario en un popup.
SELECT CONCAT(em.nombre,' ',em.primer_apellido,' ',em.segundo_apellido) AS Nombres, em.id_empleado AS ID, em.dni AS DNI, capren.cantidad AS "Cantidad prenda"
FROM Prenda pren
JOIN Empleado em ON prend.id_empleado = em.id_empleado
JOIN Caja_prenda capren ON prend.id_caja = capren.id_caja

```
| Código Requerimiento    : RV005               | 
|-----------------------------------------------|
| **Código Interfaz**    : IV005        |
| **Imagen Interfaz** | 
|  ![IV005](../Entregable%203/Prototipos/acabados/acabado-.png)   | 
| **Sentencia SQL**   | 
| **Eventos:** |
```sql
-- 1. OPERARIO: Buscar por operario según su ID
SELECT
    em.id_empleado
FROM
    Empleado em;


-- 2. Nombres: Recuperar nombres de empleado
SELECT
    CONCAT(em.nombre,' ',em.primer_apellido,' ',em.segundo_apellido)
FROM
    Empleado em;
WHERE em.id_empleado = <1>

-- 3. Correo: Recuperar correo de empleado
SELECT
    em.correo
FROM
    Empleado em;
WHERE em.id_empleado = <1>

-- 4. GRILLA: Mostrar las cajas asignadas al operario y sus datos básicos.
SELECT
    
FROM
    Prenda pre
JOIN Dim_prenda_detalle dprende ON ordpro.id_dim_prenda = dprende.id_dim_prenda
JOIN Acabado aca ON dprende.id_acabado = aca.id_acabado
JOIN Dimension_confeccion dimconf ON ordpro.id_dim_confeccion = dimconf.id_dim_confeccion
JOIN Estilo_prenda estpren ON dimconf.id_estilo_prenda = estpren.id_estilo_prenda
JOIN Talla ta ON dimconf.id_talla = ta.id_talla

```

### 6. Calidad

####  6.1
| Código requerimiento | RV601 |
| --- | --- |
| Codigo interfaz |  IV601 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/calidad/Registrar%20Solicitudes%20de%20Inspeccion.png)
| Sentencias SQL |
| Eventos |
| **1. Botón “Registrar”: Cuando el usuario presione el botón “registrar” se registrará una Inspección de calidad |

          INSERT INTO INSPECCION_CALIDAD(ID_INSPECCION,
          FECHA_INSPECCION,
          ESTADO,
          CANTIDAD_DEFECTUOSOS,
          ID_LOTE,
          ID_AQL_LOTE_RANGO,
          ID_AQL_NIVEL,
          ID_AQL_CODIGO,
          ID_AQL_SIGNIFICANCIA,
          ID_DESCRIPCION,
          ID_RESULTADO)
          VALUES(<4>, <3>,'SOLICITADO',0,<1>,<2>,<6>,<7>,<5>,NULL,NULL);
              
####  6.2
| Código requerimiento | RV602 |
| --- | --- |
| Codigo interfaz | IV602 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/calidad/Registrar%20datos%20de%20Inspeccion.png)
| Sentencias SQL |
| Eventos |
| **1. Botón Buscar Inspección: Cuando el usuario presione el botón “buscar” se buscará las inspecciones de calidad |

          SELECT
          I.ID_INSPECCION,
          I.ID_LOTE,
          I.FECHA_INSPECCION,
          I.ID_AQL_LOTE_RANGO,
          I.CANTIDAD_DEFECTUOSOS,
          I.ID_AQL_CODIGO,
          I.ID_AQL_NIVEL,
          I.ID_AQL_SIGNIFICANCIA,
          I.ESTADO,
          I.ID_RESULTADO
          FROM INSPECCION_CALIDAD I
          WHERE I.ID_INSPECCION = <1>
          AND I.ID_LOTE = <2>
          AND I.FECHA_INSPECCION = <3>
          GROUP BY I.ID_INSPECCION;

####  6.3
| Código requerimiento | RV603 |
| --- | --- |
| Codigo interfaz |  IV603 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/calidad/Revisar%20Inspecciones.png)
| Sentencias SQL |
| Eventos |
| **1. Botón “Registrar datos de Inspección”: Cuando el usuario presione el botón se actualizará la inspección seleccionada previamente |

          UPDATE INSPECCION_CALIDAD SET
          CANTIDAD_DEFECTUOSOS = <2>,
          DESCRIPCION = <3>,
          RESULTADO = <4>
          ESTADO = 'INSPECCIONADO'
          WHERE ID_INSPECCION = <1>;

### 7. PCP 

**[Ir a la seccion 4](4-carga-datos.md)**

***[Regresar al índice](./entregable%203-indice.md)***
