# Entregable 4 del proyecto
## Proceso Batch
### Enunciado:
* Obtener una vista del progreso de producción al final del día (medianoche) para registrar el avance diario. Se actualiza diariamente.

***Query SQL***
```sql
            explain analyze
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
                    

```
![batch1](./images/ba1.png)
![batch2](./images/ba2.png)
![batch3](./images/ba3.png)
![batch4](./images/ba4.png)


### PLPGSQL
```sql
CREATE OR REPLACE FUNCTION calcular_progreso_produccion()
RETURNS VOID AS $$
BEGIN
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
END;
$$ LANGUAGE plpgsql;
```

### Usando Cron
Se agrega una entrada al archivo crontab para ejecutar un script de shell que invoque psql y ejecute la función todos los días a medianoche.
```
0 0 * * * psql -d vircatex -c 'SELECT calcular_progreso_produccion();'

```


[Regresar al índice](./indice.md)
