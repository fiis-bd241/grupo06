# Entregable 4 del proyecto
## Base de datos NoSQL


## Base de datos NoSQL Elegido
<div align=center>

[![Website](https://img.shields.io/website?up_message=AVAILABLE&down_message=DOWN&url=https%3A%2F%2Fclickhouse.com&style=for-the-badge)](https://clickhouse.com)
[![Apache 2.0 License](https://img.shields.io/badge/license-Apache%202.0-blueviolet?style=for-the-badge)](https://www.apache.org/licenses/LICENSE-2.0)

<picture align=center>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ClickHouse/clickhouse-docs/assets/9611008/4ef9c104-2d3f-4646-b186-507358d2fe28">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/ClickHouse/clickhouse-docs/assets/9611008/b001dc7b-5a45-4dcd-9275-e03beb7f9177">
    <img alt="The ClickHouse company logo." src="https://github.com/ClickHouse/clickhouse-docs/assets/9611008/b001dc7b-5a45-4dcd-9275-e03beb7f9177">
</picture>

<h4>ClickHouse® es un sistema de gestión de bases de datos de código abierto orientado a columnas que permite generar informes analíticos de datos en tiempo real..</h4>

</div>

**ClickHouse®** es un sistema de gestión de bases de datos SQL de alto rendimiento orientado a columnas para el procesamiento analítico en línea (OLAP, por sus siglas en inglés). Está disponible tanto como software de código abierto como en una oferta en la nube.

**¿Qué es OLAP?**

Los escenarios OLAP requieren respuestas en tiempo real sobre conjuntos de datos grandes para consultas analíticas complejas con las siguientes características:

- Los conjuntos de datos pueden ser masivos, con miles de millones o billones de filas.
- Los datos están organizados en tablas que contienen muchas columnas.
- Solo se seleccionan unas pocas columnas para responder a cualquier consulta específica.
- Los resultados deben devolverse en milisegundos o segundos.



### Enlaces

* [Official website](https://clickhouse.com/) tiene una rápida visión general de ClickHouse en la página principal.
* [ClickHouse Cloud](https://clickhouse.cloud) ClickHouse como servicio, construido por los creadores y mantenedores.
* [Tutorial](https://clickhouse.com/docs/en/getting_started/tutorial/) muestra cómo configurar y consultar un pequeño clúster ClickHouse.
* [Documentation](https://clickhouse.com/docs/en/) ofrece información más detallada.
* [YouTube channel](https://www.youtube.com/c/ClickHouseDB) tiene mucho contenido sobre ClickHouse en formato de vídeo.
* [Slack](https://clickhouse.com/slack) y [Telegram](https://telegram.me/clickhouse_en) permiten chatear con los usuarios de ClickHouse en tiempo real.
* [Blog](https://clickhouse.com/blog/) contiene diversos artículos relacionados con ClickHouse, así como anuncios e informes sobre eventos.
* [Code Browser (github.dev)](https://github.dev/ClickHouse/ClickHouse) con resaltado de sintaxis, impulsado por github.dev.
* [Contacts](https://clickhouse.com/company/contact) resuelve dudas.


### Características Avanzadas de ClickHouse

<table>
  <thead>
    <tr>
      <th style="padding:10px;">Categoría</th>
      <th style="padding:10px;">Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style=" padding:10px;" colspan="2"><b>Índices y Particionamiento</b></td>
    </tr>
    <tr>
      <td style="padding:10px;">Primary Key y Orden de Índices</td>
      <td style="padding:10px;">ClickHouse permite definir una clave primaria y un orden de índice para optimizar las consultas. El índice primario no garantiza la unicidad, sino que organiza los datos para una lectura eficiente.</td>
    </tr>
    <tr>
      <td style="padding:10px;">Particionamiento</td>
      <td style="padding:10px;">Los datos pueden ser particionados para mejorar el rendimiento de las consultas y la gestión del almacenamiento. El particionamiento puede basarse en campos como fechas, útil para datos de series temporales.</td>
    </tr>
    <tr>
      <td style="background-color:#e6f7ff; padding:10px;" colspan="2"><b>Ingesta y Procesamiento de Datos</b></td>
    </tr>
    <tr>
      <td style="padding:10px;">Batch y Streaming</td>
      <td style="padding:10px;">ClickHouse soporta tanto la ingesta en batch como en streaming, lo que lo hace flexible para diferentes flujos de trabajo de datos. Puedes usar Kafka, RabbitMQ o sistemas similares para la ingesta en tiempo real.</td>
    </tr>
    <tr>
      <td style="padding:10px;">Materialized Views</td>
      <td style="padding:10px;">Las vistas materializadas permiten almacenar resultados precomputados de consultas complejas, mejorando el rendimiento en consultas repetitivas.</td>
    </tr>
    <tr>
      <td style="background-color:#e6f7ff; padding:10px;" colspan="2"><b>Alta Disponibilidad y Recuperación de Desastres</b></td>
    </tr>
    <tr>
      <td style="padding:10px;">Replica Sets</td>
      <td style="padding:10px;">ClickHouse soporta la replicación de datos entre nodos, proporcionando alta disponibilidad y tolerancia a fallos. Los datos se replican de manera asíncrona, asegurando que las copias de seguridad estén siempre disponibles.</td>
    </tr>
    <tr>
      <td style="padding:10px;">Backups y Restauración</td>
      <td style="padding:10px;">Las herramientas integradas permiten realizar backups incrementales y restauraciones, facilitando la recuperación ante desastres.</td>
    </tr>
    <tr>
      <td style=" padding:10px;" colspan="2"><b>Interoperabilidad</b></td>
    </tr>
    <tr>
      <td style="padding:10px;">Integración con Ecosistemas de Big Data</td>
      <td style="padding:10px;">ClickHouse puede integrarse con herramientas y plataformas de big data como Hadoop, Spark, y herramientas de BI como Tableau, Grafana, y Power BI.</td>
    </tr>
    <tr>
      <td style="padding:10px;">APIs y Conectores</td>
      <td style="padding:10px;">Proporciona APIs y conectores para diferentes lenguajes de programación, facilitando su integración en aplicaciones existentes.</td>
    </tr>
  </tbody>
</table>


[Regresar al índice](./indice.md)
