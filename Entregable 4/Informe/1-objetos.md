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
  
* **Inspección de calidad**


***Querys***
```sql

```

* **PCP**


***Querys***
```sql

```


[Regresar al Índice](./indice.md)
