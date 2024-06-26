--Parche para corregir el sistema legacy
-- Paso 1: Agregar nuevas columnas serial a `aql_muestra` y `aql_resultado_rango`
ALTER TABLE aql_muestra ADD COLUMN id_aql_muestra SERIAL;
ALTER TABLE aql_resultado_rango ADD COLUMN id_aql_resultado_rango SERIAL;

-- Paso 2: Poblar las nuevas columnas seriales (esto es automático con SERIAL)

-- Paso 3: Eliminar las claves foráneas en `inspeccion_calidad` que dependen de las claves primarias compuestas
ALTER TABLE inspeccion_calidad DROP CONSTRAINT inspeccion_calidad_id_aql_lote_rango_id_aql_nivel_fkey;
ALTER TABLE inspeccion_calidad DROP CONSTRAINT inspeccion_calidad_id_aql_codigo_id_aql_significancia_fkey;

-- Paso 4: Eliminar las claves primarias compuestas antiguas
ALTER TABLE aql_muestra DROP CONSTRAINT aql_muestra_pkey;
ALTER TABLE aql_resultado_rango DROP CONSTRAINT aql_resultado_rango_pkey;

-- Paso 5: Crear nuevas claves primarias en `aql_muestra` y `aql_resultado_rango`
ALTER TABLE aql_muestra ADD CONSTRAINT pk_aql_muestra PRIMARY KEY (id_aql_muestra);
ALTER TABLE aql_resultado_rango ADD CONSTRAINT pk_aql_resultado_rango PRIMARY KEY (id_aql_resultado_rango);

-- Paso 6: Agregar nuevas columnas de clave foránea a `inspeccion_calidad`
ALTER TABLE inspeccion_calidad ADD COLUMN id_aql_muestra INT;
ALTER TABLE inspeccion_calidad ADD COLUMN id_aql_resultado_rango INT;

-- Poblar las nuevas columnas de clave foránea en `inspeccion_calidad`
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT id_aql_lote_rango, id_aql_nivel, id_aql_muestra FROM aql_muestra) LOOP
        UPDATE inspeccion_calidad
        SET id_aql_muestra = r.id_aql_muestra
        WHERE id_aql_lote_rango = r.id_aql_lote_rango AND id_aql_nivel = r.id_aql_nivel;
    END LOOP;

    FOR r IN (SELECT id_aql_codigo, id_aql_significancia, id_aql_resultado_rango FROM aql_resultado_rango) LOOP
        UPDATE inspeccion_calidad
        SET id_aql_resultado_rango = r.id_aql_resultado_rango
        WHERE id_aql_codigo = r.id_aql_codigo AND id_aql_significancia = r.id_aql_significancia;
    END LOOP;
END $$;

ALTER TABLE inspeccion_calidad ALTER COLUMN id_aql_muestra SET NOT NULL;
ALTER TABLE inspeccion_calidad ALTER COLUMN id_aql_resultado_rango SET NOT NULL;

-- Paso 7: Crear nuevas claves foráneas simples en `inspeccion_calidad`
ALTER TABLE inspeccion_calidad ADD CONSTRAINT fk_inspeccion_calidad_aql_muestra FOREIGN KEY (id_aql_muestra) REFERENCES aql_muestra(id_aql_muestra);
ALTER TABLE inspeccion_calidad ADD CONSTRAINT fk_inspeccion_calidad_aql_resultado_rango FOREIGN KEY (id_aql_resultado_rango) REFERENCES aql_resultado_rango(id_aql_resultado_rango);

-- (Opcional) Eliminar las columnas de la clave foránea compuesta antigua en `inspeccion_calidad`
ALTER TABLE inspeccion_calidad DROP COLUMN id_aql_lote_rango, DROP COLUMN id_aql_nivel, DROP COLUMN id_aql_codigo, DROP COLUMN id_aql_significancia;