# Entregable 4 del proyecto
## 1. Objetos de BD
Presentamos diversos objetos de base de datos, como índices y vistas, y las mostramos por módulos del sistema:
* **Almacén Central**


***Querys***
```sql

```
  
* **Corte**


***Querys***
```sql

```
  
* **Confección**
```sql

```
  
* **Almacén de tránsito**

***Querys***
```sql

```
  
* **Acabados**
1. Pantalla **Lotes de entrada**

***Querys***
```sql
-- CARGAR LOTES: lotes entrantes al área de acabados, en carga de página.
create view entrante_aca as 
SELECT le.id_entrada ,le.fecha_entrada,l.id_tipo_lote,l.cantidad, dc.id_dim_confeccion,dc.id_guia_confeccion
FROM lote_entrada le
JOIN lote l on le.id_lote = l.id_lote
join dimension_confeccion dc on l.id_dim_confeccion = dc.id_dim_confeccion
LIMIT 200;

-- BOTÖN BUSCAR
select * from entrante_aca
where id_entrada='101';
```
2. Pantalla **Detalle de caja**
```sql
--WHERE id_caja = '101' : Indica el id principal que será parte de la url para el detalle de caja.
-- DETALLE CAJA: SENTENCIA SQL
SELECT cp.id_caja as ID_Caja,
cp.cantidad , 
gconf.id_guia_confeccion as ID_guia,
tp.nombre, ep.nombre ,t.nombre,
g.nombre  ,
    COALESCE(gconf.medida_longitud::text, ' ') AS ml,
    COALESCE(gconf.medida_hombro::text, ' ') AS mh,
    COALESCE(gconf.medida_pecho::text, ' ') AS mp,
    COALESCE(gconf.medida_manga::text, ' ') AS mm,
    COALESCE(gconf.medida_cintura::text, ' ') AS mc,
    COALESCE(gconf.medida_cadera::text, ' ') AS mca,
    COALESCE(gconf.medida_muslo::text, ' ') AS mmu
FROM 
dimension_confeccion dc
JOIN guia_confeccion gconf ON dc.id_guia_confeccion = gconf.id_guia_confeccion
JOIN tipo_prenda tp ON dc.id_tipo_prenda = tp.id_tipo_prenda
JOIN estilo_prenda ep ON dc.id_estilo_prenda = ep.id_estilo_prenda
JOIN talla t ON dc.id_talla = t.id_talla
JOIN genero g ON dc.id_genero = g.id_genero
join dimension_prenda dp on dc.id_dim_confeccion = dp.id_dim_confeccion 
join caja_prenda cp on dp.id_dim_prenda = cp.id_dim_prenda
join prenda p on cp.id_caja = p.id_caja 
where cp.id_caja = '101';

-- DETALLE CAJA: Mostrar, al cargar la página todos los detalles de una
-- caja perteneciente a un lote que ingresa al área de acabados
-- (Se muestra 'No hay datos' si en la DB no hay datos):
SELECT 
    COALESCE(subquery.id_caja::text, 'No hay datos') AS id_caja,
    subquery.cantidad, 
    subquery.id_guia AS id_guia,
    subquery.tipo_prenda, 
    subquery.estilo_prenda, 
    subquery.talla, 
    subquery.genero,
    subquery.ml,
    subquery.mh,
    subquery.mp,
    subquery.mm,
    subquery.mc,
    subquery.mca,
    subquery.mmu
FROM (
    SELECT 
        cp.id_caja::text AS id_caja,
        cp.cantidad, 
        gconf.id_guia_confeccion AS id_guia,
        tp.nombre AS tipo_prenda, 
        ep.nombre AS estilo_prenda, 
        t.nombre AS talla, 
        g.nombre AS genero,
        COALESCE(gconf.medida_longitud::text, ' ') AS ml,
        COALESCE(gconf.medida_hombro::text, ' ') AS mh,
        COALESCE(gconf.medida_pecho::text, ' ') AS mp,
        COALESCE(gconf.medida_manga::text, ' ') AS mm,
        COALESCE(gconf.medida_cintura::text, ' ') AS mc,
        COALESCE(gconf.medida_cadera::text, ' ') AS mca,
        COALESCE(gconf.medida_muslo::text, ' ') AS mmu
    FROM 
        dimension_confeccion dc
    JOIN 
        guia_confeccion gconf ON dc.id_guia_confeccion = gconf.id_guia_confeccion
    JOIN 
        tipo_prenda tp ON dc.id_tipo_prenda = tp.id_tipo_prenda
    JOIN 
        estilo_prenda ep ON dc.id_estilo_prenda = ep.id_estilo_prenda
    JOIN 
        talla t ON dc.id_talla = t.id_talla
    JOIN 
        genero g ON dc.id_genero = g.id_genero
    JOIN 
        dimension_prenda dp ON dc.id_dim_confeccion = dp.id_dim_confeccion 
    JOIN 
        caja_prenda cp ON dp.id_dim_prenda = cp.id_dim_prenda
    JOIN 
        prenda p ON cp.id_caja = p.id_caja 
    WHERE 
        cp.id_caja = '101'
) subquery
UNION ALL
SELECT 
    'No hay datos' AS id_caja,
    NULL AS cantidad, 
    null AS id_guia,
    NULL AS tipo_prenda, 
    NULL AS estilo_prenda, 
    NULL AS talla, 
    NULL AS genero,
    ' ' AS ml,
    ' ' AS mh,
    ' ' AS mp,
    ' ' AS mm,
    ' ' AS mc,
    ' ' AS mca,
    ' ' AS mmu
WHERE NOT EXISTS (
    SELECT 1 
    FROM dimension_confeccion dc
    JOIN guia_confeccion gconf ON dc.id_guia_confeccion = gconf.id_guia_confeccion
    JOIN tipo_prenda tp ON dc.id_tipo_prenda = tp.id_tipo_prenda
    JOIN estilo_prenda ep ON dc.id_estilo_prenda = ep.id_estilo_prenda
    JOIN talla t ON dc.id_talla = t.id_talla
    JOIN genero g ON dc.id_genero = g.id_genero
    JOIN dimension_prenda dp ON dc.id_dim_confeccion = dp.id_dim_confeccion 
    JOIN caja_prenda cp ON dp.id_dim_prenda = cp.id_dim_prenda
    JOIN prenda p ON cp.id_caja = p.id_caja 
    WHERE cp.id_caja = '101'
);

```
***VIEW - Detalle caja***
```sql
CREATE VIEW vista_datos_confeccion AS
SELECT 
    cp.id_caja::text AS id_caja,
    cp.cantidad, 
    gconf.id_guia_confeccion::text AS id_guia,
    tp.nombre AS tipo_prenda, 
    ep.nombre AS estilo_prenda, 
    t.nombre AS talla, 
    g.nombre AS genero,
    COALESCE(gconf.medida_longitud::text, ' ') AS ml,
    COALESCE(gconf.medida_hombro::text, ' ') AS mh,
    COALESCE(gconf.medida_pecho::text, ' ') AS mp,
    COALESCE(gconf.medida_manga::text, ' ') AS mm,
    COALESCE(gconf.medida_cintura::text, ' ') AS mc,
    COALESCE(gconf.medida_cadera::text, ' ') AS mca,
    COALESCE(gconf.medida_muslo::text, ' ') AS mmu
FROM 
    dimension_confeccion dc
JOIN 
    guia_confeccion gconf ON dc.id_guia_confeccion = gconf.id_guia_confeccion
JOIN 
    tipo_prenda tp ON dc.id_tipo_prenda = tp.id_tipo_prenda
JOIN 
    estilo_prenda ep ON dc.id_estilo_prenda = ep.id_estilo_prenda
JOIN 
    talla t ON dc.id_talla = t.id_talla
JOIN 
    genero g ON dc.id_genero = g.id_genero
JOIN 
    dimension_prenda dp ON dc.id_dim_confeccion = dp.id_dim_confeccion 
JOIN 
    caja_prenda cp ON dp.id_dim_prenda = cp.id_dim_prenda
JOIN 
    prenda p ON cp.id_caja = p.id_caja;

-- ====== VISTAS: ==============
-- ID Caja
select id_caja from vista_datos_confeccion
where id_caja =' 101';
-- Cantidad
select cantidad from vista_datos_confeccion
where id_caja =' 101';
-- ID guía
select id_guia from vista_datos_confeccion
where id_caja =' 101';
-- Tipo prenda
select tipo_prenda from vista_datos_confeccion
where id_caja =' 101';

-- GRILLA DETALLE
select tipo_prenda,id_guia,ml,mh,mp,
mm,mc,mca,mmu,estilo_prenda,talla,
genero 
from vista_datos_confeccion
where id_caja =' 101';

```


* **Inspección de calidad**


***Querys***
```sql

```

* **PCP**


***Querys***
```sql

```


[Regresar al Índice](./indice.md)
