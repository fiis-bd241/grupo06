# Entregable 3 del proyecto
## Funcionalidades Primarias
### Almacén central 

### Corte
* **Visualizar orden de produccion de corte:** Se verifica la orden de produccion, lo cual tiene el detalle de orden de producción y por cada orden de produccion se le asignará una actividad
* **Visualizar actividad a realizar la maquina en el dia:** El operario recibe que actividades debe realizar cada maquina en el dia
* **Registra corte realizado con el lote usado:** El operario registrara la cantidad de corte realizado, lo cual tiene tipo de lote, cantidad, id_dim_corte, tipo de corte, id_actividad, fecha creacion; en cantidad de lote usado tiene id_lote, que cantidad del lote esta usada
* **Visualizar actividades diarias por máquina:** El jefe de corte pordrá visualizar la id_maquina, la capacidad total, cantidad de actividades, fecha actividad, y un boton de ver actividad lo cual nos muestra un detalle esas actividades que tiene la maquina, como cantidad de cortes, cantidad de orden de produccion y el progreso de produccion
* **Visualizar Número de lotes por dia en el mes:** El jefe veririfica la cantidad de lotes por dia en un mes
* **Visualizar numero de cortes por el orden de producción:**  El jefe podrá visualizar a detalle vsntidad de cortes, en que estado se encuentra y en que progreso se encuentra la produccion
  
### Confección 

### Almacén de tránsito 
------------------------------------------------- Recepciones ----------------------------------------------------------------------------
* **Buscar las ordenes de trabajo:** El Jefe de almacen de transito podra buscar y visualizas las ordenes de de trabajo para aceptar la recepcion
* **Editar producto:** El Jefe de almacen de transito podra editar la cantidad de productos que recepcione en caso no llegue lo establecido en el sistema
* **Eliminar producto:** El Jefe de almacen de transito podra eliminar la cantidad de productos que recepcione en caso no llegue lo establecido en el sistema
* **Añadir producto:** El Jefe de almacen de transito podra añadir la cantidad de productos que recepcione en caso no llegue lo establecido en el sistema
* **Visualizar documentos de recepcion:** El Jefe de almacen de transito podra visualizar los documentos de recepciom en forma de historial
* **Visualizar documentos de recepcion por estado:** El Jefe de almacen de transito podra visualizar el estado en que se encuentran los documentos de recepcion: Recepcionado, Pendiente, Cancelado.
* **Visualizar documentos de recepcion por rango de fecha:** El Jefe de almacen de transito podra visualizar los documentos de recpecion por rango de fecha segun el dia/mes/año buscado.

------------------------------------------------- Prendas Erroneas -----------------------------------------------------------------------
* **Editar producto:** El operario de recepcion podra editar la cantidad de productos defectuosos en caso haya colocado un dato incorrecto.
* **Eliminar producto:** El operario de recepcion podra eliminar la cantidad de productos defectuosos en caso haya colocado un dato incorrecto.
* **Añadir producto:** El operario de recepcion podra añadir la cantidad de productos defectuosos como una nueva fila dentro de la tabla ya existente
* **Visualizar documentos prendas erroneas:** El operario de recepcion podra visualizar las prendas falladas registradas en forma de historial
* **Buscar y visualizar documentos prendas erroneas por registro:** El operario de recepcion podra buscar y visualizar las prendas falladas registradas por el #Registro.
* **Ordenar documentos de recepcion por cantidad de prendas falladas registradas:** El operario de recepcion podra ordenar los documentos de recepcion de forma ascendente o descendente segun la cantidad de prendas falladas registradas.
* **Visualizar documentos de recepcion por rango de fecha:** El operario de recepcion podra visualizar los documentos de prendas falladas por rango de fecha segun el dia/mes/año buscado.

------------------------------------------------- Ubicacion Cajas -----------------------------------------------------------------------
* **Editar producto:** El operario de conteo podra editar los campos de la tabla ubicacion cajas en caso haya colocado un dato incorrecto.
* **Eliminar producto:** El operario de conteo podra eliminar la fila de la tabla ubicacionn caja en caso haya colocado un dato incorrecto.
* **Añadir producto:** El operario de conteo podra añadir un nuevo producto al igual que sus otros datos en latabla ya existente.
* **Guadar cambios:** El operario de conteo una vez verificado el correcto llenado de los campos de la tabla podra guardar los cambio para actualizar la ubicacion de la cajas.

------------------------------------------------- Envio cajas -----------------------------------------------------------------------
* **Editar producto - cajas:** El operario de conteo podra editar los campos de la tabla existente en caso haya colocado un dato incorrecto, teniendo como principal dato su LT, cantidad de cajas y productos enviados.
* **Eliminar producto:**El operario de conteo podra editar los campos de la tabla existente en caso haya colocado un dato incorrecto.
* **Añadir producto:** El operario de conteo podra añadir una nueva fila dentro de la tabla ya existente.
* **Ordenar documentos de envio de cajas por cantidad de prendas enviadas o cajas enviadas:** El operario de conteo podra ordenar los documentos de envio de forma ascendente o descendente segun la cantidad de prendas enviadas o cajas enviadas.
* **Visualizar documentos de envio de cajas por rango de fecha de envio:** El operario de conteo podra visualizar los documentos de cajas enviadas por rango de fecha de envio segun el dia/mes/año buscado.
* **Visualizar documentos de envio de cajas segun los LS:** El operario de conteo podra visualizar los documentos de cajas enviadas segun el LS.

### Acabados
* **Visualizar lotes, cajas, prendas ingresantes a área:** Se verifica las órdenes de producción, cajas que incluyen, detalles de prendas y medidas con características, en una tabla.
* **Ver operario:** Encargado asigna operario a un lote ingresante al área.
* **Ver Caja:** Operario verifica las cajas del lote asignado y ve detalles para realizar los acabados.
* **Registro de acabados:** Operario registra el término del subproceso, modifica el estado del acabado mediante el sistema.

### Calidad 
* **Registrar solicitud de Inspeccion de calidad:** Se ingresa los datos de una solicitud de inspección de calidad, solo con los datos inciales previos a la inspección, por lo que algunas se encuentran aún como NULL
* **Revisar Inspecciones de calidad:** Ver detalles de todas o una parte de las inspecciones, según los parámetros de búsqueda que ingresa el usuario.
* **Registrar datos de inspeccion de calidad:** El usuario se encarga de ingresar los datos restantes de una inspección de calidad como la cantidad de defectos, resultado y descripcion; además el estado cambia a inspeccionado.
  
### PCP 
* **Ingresar pedidos a la línea de producción:** Se designará una orden de producción por cada orden de pedido solicitado.
* **Programar producción:** Se ingresa datos de programación de fechas, responsables y dimensiones del pedido, para luego ser registrado.
* **Controlar producción:** El usuario puede revisar los detalles de la producción y tomar una decisión según el estado.
* **Reprogramar producción:** Se ingresa nuevos datos de programación de fechas, responsables y dimensiones del pedido, para luego ser registrado.
* **Visualizar orden de trabajo:** El usuario puede revisar a detalle e imprimir la orden de trabajo según la orden de producción.

**[Ir a la seccion 6](6-stack.md)**

***[Regresar al índice](./entregable%203-indice.md)***
