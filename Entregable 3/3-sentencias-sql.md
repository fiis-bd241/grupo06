# Entregable 3 del proyecto
## Sentencias SQL
### 1. Almacén central
####  1.1
| Código requerimiento | RV101 |
| --- | --- |
| Codigo interfaz |  IV101 |
| Imagen interfaz  |

interfaz
| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes que están en un estado específico, junto con la información del proveedor, la materia prima, el espacio en el que se encuentra y la fecha de entrada. |
          SELECT    
                    l.estado, 
                    p.denominacion_social,
                    mp.id_materia_prima,
                    e.id_espacio,
                    le.fecha_entrada
          FROM lote l
          JOIN materia_prima mp ON l.id_lote = mp.id_lote
          JOIN proveedor p ON mp.id_proveedor = p.id_proveedor
          JOIN espacio e ON l.id_lote = e.id_lote
          JOIN lote_entrada le ON l.id_lote = le.id_lote
          WHERE l.estado = 'En almacen';

####  1.2
| Código requerimiento | RV102 |
| --- | --- |
| Codigo interfaz |  IV102 |
| Imagen interfaz  |

interfaz
| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes que han entrado en el almacén entre dos fechas específicas junto con la información del espacio, la estantería, el proveedor y la materia prima. |
         CREATE OR REPLACE FUNCTION get_lotes_entre_fechas(fecha_inicio DATE, fecha_fin DATE DEFAULT NULL)
          RETURNS TABLE (
              fecha_entrada DATE,
              id_lote INT,
              id_estanteria NUMERIC,
              id_espacio NUMERIC,
              denominacion_social VARCHAR,
              id_materia_prima INT
          ) AS $$
          BEGIN
              IF fecha_fin IS NULL THEN
                  fecha_fin := CURRENT_DATE;
              END IF;

              RETURN QUERY
              SELECT 
              DATE(le.fecha_entrada), 
              l.id_lote, 
              e.id_estanteria, 
              es.id_espacio, 
              p.denominacion_social, 
              mp.id_materia_prima
              FROM lote_entrada le
              JOIN lote l ON le.id_lote = l.id_lote
              JOIN espacio es ON l.id_lote = es.id_lote
              JOIN estanteria e ON es.id_estanteria = e.id_estanteria
              JOIN materia_prima mp ON l.id_lote = mp.id_lote
              JOIN proveedor p ON mp.id_proveedor = p.id_proveedor
              WHERE le.fecha_entrada >= fecha_inicio AND le.fecha_entrada < fecha_fin + INTERVAL '1 day';
          END; $$ LANGUAGE plpgsql;

          Opciones de llamado:
          SELECT * FROM get_lotes_entre_fechas('2022-01-01');
          SELECT * FROM get_lotes_entre_fechas('2022-01-01', '2022-02-01');

####  1.3
| Código requerimiento | RV103 |
| --- | --- |
| Codigo interfaz |  IV103 |
| Imagen interfaz  |

interfaz
| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes que están en un pasillo específico, junto con la información de la zona, el área, el proveedor y la materia prima. |
          SELECT 
          l.id_lote, 
          z.nombre as nombre_zona, 
          a.nombre as nombre_area, 
          p.denominacion_social, 
          mp.id_materia_prima
          FROM pasillo p
          JOIN estanteria e ON p.id_pasillo = e.id_pasillo
          JOIN espacio es ON e.id_estanteria = es.id_estanteria
          JOIN lote l ON es.id_lote = l.id_lote
          JOIN materia_prima mp ON l.id_lote = mp.id_lote
          JOIN proveedor p ON mp.id_proveedor = p.id_proveedor
          JOIN zona z ON p.id_zona = z.id_zona
          JOIN area a ON z.id_area = a.id_area;

####  1.4
| Código requerimiento | RV104 |
| --- | --- |
| Codigo interfaz |  IV104 |
| Imagen interfaz  |

interfaz
| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes que están asociados a una actividad específica, junto con la información del proveedor y la materia prima correspondiente. |
         SELECT 
         a.id_actividad, 
         COUNT(l.id_lote) as cantidad_lotes, 
         p.denominacion_social, 
         mp.id_materia_prima
          FROM actividad_diaria a
          JOIN lote l ON a.id_actividad = l.id_actividad
          JOIN materia_prima mp ON l.id_lote = mp.id_lote
          JOIN proveedor p ON mp.id_proveedor = p.id_proveedor
          GROUP BY a.id_actividad, p.denominacion_social, mp.id_materia_prima; 

####  1.5
| Código requerimiento | RV105 |
| --- | --- |
| Codigo interfaz |  IV105 |
| Imagen interfaz  |

interfaz
| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes que están en un estado específico, junto con la información del proveedor y la materia prima correspondiente. |
          SELECT 
          l.estado, 
          COUNT(l.id_lote) as cantidad_lotes, 
          p.denominacion_social, 
          mp.id_materia_prima
          FROM lote l
          JOIN materia_prima mp ON l.id_lote = mp.id_lote
          JOIN proveedor p ON mp.id_proveedor = p.id_proveedor
          GROUP BY l.estado, p.denominacion_social, mp.id_materia_prima;

####  1.6
| Código requerimiento | RV106 |
| --- | --- |
| Codigo interfaz |  IV106 |
| Imagen interfaz  |

interfaz
| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes que han entrado en el almacén en una fecha específica. |
          SELECT 
          le.fecha_entrada, 
          l.id_lote
          FROM lote_entrada le
          JOIN lote l ON le.id_lote = l.id_lote
          WHERE le.fecha_entrada = '2022-01-01';

####  1.7
| Código requerimiento | RV107 |
| --- | --- |
| Codigo interfaz |  IV107 |
| Imagen interfaz  |

interfaz
| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes que han salido del almacén en una fecha específica. |
          SELECT 
          ls.fecha_salida, 
          l.id_lote
          FROM lote_salida ls
          JOIN lote l ON ls.id_lote = l.id_lote
          WHERE ls.fecha_salida = '2022-01-01';
          
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
|**INSERT INTO lote (id_tipo_lote, cantidad, id_dim_corte, id_dim_confeccion, id_dim_materia_prima, id_actividad, fecha_creacion) VALUES (<1>, <2>, <3>, NULL, NULL, <4>, <6>);**|
|**INSERT INTO Registro_uso_lote (id_actividad, id_lote, cantidad_usada) VALUES (<5>, <7>, <8>);**|

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
          JOIN orden_producción op ON ad.id_orden_producción = op.id_orden_producción
          JOIN lote l ON ad.id_actividad = l.id_actividad
          JOIN corte c ON l.id_lote = c.id_lote
          GROUP BY
              ad.id_actividad,
              ad.fecha_actividad,
              op.cantidad
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
| Código requerimiento | RV401 |
| --- | --- |
| Codigo interfaz |  IV401 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/transito/1.0%20-%20Recepcion%20Lote.PNG)

| Sentencias SQL |
| --- |
| Eventos |







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
| Código Requerimiento    : RV006              | 
|-----------------------------------------------|
| **Código Interfaz**    : IV006        |
| **Imagen Interfaz** | 
|  ![IV006](../Entregable%203/Prototipos/acabados/acabado-4.png)   | 
|  ![IV006](../Entregable%203/Prototipos/acabados/acabado-5.png)   | 
| **Sentencia SQL**   | 
| **Eventos:** |
```sql
-- 1. OPERARIO: recurpera ID del operario según la caja carga de pagina
SELECT
    em.id_empleado
FROM
    Empleado em, Caja_prenda capren
WHERE caprend.id_empleado = em_id_empleado
AND capren.id_caja = <4>;

-- 2. NOMBRE: recupera nombre del operario en carga de pagina
SELECT
    CONCAT(em.nombre,' ',em.primer_apellido,' ',em.segundo_apellido) AS nombreOpe 
FROM
    Empleado em, Caja_prenda capren
WHERE caprend.id_empleado = em_id_empleado
AND em.id_empleado = <1>;

-- 3, CORREO: recuperar correo de operario en carga de pagina.
SELECT
    em.correo
FROM
    Empleado em, Caja_prenda capren
WHERE caprend.id_empleado = em_id_empleado
AND em.id_empleado = <1>;

-- 4. ID CAJA:
SELECT
    id_caja
FROM
    Caja_prenda;

-- 5. GRILLA: Datos generales de la caja

SELECT tipren.nombre AS Prenda, dimconf.id_dim_confeccion AS IDconfeccion,
          COALESCE(gconf.medida_longitud AS ml,' '),
          COALESCE(gconf.medida_hombro AS mh,' '),
          COALESCE(gconf.medida_pecho AS mp,' '),
          COALESCE(gconf.medida_manga AS mma,' '),
          COALESCE(gconf.medida_cintura AS mci,' '),
          COALESCE(gconf.medida_cadera AS mca,' '),
          COALESCE(gconf.medida_muslo AS mmu,' '),
          espren.mombre AS estilo, ta.nombre AS Talla, ge.nombre AS Género, est.nombre AS Estado
FROM Caja_prenda cpren
JOIN Prenda pren ON cpren.id_caja = pren.id_caja
JOIN Dimension_prenda dimpren ON pren.id_dim_prenda = dimpren.id_dim_prenda
JOIN Dimension_confeccion dimconf ON dimpren.id_dim_confeccion = dimpren.id_dim_confeccion
JOIN Guia_confeccion gconf ON dimconf.id_guia_confeccion = gconf.id_guia_confeccion
JOIN Tipo_prenda tipren ON dimconf.id_tipo_prenda = tipren.id_tipo_prenda
JOIN Estilo_prenda espren ON dimconf.id_estilo_prenda = espren.id_estilo_prenda
JOIN Talla ta ON dimconf.id_talla = ta.id_talla
JOIN Genero ge ON dimconf.id_genero = ge.id_genero
JOIN Estado est ON cpren.id_estado = est.id_estado
WHERE cpren.id_caja =  <4>


-- 6. ACABADOS: Carga la grilla de acbados por orden de produccion y
--caja de entrada, aqui se ingresa su caja de salida.
--Planchado
SELECT acab.nombre, acd.id_Actividad, acd.fecha_actividad, capre.id_caja AS Caja, COALESCE(casa.id_salida,' ') AS Salida
FROM Prenda pre
Caja_prenda capre ON pre.id_caja = capre.id_caja
JOIN Dimension_prenda_detalle dprende ON pre.id_dim_prenda = dprende.id_dim_prenda
JOIN Acabado acab ON dprende.id_acabado = acab.id_acabado
JOIN Empleado em ON pre.id_empleado = em.id_empleado
JOIN Empleado_actividad emac ON em.id_empleado = emac.id_empleado
JOIN Actividad_diaria acd ON emac.id_actividad = acd.id_actividad
JOIN Registro_transformación_caja retca ON acd.id_actividad = retca.id_actividad
JOIN Caja_lote calo ON retca.id_caja = calo.id_caja
JOIN Caja_salida casa ON calo.id_caja = casa.id_caja
WHERE capre.id_caja = <4>
AND aca.nombre = "Planchado"


--Hangteado
SELECT acab.nombre, acd.id_Actividad, acd.fecha_actividad, capre.id_caja AS Caja, COALESCE(casa.id_salida,' ') AS Salida
FROM Prenda pre
Caja_prenda capre ON pre.id_caja = capre.id_caja
JOIN Dimension_prenda_detalle dprende ON pre.id_dim_prenda = dprende.id_dim_prenda
JOIN Acabado acab ON dprende.id_acabado = acab.id_acabado
JOIN Empleado em ON pre.id_empleado = em.id_empleado
JOIN Empleado_actividad emac ON em.id_empleado = emac.id_empleado
JOIN Actividad_diaria acd ON emac.id_actividad = acd.id_actividad
JOIN Registro_transformación_caja retca ON acd.id_actividad = retca.id_actividad
JOIN Caja_lote calo ON retca.id_caja = calo.id_caja
JOIN Caja_salida casa ON calo.id_caja = casa.id_caja
WHERE capre.id_caja = <4>
AND aca.nombre = "Hangteado"

-- Embalaje
SELECT acab.nombre, acd.id_Actividad, acd.fecha_actividad, capre.id_caja AS Caja, COALESCE(casa.id_salida,' ') AS Salida
FROM Prenda pre
Caja_prenda capre ON pre.id_caja = capre.id_caja
JOIN Dimension_prenda_detalle dprende ON pre.id_dim_prenda = dprende.id_dim_prenda
JOIN Acabado acab ON dprende.id_acabado = acab.id_acabado
JOIN Empleado em ON pre.id_empleado = em.id_empleado
JOIN Empleado_actividad emac ON em.id_empleado = emac.id_empleado
JOIN Actividad_diaria acd ON emac.id_actividad = acd.id_actividad
JOIN Registro_transformación_caja retca ON acd.id_actividad = retca.id_actividad
JOIN Caja_lote calo ON retca.id_caja = calo.id_caja
JOIN Caja_salida casa ON calo.id_caja = casa.id_caja
WHERE capre.id_caja = <4>
AND aca.nombre = "Embalaje"

-- Empaquetado
SELECT acab.nombre, acd.id_Actividad, acd.fecha_actividad, capre.id_caja AS Caja, COALESCE(casa.id_salida,' ') AS Salida
FROM Prenda pre
Caja_prenda capre ON pre.id_caja = capre.id_caja
JOIN Dimension_prenda_detalle dprende ON pre.id_dim_prenda = dprende.id_dim_prenda
JOIN Acabado acab ON dprende.id_acabado = acab.id_acabado
JOIN Empleado em ON pre.id_empleado = em.id_empleado
JOIN Empleado_actividad emac ON em.id_empleado = emac.id_empleado
JOIN Actividad_diaria acd ON emac.id_actividad = acd.id_actividad
JOIN Registro_transformación_caja retca ON acd.id_actividad = retca.id_actividad
JOIN Caja_lote calo ON retca.id_caja = calo.id_caja
JOIN Caja_salida casa ON calo.id_caja = casa.id_caja
WHERE capre.id_caja = <4>
AND aca.nombre = "Embalaje"

-- ASIGNAR EN PLANCHADO:
INSERT INTO Caja_salida (id_salida, fecha_salida, id_caja, id_area)
SELECT
    <1>,  -- Reemplaza esto con el valor que deseas insertar en id_salida
    CURRENT_DATE,          -- Fecha actual
    capre.id_caja,         -- id_caja obtenido de la consulta
    5                      -- id_area fijo como 5
FROM Prenda pre
JOIN Caja_prenda capre ON pre.id_caja = capre.id_caja
JOIN Dimension_prenda_detalle dprende ON pre.id_dim_prenda = dprende.id_dim_prenda
JOIN Acabado acab ON dprende.id_acabado = acab.id_acabado
JOIN Empleado em ON pre.id_empleado = em.id_empleado
JOIN Empleado_actividad emac ON em.id_empleado = emac.id_empleado
JOIN Actividad_diaria acd ON emac.id_actividad = acd.id_actividad
JOIN Registro_transformación_caja retca ON acd.id_actividad = retca.id_actividad
JOIN Caja_lote calo ON retca.id_caja = calo.id_caja
JOIN Caja_salida casa ON calo.id_caja = casa.id_caja
WHERE capre.id_caja = 4
AND acab.nombre = 'Planchado';

-- ASIGNAR EN HANGTEADO:
INSERT INTO Caja_salida (id_salida, fecha_salida, id_caja, id_area)
SELECT
    <1>,  -- Reemplaza esto con el valor que deseas insertar en id_salida
    CURRENT_DATE,          -- Fecha actual
    capre.id_caja,         -- id_caja obtenido de la consulta
    5                      -- id_area fijo como 5
FROM Prenda pre
JOIN Caja_prenda capre ON pre.id_caja = capre.id_caja
JOIN Dimension_prenda_detalle dprende ON pre.id_dim_prenda = dprende.id_dim_prenda
JOIN Acabado acab ON dprende.id_acabado = acab.id_acabado
JOIN Empleado em ON pre.id_empleado = em.id_empleado
JOIN Empleado_actividad emac ON em.id_empleado = emac.id_empleado
JOIN Actividad_diaria acd ON emac.id_actividad = acd.id_actividad
JOIN Registro_transformación_caja retca ON acd.id_actividad = retca.id_actividad
JOIN Caja_lote calo ON retca.id_caja = calo.id_caja
JOIN Caja_salida casa ON calo.id_caja = casa.id_caja
WHERE capre.id_caja = 4
AND acab.nombre = 'Hangteado';

-- ASIGNAR EN EMBALAJE:
INSERT INTO Caja_salida (id_salida, fecha_salida, id_caja, id_area)
SELECT
    <1>,  -- Reemplaza esto con el valor que deseas insertar en id_salida
    CURRENT_DATE,          -- Fecha actual
    capre.id_caja,         -- id_caja obtenido de la consulta
    5                      -- id_area fijo como 5
FROM Prenda pre
JOIN Caja_prenda capre ON pre.id_caja = capre.id_caja
JOIN Dimension_prenda_detalle dprende ON pre.id_dim_prenda = dprende.id_dim_prenda
JOIN Acabado acab ON dprende.id_acabado = acab.id_acabado
JOIN Empleado em ON pre.id_empleado = em.id_empleado
JOIN Empleado_actividad emac ON em.id_empleado = emac.id_empleado
JOIN Actividad_diaria acd ON emac.id_actividad = acd.id_actividad
JOIN Registro_transformación_caja retca ON acd.id_actividad = retca.id_actividad
JOIN Caja_lote calo ON retca.id_caja = calo.id_caja
JOIN Caja_salida casa ON calo.id_caja = casa.id_caja
WHERE capre.id_caja = 4
AND acab.nombre = 'Embalaje';

-- ASIGNAR EN EMPAQUETADO:
INSERT INTO Caja_salida (id_salida, fecha_salida, id_caja, id_area)
SELECT
    <1>,  -- Reemplaza esto con el valor que deseas insertar en id_salida
    CURRENT_DATE,          -- Fecha actual
    capre.id_caja,         -- id_caja obtenido de la consulta
    5                      -- id_area fijo como 5
FROM Prenda pre
JOIN Caja_prenda capre ON pre.id_caja = capre.id_caja
JOIN Dimension_prenda_detalle dprende ON pre.id_dim_prenda = dprende.id_dim_prenda
JOIN Acabado acab ON dprende.id_acabado = acab.id_acabado
JOIN Empleado em ON pre.id_empleado = em.id_empleado
JOIN Empleado_actividad emac ON em.id_empleado = emac.id_empleado
JOIN Actividad_diaria acd ON emac.id_actividad = acd.id_actividad
JOIN Registro_transformación_caja retca ON acd.id_actividad = retca.id_actividad
JOIN Caja_lote calo ON retca.id_caja = calo.id_caja
JOIN Caja_salida casa ON calo.id_caja = casa.id_caja
WHERE capre.id_caja = 4
AND acab.nombre = 'Empaquetado';


-- 7. GUARDAR CAMBIOS: Se realiza click en guardar cambios para guardar
-- las modificaciones en Acabados y volver pantalla incial del modulo
-- acabados/acabados



--
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
