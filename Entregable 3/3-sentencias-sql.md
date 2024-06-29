# Entregable 3 del proyecto
## Sentencias SQL
### 1. Almacén central
####  1.1
| Código requerimiento | RV101 |
| --- | --- |
| Codigo interfaz |  IV101 |
| Imagen interfaz | ![](../Entregable%201/Mockups%20-%20Figma/almacen-central/consulta1.png)  |

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes que están en un estado y material específico, junto con el nombre del proveedor, la materia prima y la fecha de entrada. |
          SELECT
              l.id_lote,
              p.denominacion_social,
              e.id_espacio,
              le.fecha_entrada,
              tmp.nombre as tipo_materia_prima
          FROM lote l
          JOIN materia_prima mp ON l.id_lote = mp.id_lote
          JOIN proveedor p on mp.id_proveedor = p.id_proveedor
          JOIN espacio e on l.id_lote = e.id_lote
          JOIN lote_entrada le on l.id_lote = le.id_lote
          JOIN estado e2 on l.id_estado = e2.id_estado
          JOIN dimension_materia_prima dmp on mp.id_dim_materia_prima = dmp.id_dim_materia_prima
          JOIN tipo_materia_prima tmp ON dmp.id_tipo_materia_prima =tmp.id_tipo_materia_prima
          WHERE e2.nombre = 'Disponible' AND tmp.nombre = 'Jersey';

####  1.2
| Código requerimiento | RV102 |
| --- | --- |
| Codigo interfaz |  IV102 |
| Imagen interfaz |  ![](../Entregable%201/Mockups%20-%20Figma/almacen-central/consulta2.png)  |

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
| Imagen interfaz |  ![](../Entregable%201/Mockups%20-%20Figma/almacen-central/consulta3v2.png)  |

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes correspondientes a un proveedor específico, agrupados por materia prima y mostrando la cantidad de cada uno. |
          SELECT 
              tmp.nombre AS materia_prima,
              p.denominacion_social AS proveedor,
              COUNT(*) AS cantidad_lotes
          FROM 
              proveedor p
          JOIN materia_prima mp ON p.id_proveedor = mp.id_proveedor
          join lote l ON mp.id_lote = l.id_lote
          JOIN dimension_materia_prima dmp on mp.id_dim_materia_prima = dmp.id_dim_materia_prima
          JOIN tipo_materia_prima tmp ON dmp.id_tipo_materia_prima =tmp.id_tipo_materia_prima
          WHERE 
              l.id_estado = 12 AND
              p.denominacion_social = 'Serna y Cabanillas S.Com.' and 
              tmp.nombre = 'Full Lycra'
          GROUP BY 
              tmp.nombre, 
              p.denominacion_social;
              
####  1.4
| Código requerimiento | RV104 |
| --- | --- |
| Codigo interfaz |  IV104 |
| Imagen interfaz |  ![](../Entregable%201/Mockups%20-%20Figma/almacen-central/consulta6v2.png)  |

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes que han entrado en el almacén en una fecha específica. |
          SELECT
              le.fecha_entrada,
              l.id_lote,
              tmp.nombre AS nombre_material,
              p.denominacion_social AS nombre_proveedor,
              l.cantidad
          FROM
              lote_entrada le
          JOIN
              lote l ON le.id_lote = l.id_lote
          JOIN
              materia_prima mp ON l.id_lote = mp.id_lote
          JOIN
              dimension_materia_prima dmp ON mp.id_dim_materia_prima = dmp.id_dim_materia_prima
          JOIN
              tipo_materia_prima tmp ON dmp.id_tipo_materia_prima = tmp.id_tipo_materia_prima
          JOIN
              proveedor p ON mp.id_proveedor = p.id_proveedor
          WHERE
              DATE(le.fecha_entrada) = DATE('2024-06-25') AND
              tmp.nombre = 'Full Lycra' and 
              p.denominacion_social = 'Fábrica Españolas S.C.P'

####  1.5
| Código requerimiento | RV105 |
| --- | --- |
| Codigo interfaz |  IV105 |
| Imagen interfaz |  ![](../Entregable%201/Mockups%20-%20Figma/almacen-central/consulta7v2.png)  |

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Buscar:** Consulta de todos los lotes que han salido del almacén en una fecha específica. |
          SELECT
              ls.fecha_salida,
              l.id_lote,
              tmp.nombre AS nombre_material,
              p.denominacion_social AS nombre_proveedor,
              l.cantidad,
              a.nombre AS nombre_area
          FROM
              lote_salida ls
          JOIN
              lote l ON ls.id_lote = l.id_lote
          JOIN
              materia_prima mp ON l.id_lote = mp.id_lote
          JOIN
              dimension_materia_prima dmp ON mp.id_dim_materia_prima = dmp.id_dim_materia_prima
          JOIN
              tipo_materia_prima tmp ON dmp.id_tipo_materia_prima = tmp.id_tipo_materia_prima
          JOIN
              proveedor p ON mp.id_proveedor = p.id_proveedor
          JOIN
              area a ON ls.area_envio = a.id_area
          WHERE
              DATE(ls.fecha_salida) = DATE('2024-03-03') AND
              tmp.nombre = 'French Terry' and 
              p.denominacion_social = 'Restauración TG S.Coop.';

####  1.6
| Código requerimiento | RV106 |
| --- | --- |
| Codigo interfaz |  IV106 |
| Imagen interfaz |  ![](../Entregable%201/Mockups%20-%20Figma/almacen-central/Agregar%20proveedor.png)  |

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Agregar:** Agrega a un nuevo proveedor tras obtener los campos necesarios. |
        CREATE OR REPLACE PROCEDURE crear_o_actualizar_proveedor(
              _descripcion_direccion VARCHAR(100),
              _direccion_correo VARCHAR(100),
              _numero_telefono VARCHAR(30),
              _ruc NUMERIC(11),
              _denominacion_social VARCHAR(100)
          )
          AS $$
          DECLARE
              _id_direccion INT;
              _id_correo INT;
              _id_telefono INT;
              _id_proveedor INT;
          BEGIN
              -- Buscar si el proveedor ya existe
              SELECT id_proveedor INTO _id_proveedor FROM proveedor WHERE ruc = _ruc;

              -- Si el proveedor existe, actualizar los datos
              IF _id_proveedor IS NOT NULL THEN
                  UPDATE proveedor SET denominacion_social = _denominacion_social WHERE id_proveedor = _id_proveedor;
                  UPDATE direccion SET descripcion = _descripcion_direccion WHERE id_direccion = (SELECT                               id_direccion FROM proveedor WHERE id_proveedor = _id_proveedor);
                  UPDATE correo SET direccion_correo = _direccion_correo WHERE id_correo = (SELECT id_correo FROM                     proveedor WHERE id_proveedor = _id_proveedor);
                    UPDATE telefono SET numero = _numero_telefono WHERE id_telefono = (SELECT id_telefono FROM                     proveedor WHERE id_proveedor = _id_proveedor);
              ELSE
                  -- Si el proveedor no existe, insertar un nuevo proveedor
                  INSERT INTO direccion (descripcion)
                  VALUES (_descripcion_direccion)
                  RETURNING id_direccion INTO _id_direccion;

                  INSERT INTO correo (direccion_correo)
                  VALUES (_direccion_correo)
                  RETURNING id_correo INTO _id_correo;

                  INSERT INTO telefono (numero)
                  VALUES (_numero_telefono)
                  RETURNING id_telefono INTO _id_telefono;

                  INSERT INTO proveedor (ruc, denominacion_social, id_direccion, id_telefono, id_correo)
                  VALUES (_ruc, _denominacion_social, _id_direccion, _id_telefono, _id_correo);
              END IF;
          END;
          $$ LANGUAGE plpgsql;
          
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
              e.nombre AS estado_orden,
              a.nombre AS area,
              tc.nombre AS tipo_corte,
              tmp.nombre AS tipo_materia_prima,
              o.id_orden_trabajo,
              o.fecha_creacion
          FROM
              orden_producción o
          JOIN
              estado e ON o.id_estado = e.id_estado
          JOIN
              area a ON o.id_area = a.id_area
          JOIN
              dimension_corte dc ON o.id_dim_corte = dc.id_dim_corte
          JOIN
              parte_corte_detalle pcd ON dc.id_dim_parte_prenda = pcd.id_dim_parte_prenda
          JOIN
              tipo_corte tc ON pcd.id_tipo_corte = tc.id_tipo_corte
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
              o.id_orden_producción, o.fecha_inicio, o.fecha_fin, o.cantidad, e.nombre, a.nombre, tc.nombre, tmp.nombre,       
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
              tc.nombre AS tipo_corte
          FROM actividad_diaria a
          JOIN maquina_actividad ma ON a.id_actividad = ma.id_actividad
          JOIN maquina m ON ma.id_maquina = m.id_maquina
          JOIN orden_producción o ON a.id_orden_producción = o.id_orden_producción
          JOIN corte c ON c.id_lote = o.id_dim_corte  -- Ajuste en esta línea para relacionar correctamente
          JOIN dimension_corte dc ON c.id_dim_corte = dc.id_dim_corte
          JOIN parte_corte_detalle pcd ON dc.id_dim_parte_prenda = pcd.id_dim_parte_prenda
          JOIN tipo_corte tc ON pcd.id_tipo_corte = tc.id_tipo_corte
          ORDER BY a.fecha_actividad DESC;

####  2.4
| Código requerimiento | RV208 |
| --- | --- |
| Codigo interfaz |  IV204 |
| Imagen interfaz  |

![](../Entregable%201/Mockups%20-%20Figma/Corte/corte_v2/operario_corte2.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Operaio corte:** El oprario insertara los valores del corte que se realizaxo y la cantidad de lote usado |
|**INSERT INTO lote (id_tipo_lote, cantidad, id_dim_corte, id_estado, id_dim_confeccion, id_dim_materia_prima, id_actividad, fecha_creacion) VALUES (<1>, <2>, <3>, <4>, NULL, NULL, <5>, <6>); -- se coloca en id_tipo_lote el 2, porque el 2 es para el área de corte**|
|**INSERT INTO Registro_uso_lote (id_actividad, id_lote, cantidad_usada) VALUES (NULL, <7>, <8>);**|

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
          GROUP BY 
              ma.id_maquina, m.capacidad_total, ad.fecha_actividad
          ORDER BY 
              fecha_actividad DESC;  -- Ordenar la cantidad de actividades de forma descendente

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
              tc.nombre AS tipo_corte,
              COUNT(c.id_corte) AS cantidad_cortes,
              e.nombre AS estado_orden,
              (SELECT
                  (SUM(l2.cantidad) / op.cantidad) * 100
               FROM lote l2
               INNER JOIN corte c2 ON l2.id_lote = c2.id_lote
               INNER JOIN orden_producción op2 ON op2.id_dim_corte = c2.id_dim_corte
               WHERE op2.id_orden_producción = op.id_orden_producción) AS progreso_produccion
          FROM orden_producción op
          INNER JOIN estado e ON op.id_estado = e.id_estado
          INNER JOIN dimension_corte dc ON op.id_dim_corte = dc.id_dim_corte
          INNER JOIN corte c ON dc.id_dim_corte = c.id_dim_corte
          INNER JOIN lote l ON c.id_lote = l.id_lote
          INNER JOIN parte_corte_detalle pcd ON dc.id_dim_parte_prenda = pcd.id_dim_parte_prenda
          INNER JOIN tipo_corte tc ON pcd.id_tipo_corte = tc.id_tipo_corte
          GROUP BY
              op.id_orden_producción,
              op.cantidad,
              l.id_lote,
              l.cantidad,
              tc.nombre,
              e.nombre
          ORDER BY
              op.id_orden_producción,
              tc.nombre,
              cantidad_cortes DESC;

### 3. Confección 
### 4. Almacén de tránsito 
| Código requerimiento | RV401 |
| --- | --- |
| Codigo interfaz |  IV401 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/transito/1.1%20-%20Buscar%20OT.PNG)

| Sentencias SQL |
| --- |
```sql

SELECT 
    ot.id_orden_trabajo,
    ot.fecha_inicio,
    ot.fecha_fin,
    ot.prioridad,
    e.nombre AS estado,
    ot.id_plan,
    pp.fecha_inicio AS plan_fecha_inicio,
    pp.fecha_fin AS plan_fecha_fin,
    op.fecha_entrega AS orden_pedido_fecha_entrega,
    ot.fecha_creacion
FROM 
    orden_trabajo ot
JOIN 
    estado e ON ot.id_estado = e.id_estado
JOIN 
    plan_produccion pp ON ot.id_plan = pp.id_plan
JOIN 
    orden_pedido op ON ot.id_orden_pedido = op.id_orden_pedido;

```
| Eventos || Al darle click sobre la caja de texto apareceran todas las ordenes de trabajo existente |

| Código requerimiento | RV402 |
| --- | --- |
| Codigo interfaz |  IV402 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/transito/1.2%20-%20Recepcion.PNG)

| Sentencias SQL |
| --- |
```sql

INSERT INTO recepcion_documentos (numero_documento, area_remitente, nombre_receptor)
VALUES ('204165', 'Confeccion', 'Juan Perez');

```
| Eventos |

| Código requerimiento | RV403 |
| --- | --- |
| Codigo interfaz |  IV403 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/transito/1.3%20-%20Conteo%20Productos.PNG)

| Sentencias SQL |
| --- |
```sql

--Insertar codigo producto
INSERT INTO recepcion (codigo_producto)
VALUES ('BD250241');

--Actualizar datos

UPDATE recepcion_productos
SET nombre = 'Polo Amarillo',
    cantidad_original = 45,
    cantidad_a_recepcionar = 45,
    u_m_recepcionada = 'Unidad'

WHERE codigo = 'BD250241';

--Eliminar datos

DELETE FROM recepcion_productos
WHERE codigo = 'BD250241';

```
| Eventos |

| Código requerimiento | RV404 |
| --- | --- |
| Codigo interfaz |  IV404 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/transito/1.4%20-%20Verificacion.PNG)

| Sentencias SQL |
| --- |
```sql
--Mostrar datos finales
SELECT *
FROM recepcion_productos;
```
| Eventos |

| Código requerimiento | RV405 |
| --- | --- |
| Codigo interfaz |  IV405 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/transito/1.5%20-%20Resultado%20Final.PNG)

| Sentencias SQL |
| --- |
```sql

--Mostrar datos finales

SELECT *
FROM recepcion_productos;

```
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

* **EXTRA:**


  * Consulta 1: Lista de ordenes de produccion
  
  ```python
  class OrdenesListView(View):
    def get(self, request):
        with connection.cursor() as cursor:
            query = """
            SELECT
                o.id_orden_producción,
                o.fecha_inicio,
                o.fecha_fin,
                o.cantidad,
                e.nombre AS estado_orden,
                a.nombre AS area,
                tc.nombre AS tipo_corte,
                tmp.nombre AS tipo_materia_prima,
                o.id_orden_trabajo,
                o.fecha_creacion
            FROM
                orden_producción o
            JOIN
                estado e ON o.id_estado = e.id_estado
            JOIN
                area a ON o.id_area = a.id_area
            JOIN
                dimension_corte dc ON o.id_dim_corte = dc.id_dim_corte
            JOIN
                parte_corte_detalle pcd ON dc.id_dim_parte_prenda = pcd.id_dim_parte_prenda
            JOIN
                tipo_corte tc ON pcd.id_tipo_corte = tc.id_tipo_corte
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
                a.nombre = 'Corte'
            GROUP BY
                o.id_orden_producción, o.fecha_inicio, o.fecha_fin, o.cantidad, e.nombre, a.nombre, tc.nombre, tmp.nombre,
                o.id_orden_trabajo, o.fecha_creacion
            ORDER BY
                o.fecha_inicio DESC;
            """
            cursor.execute(query)
            rows = cursor.fetchall()

        data = [
            {
                'id_orden_produccion': row[0],
                'fecha_inicio': row[1],
                'fecha_fin': row[2],
                'cantidad': row[3],
                'estado_orden': row[4],
                'area': row[5],
                'tipo_corte': row[6],
                'tipo_materia_prima': row[7],
                'id_orden_trabajo': row[8],
                'fecha_creacion': row[9]
            }
            for row in rows
        ]
        return JsonResponse(data, safe=False)
  ```

    * Consulta 2: Botón Asignar: el jefe de corte asigna en cada orden de producción la fecha que la a realizar la actividad, que máquina lo va a realizar, y la cantidad ya hecha de la orden de producción si es que esa orden de producción ya se recibió y no se ha terminado.

 

```python
class AsignarView(View):
    def post(self, request, id_orden_produccion):
        body = json.loads(request.body)
        id_maquina = body['id_maquina']
        cantidad_hecha = body['cantidad_hecha']

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO actividad_diaria (fecha_actividad, id_orden_producción) VALUES (NOW(), %s) RETURNING id_actividad;",
                [id_orden_produccion]
            )
            id_actividad = cursor.fetchone()[0]

            cursor.execute(
                "INSERT INTO maquina_actividad (id_actividad, id_maquina, cantidad_hecha) VALUES (%s, %s, %s);",
                [id_actividad, id_maquina, cantidad_hecha]
            )

        return JsonResponse({'status': 'success'})
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
          ID_ESTADO,
          CANTIDAD_DEFECTUOSOS,
          ID_LOTE,
          ID_AQL_LOTE_RANGO,
          ID_AQL_NIVEL,
          ID_AQL_CODIGO,
          ID_AQL_SIGNIFICANCIA,
          DESCRIPCION,
          ID_RESULTADO)
          VALUES(<4>, <3>, 0, 0, <1>, <2>, <6>, <7>, <5>, NULL, NULL);
              
####  6.2
| Código requerimiento | RV602 |
| --- | --- |
| Codigo interfaz | IV602 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/calidad/Revisar%20Inspecciones%202.png)
| Sentencias SQL |
| Eventos |
| **1. Botón Buscar Inspección: Cuando el usuario presione el botón “buscar” se buscará las inspecciones de calidad |

          SELECT
          OP.ID_ORDEN_PRODUCCION
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
          FROM
          INSPECCION_CALIDAD I
          JOIN LOTE LT ON I.ID_LOTE = LT.ID_LOTE
          JOIN ACTIVIDAD_DIARIA AD ON LT.ID_ACTIVIDAD = AD.ID_ACTIVIDAD
          JOIN ORDEN_PRODUCCION OP ON AD.ID_ORDEN_PRODUCCION = OP.ID_ORDEN_PRODUCCION
          WHERE OP.ID_ORDEN_PRODUCCION = <1>
          ORDER BY OP.ID_ORDEN_PRODUCCION DESC;

####  6.3
| Código requerimiento | RV603 |
| --- | --- |
| Codigo interfaz |  IV603 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/calidad/Registrar%20datos%20de%20Inspeccion.png)
| Sentencias SQL |
| Eventos |
| **1. Botón “Registrar datos de Inspección”: Cuando el usuario presione el botón se actualizará la inspección seleccionada previamente |

          UPDATE INSPECCION_CALIDAD SET
          CANTIDAD_DEFECTUOSOS = <2>,
          DESCRIPCION = <3>,
          ID_RESULTADO = <4>
          ID_ESTADO = 3
          WHERE ID_INSPECCION = <1>;

### 7. PCP 

####  7.1
| Código requerimiento | RV701 |
| --- | --- |
| Codigo interfaz |  IV701 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/pcp/1.%20Ingresar%20órdenes%20de%20pedido%20a%20la%20línea%20de%20producción.jpg)
| Sentencias SQL |
| Eventos |
| **1. Botón “Programar”: Cuando el usuario seleccione una Orden de Pedido y presione el botón “Programar” se iniciará la programación de la Orden de Producción|

    SELECT 
    id_orden_pedido,
    COALESCE(fecha_creacion, 'Fecha no especificada') AS fecha_creacion,
    COALESCE(fecha_fin, 'Fecha no especificada') AS fecha_fin,
    COALESCE(id_dim_prenda, 'ID no especificado') AS id_dim_prenda,
    COALESCE(estado, 'Estado no especificado') AS estado
    FROM 
    orden_pedido;

);

              
####  7.2
| Código requerimiento | RV702 |
| --- | --- |
| Codigo interfaz | IV702 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/pcp/2.%20Programar%20órdenes%20de%20producción.jpg)
| Sentencias SQL |
| Eventos |
| **1. Botón "Programar": Cuando el usuario haya completado todos los campos se podrá registrar la programación de la orden de producción. |

          -- Insertar datos en la tabla area
          INSERT INTO area (id_area, nombre_area) VALUES (Texto, 'Texto'),
          -- Insertar datos en la tabla dim_prenda
          INSERT INTO dim_prenda (id_dim_prenda, tipo_prenda, estilo_prenda, talla_prenda, genero_prenda) VALUES (Texto, 'Texto','Texto', 'Texto', 'Texto'),
          -- Insertar una nueva orden de producción
          INSERT INTO orden_produccion (fecha_inicio, fecha_fin, id_area, id_dim_prenda, guia_confeccion, medidas_prenda) VALUES ('Texto', 'Texto', Texto, Texto, 'Texto', 'Texto');
         -- Verificar la inserción
          SELECT * FROM orden_produccion;

####  7.3
| Código requerimiento | RV703 |
| --- | --- |
| Codigo interfaz |  IV703 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/pcp/3.%20Controlar%20órdenes%20de%20producción.jpg)
| Sentencias SQL |
| Eventos |
| **1. Botón “Editar": Cuando el usuario presione el botón "Editar" podrá iniciar una reprogramación. |

          SELECT 
          id_orden_produccion,
          COALESCE(fecha_creacion, 'Fecha no especificada') AS fecha_creacion,
          COALESCE(fecha_inicio, 'Fecha no especificada') AS fecha_inicio,
          COALESCE(fecha_fin, 'Fecha no especificada') AS fecha_fin,
          COALESCE(id_area, 'ID no especificado') AS id_area,
          COALESCE(id_orden_trabajo, 'ID no especificado') AS id_orden_trabajo,
          COALESCE(estado, 'Estado no especificado') AS estado
          FROM 
          orden_produccion;

####  7.4
| Código requerimiento | RV704 |
| --- | --- |
| Codigo interfaz |  IV704 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/pcp/4.%20Reprogramar%20órdenes%20de%20producción.jpg)
| Sentencias SQL |
| Eventos |
| **1. Botón “Reprogramar”: Cuando el usuario presione el botón "Reprogramar" se actualizará los campos programados inicialmente. |

          SELECT * FROM orden_produccion
          -- Actualizar datos en la tabla area
          UPDATE area (id_area, nombre_area) SET (Texto, 'Texto'),
          -- Actualizar datos en la tabla dim_prenda
          UPDATE dim_prenda (id_dim_prenda, tipo_prenda, estilo_prenda, talla_prenda, genero_prenda) SET (Texto, 'Texto','Texto', 'Texto', 'Texto'),
          -- Actualizar una nueva orden de producción
          UPDATE orden_produccion (fecha_inicio, fecha_fin, id_area, id_dim_prenda, guia_confeccion, medidas_prenda) SET ('Texto', 'Texto', Texto, Texto, 'Texto', 'Texto');
          -- Verificar la inserción
          SELECT * FROM orden_produccion;


              
####  7.5
| Código requerimiento | RV705 |
| --- | --- |
| Codigo interfaz | IV705 |
| Imagen interfaz  |

![](../Entregable%203/Prototipos/pcp/5.%20Visualizar%20órdenes%20de%20trabajo.jpg)
| Sentencias SQL |
| Eventos |
| **1. Botón "Desacargar": Cuando el usuario presione el botón “Descargar” se podrá imprimir la orden de trabajo.|

    SELECT 
    fecha_creacion,
    fecha_inicio,
    fecha_fin,
    prioridad,
    estado,
    id_orden_pedido,
    id_plan
    FROM 
    orden_trabajo;

**[Ir a la seccion 4](4-carga-datos.md)**

***[Regresar al índice](./entregable%203-indice.md)***
