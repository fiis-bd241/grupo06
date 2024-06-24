# Entregable 4 del proyecto
## 1. Objetos de BD
Presentamos diversos objetos de base de datos, como índices y vistas, y las mostramos por módulos del sistema:
- [Almacén Central](#almacén_central)
- [Corte](#corte)
- [Confección](#confección)
- [Almacén_de_tránsito](#almacén_de_tránsito)
- [Acabados](#acabados)
- [Inspección_de_calidad](#inspección_de_calidad)
- [PCP - Abastecimiento](#pcp)

Acontinuamos le presentamos cada módulo:
## Almacén_Central


***Querys***
<details>
  <summary>SENTENCIAS SQL COMPLEJAS</summary>
  
```sql

```
</details>

<details>
  <summary>ÍNDICES</summary>
  
```sql

```
</details>

<details>
  <summary>VISTAS</summary>
  
```sql

```
</details>

<details>
  <summary>SECUENCIAS</summary>
  
```sql

```
</details>

<details>
  <summary>TRIGGERS</summary>
  
```sql

```
</details>

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue)](#1-objetos-de-bd)

  
### Corte


***Querys***
<details>
  <summary>SENTENCIAS SQL COMPLEJAS</summary>
  
```sql

```
</details>

<details>
  <summary>ÍNDICES</summary>
  
```sql
-- ========= INDICES =========
-- Nos mostrará el plan de ejecución de la consulta y el tiempo de ejecución real, permitiéndonos evaluar la efectividad del índice creado

CREATE INDEX idx_orden_produccion_estado_fecha_inicio ON orden_producción (id_estado, fecha_inicio);
EXPLAIN ANALYZE
SELECT * FROM orden_producción
WHERE id_estado = 9 -- Que es el estado En proceso
  AND fecha_inicio BETWEEN '2024-01-01' AND '2024-06-30';
```
</details>

<details>
  <summary>VISTAS</summary>
  
```sql
-- ========= VISTAS =========
-- 1 muestra detalles completos de las máquinas incluyendo su estado.

CREATE VIEW vista_maquinas AS
SELECT m.id_maquina, m.capacidad_total, e.nombre AS estado
FROM maquina m
JOIN estado e ON m.id_estado = e.id_estado;

-- Supongamos que deseas obtener todos los detalles de las máquinas en estado 'Disponible'
SELECT * FROM vista_maquinas
WHERE estado = 'Disponible';


--2 muestra las actividades diarias junto con las máquinas utilizadas y detalles de las órdenes de producción.

CREATE VIEW vista_actividades_diarias AS
SELECT ad.id_actividad, ad.fecha_actividad, op.id_orden_producción, ma.id_maquina, ma.cantidad_hecha
FROM actividad_diaria ad
JOIN orden_producción op ON ad.id_orden_producción = op.id_orden_producción
JOIN maquina_actividad ma ON ad.id_actividad = ma.id_actividad;

-- Obtener las actividades diarias realizadas en una fecha específica junto con las máquinas utilizadas y la orden de producción asociada
SELECT * FROM vista_actividades_diarias
WHERE fecha_actividad = '2024-06-22';

-- 3 muestra detalles completos de las órdenes de producción incluyendo el estado y las dimensiones asociadas.

CREATE VIEW vista_ordenes_produccion AS
SELECT op.id_orden_producción, op.fecha_inicio, op.fecha_fin, op.cantidad, e.nombre AS estado, a.nombre AS area, op.fecha_creacion
FROM orden_producción op
JOIN estado e ON op.id_estado = e.id_estado
JOIN area a ON op.id_area = a.id_area;

-- Obtener todas las órdenes de producción que están en estado 'En Proceso':
SELECT * FROM vista_ordenes_produccion
WHERE estado = 'En Proceso';

```
</details>

<details>
  <summary>SECUENCIAS</summary>
  
```sql

```
</details>

<details>
  <summary>TRIGGERS</summary>
  
```sql
-- ========= TRIGGERS =========
-- Verificar si la cantidad utilizada en una actividad diaria no supera la capacidad total de la máquina asignada.

CREATE OR REPLACE FUNCTION verificar_capacidad_maquina()
RETURNS TRIGGER AS $$
DECLARE
    capacidad_maquina INT;
BEGIN
    -- Obtener la capacidad total de la máquina
    SELECT capacidad_total INTO capacidad_maquina
    FROM maquina
    WHERE id_maquina = NEW.id_maquina;
    
    -- Verificar si la cantidad utilizada supera la capacidad de la máquina
    IF NEW.cantidad_hecha > capacidad_maquina THEN
        RAISE EXCEPTION 'La cantidad utilizada (%s) excede la capacidad de la máquina (%s)', NEW.cantidad_hecha, capacidad_maquina;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

```
</details>

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue)](#1-objetos-de-bd)

### Confección
***Querys***
<details>
  <summary>SENTENCIAS SQL COMPLEJAS</summary>
  
```sql

```
</details>

<details>
  <summary>ÍNDICES</summary>
  
```sql

```
</details>

<details>
  <summary>VISTAS</summary>
  
```sql

```
</details>

<details>
  <summary>SECUENCIAS</summary>
  
```sql

```
</details>

<details>
  <summary>TRIGGERS</summary>
  
```sql

```
</details>

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue)](#1-objetos-de-bd)


### Almacén_de_tránsito

***Querys***
<details>
  <summary>SENTENCIAS SQL COMPLEJAS</summary>
  
```sql

```
</details>

<details>
  <summary>ÍNDICES</summary>
  
```sql

```
</details>

<details>
  <summary>VISTAS</summary>
  
```sql

```
</details>

<details>
  <summary>SECUENCIAS</summary>
  
```sql

```
</details>

<details>
  <summary>TRIGGERS</summary>
  
```sql

```
</details>

[![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue)](#1-objetos-de-bd)

  
### Acabados

***Querys***

<details>
  <summary>SENTENCIAS SQL COMPLEJAS</summary>
  
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


</details>


<details>
  <summary>ÍNDICES</summary>

* **Índices:**
1. Consultar datos de empleado del área acabados

```sql
-- 
explain analyze
select * from empleado e 
where id_area =5;
```
![select1](./pantallas/1-ind-1a.png)

```sql
-- Índice:

CREATE INDEX EMPL_ACABADO ON empleado(nombre, primer_apellido, id_area)

EXPLAIN ANALYZE
SELECT * FROM EMPL_ACABADO
WHERE id_area=5;
```
![select1a](./pantallas/1-ind-1b.png)

----

2. Prendas: Consultar la relación de prendas de la caja 200 (12692 registros)
```sql
explain analyze
select * from prenda
where id_caja=200;
```
![select2](./pantallas/2-ind-2a.png)

```sql
CREATE INDEX PRENDA_CAJA ON prenda(id_caja)

EXPLAIN ANALYZE
select * from prenda
where id_caja=200;


```
![select2a](./pantallas/2-ind-2b.png)

</details>

<details>
  <summary>VISTAS</summary>
* Vistas
-- 1. CARGAR LOTES: lotes 200 entrantes al área de acabados, en carga de página.
  
```sql
explain analyze
SELECT le.id_entrada ,le.fecha_entrada,l.id_tipo_lote,l.cantidad, dc.id_dim_confeccion,dc.id_guia_confeccion
FROM lote_entrada le
JOIN lote l on le.id_lote = l.id_lote
join dimension_confeccion dc on l.id_dim_confeccion = dc.id_dim_confeccion
LIMIT 200;
```
![select3a](./pantallas/3-ind-2.png)

```sql

create view entrante_aca as 
SELECT le.id_entrada ,le.fecha_entrada,l.id_tipo_lote,l.cantidad, dc.id_dim_confeccion,dc.id_guia_confeccion
FROM lote_entrada le
JOIN lote l on le.id_lote = l.id_lote
join dimension_confeccion dc on l.id_dim_confeccion = dc.id_dim_confeccion
LIMIT 200;

--  BUSCAR
select * from entrante_aca
where id_entrada='101';
```
![select3a](./pantallas/3-ind-2.png)

----

***VIEW - Detalle caja***

```sql
-- Consulta:
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
    prenda p ON cp.id_caja = p.id_caja
where  cp.id_caja='101';
```
![select4a](./pantallas/4-vis-1.png)
![select4a1](./pantallas/4-vis-1a.png)

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
-- Caja 101
select * from vista_datos_confeccion
where id_caja =' 101';

```
![select4a](./pantallas/4-vis-2.png)
![select4a1](./pantallas/4-vis-2a.png)

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


```
</details>

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue)](#1-objetos-de-bd)





### Inspección_de_calidad


***Querys***
<details>
  <summary>SENTENCIAS SQL COMPLEJAS</summary>
  
```sql

```
</details>

<details>
  <summary>ÍNDICES</summary>
  
```sql

```
</details>

<details>
  <summary>VISTAS</summary>
  
```sql

```
</details>

<details>
  <summary>SECUENCIAS</summary>
  
```sql

```
</details>

<details>
  <summary>TRIGGERS</summary>
  
```sql

```
</details>

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue)](#1-objetos-de-bd)

  
### PCP


***Querys***
<details>
  <summary>SENTENCIAS SQL COMPLEJAS</summary>
  
```sql

```
</details>

<details>
  <summary>ÍNDICES</summary>
  
```sql

```
</details>

<details>
  <summary>VISTAS</summary>
  
```sql

```
</details>

<details>
  <summary>SECUENCIAS</summary>
  
```sql

```
</details>

<details>
  <summary>TRIGGERS</summary>
  
```sql

```
</details>

  [![Volver al inicio](https://img.shields.io/badge/Volver_al_inicio-blue)](#1-objetos-de-bd)


[Regresar al Índice](./indice.md)
