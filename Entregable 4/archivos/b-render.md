## Crear Backend Local con conexión a PostgreSQL en render

**Indicaciones**

1. Seguimos los pasos de la conexión del [backend local](./archivos/b-local.md). La diferencia radica en
el paso 4:

* La conexión a PostgreSQL en render y se accede mediante API:

```sql
DATABASES = {
    "default": dj_database_url.parse(config("DATABASE_URL"))
}
```
