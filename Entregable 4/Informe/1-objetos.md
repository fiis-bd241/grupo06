# Entregable 4 del proyecto
## 1. Objetos de BD
Presentamos diversos objetos de base de datos, como índices y vistas, y las mostramos por módulos del sistema:


Acontinuamos le presentamos cada módulo:
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

<details>
  <summary>SENTENCIAS SQL COMPLEJAS</summary>
  
```sql
-- ========= INDICES =========
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
</details>


<details>
  <summary>ÍNDICES</summary>
  
```sql
-- ========= INDICES =========
-- 1. Consultar datos de empleado del área acabados
CREATE INDEX EMPL_ACABADO ON empleado(nombre, primer_apellido, id_area)

EXPLAIN ANALYZE
SELECT * FROM EMPL_ACABADO
WHERE id_area=5;

-- 2. Actividad diaria: Ver la actividad que se realizó hoy en la empresa
CREATE INDEX ACT_DIARIA ON actividad_diaria(cantidad_hecha)

EXPLAIN ANALYZE
SELECT * FROM ACT_DIARIA
WHERE

```
</details>

<details>
  <summary>VISTAS</summary>
  
```sql
-- ========= VISTAS =========
```sql
-- 1. CARGAR LOTES: lotes entrantes al área de acabados, en carga de página.
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

```
</details>

<details>
  <summary>SECUENCIAS</summary>
  
```sql
-- ========= SECUENCIAS ==========
-- Seriales:
-- Trabajando con secuencias en tablas del Modelo ER que intervienen en el módulo de acabados.

CREATE TABLE direccion
(
  id_direccion SERIAL,
  descripcion VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_direccion)
);

CREATE TABLE correo
(
  id_correo SERIAL,
  direccion_correo VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_correo)
);

CREATE TABLE telefono
(
  id_telefono SERIAL,
  numero VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_telefono),
  UNIQUE (numero)
);

CREATE TABLE cargo
(
  id_cargo SERIAL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_cargo),
  UNIQUE (nombre)
);

CREATE TABLE estado
(
  id_estado SERIAL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_estado),
  UNIQUE (nombre)
);
CREATE TABLE guia_confeccion
(
  id_guia_confeccion SERIAL,
  medida_pecho NUMERIC(4,2),
  medida_cintura NUMERIC(4,2),
  medida_cadera NUMERIC(4,2),
  medida_hombro NUMERIC(4,2),
  medida_longitud NUMERIC(4,2),
  medida_manga NUMERIC(4,2),
  medida_muslo NUMERIC(4,2),
  PRIMARY KEY (id_guia_confeccion)
);

CREATE TABLE tipo_prenda
(
  id_tipo_prenda SERIAL,
  nombre VARCHAR(10) NOT NULL,
  PRIMARY KEY (id_tipo_prenda),
  UNIQUE (nombre)
);

CREATE TABLE estilo_prenda
(
  id_estilo_prenda SERIAL,
  nombre VARCHAR(10) NOT NULL,
  PRIMARY KEY (id_estilo_prenda),
  UNIQUE (nombre)
);

CREATE TABLE talla
(
  id_talla SERIAL,
  nombre VARCHAR(4) NOT NULL,
  PRIMARY KEY (id_talla),
  UNIQUE (nombre)
);

CREATE TABLE genero
(
  id_genero SERIAL,
  nombre VARCHAR(10) NOT NULL,
  PRIMARY KEY (id_genero),
  UNIQUE (nombre)
);

CREATE TABLE acabado
(
  id_acabado SERIAL,
  nombre VARCHAR(10) NOT NULL,
  PRIMARY KEY (id_acabado),
  UNIQUE (nombre)
);

CREATE TABLE area
(
  id_area SERIAL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_area),
  UNIQUE (nombre)
);
CREATE TABLE dimension_confeccion
(
  id_dim_confeccion SERIAL,
  id_tipo_prenda INT NOT NULL,
  id_estilo_prenda INT NOT NULL,
  id_guia_confeccion INT NOT NULL,
  id_talla INT NOT NULL,
  id_genero INT NOT NULL,
  PRIMARY KEY (id_dim_confeccion),
  FOREIGN KEY (id_tipo_prenda) REFERENCES tipo_prenda(id_tipo_prenda),
  FOREIGN KEY (id_estilo_prenda) REFERENCES estilo_prenda(id_estilo_prenda),
  FOREIGN KEY (id_guia_confeccion) REFERENCES guia_confeccion(id_guia_confeccion),
  FOREIGN KEY (id_talla) REFERENCES talla(id_talla),
  FOREIGN KEY (id_genero) REFERENCES genero(id_genero)
);
CREATE TABLE lote
(
  id_lote SERIAL,
  cantidad INT NOT NULL,
  id_estado INT NOT NULL,
  id_tipo_lote INT NOT NULL,
  id_dim_corte INT,
  id_dim_confeccion INT,
  id_dim_materia_prima INT,
  id_actividad INT,
  fecha_creacion TIMESTAMP NOT NULL,
  PRIMARY KEY (id_lote),
  FOREIGN KEY (id_estado) REFERENCES estado(id_estado),
  FOREIGN KEY (id_tipo_lote) REFERENCES tipo_lote(id_tipo_lote),
  FOREIGN KEY (id_dim_corte) REFERENCES dimension_corte(id_dim_corte),
  FOREIGN KEY (id_dim_confeccion) REFERENCES dimension_confeccion(id_dim_confeccion),
  FOREIGN KEY (id_dim_materia_prima) REFERENCES dimension_materia_prima(id_dim_materia_prima),
  FOREIGN KEY (id_actividad) REFERENCES actividad_diaria(id_actividad)
);
CREATE TABLE caja_prenda
(
  id_caja SERIAL,
  cantidad INT NOT NULL,
  fecha_creacion TIMESTAMP NOT NULL,
  id_estado INT NOT NULL,
  id_dim_prenda INT NOT NULL,
  id_actividad INT NOT NULL,
  PRIMARY KEY (id_caja),
  FOREIGN KEY (id_estado) REFERENCES estado(id_estado),
  FOREIGN KEY (id_dim_prenda) REFERENCES dimension_prenda(id_dim_prenda),
  FOREIGN KEY (id_actividad) REFERENCES actividad_diaria(id_actividad)
);
```
</details>

<details>
  <summary>TRIGGERS</summary>
  
```sql
-- ========= TRIGGERS =========
-- 1. CAJA SALIDA
-- A) Creando una función que lance una exception si queremos asignar una caja de salida después de 9pm.
CREATE OR REPLACE FUNCTION VALIDAR_HORARIO_CAJA_ACAB_SALIDA()
RETURNS TRIGGER
LANGUAGE PLPGSQL AS $$
BEGIN
IF TO_CHAR(CURRENT_DATE, 'd') IN ('1') -- Para domingos
OR
-- Horario fuera de trabajo de acabado u oficina
TO_CHAR(now(),'hh24:mi') NOT BETWEEN '07:00' AND '21:00'
THEN
RAISE EXCEPTION 'No está permitido asignar caja de salida. Comunìquese con Administricación o su sipervisor inmediato';
END IF;
RETURN NULL;
END $$;

-- B) TRIGGER
-- Creando trigger para ejecutar antes de un INSERT de la tabla caja_salida
CREATE TRIGGER ADVER_CAJA_SALIDA
BEFORE INSERT ON EMPLOYEES
EXECUTE PROCEDURE VALIDAR_HORARIO_CAJA_ACAB_SALIDA();

-- C) PRUEBA
INSERT caja_salida 
WHERE 


-- 2.
-- A)
-- B) TRIGGER
-- C) PRUEBA

-- A)
-- B) TRIGGER
-- C) PRUEBA

-- A)
-- B) TRIGGER
-- C) PRUEBA

-- A)
-- B) TRIGGER
-- C) PRUEBA

```
</details>






* **Inspección de calidad**


***Querys***
```sql

```

* **PCP**


***Querys***
```sql

```


[Regresar al Índice](./indice.md)
