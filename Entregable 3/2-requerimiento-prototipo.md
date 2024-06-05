# Entregable 3 del proyecto
## Requerimientos e Interfaces
### 1. Almacén central 

### 2. Corte
| N°    | Requerimiento Funcional  | Descripción                                         | Impacto <br> (1) Bajo (2) Normal<br> (3) Alto (4) Muy alto |
|-------|--------------------------|-----------------------------------------------------|---------------------------------------------------|
| RV201 | Verificar la orden de producción| El jefe de corte debe verificar si la orden que recibe esta bien. | 3                                                 |
| RV202 |Registrar actividades diarias  | El jefe de corte va a registrar las actividades diarias, para el orte que maquinas va a realizar y de a cuerdo a que orden de producción.        | 4                                               |
| RV203 | Actividades diarias relaizadas | El jefe realizara un reporte donde se podra ver cuantas actividades diarias realizó cada máquina en un dia | 4                                                 |
| RV204 | Verificar los cortes que se realizaron por cada actividad       | El jefe va a verificar cuantos cortes se realizó por cada acitividad, con la cantidad de orden de producción  | 4                                                 |
| RV205 | Verificar lotes       | El jefe va a verificar cuantos lotes se está realizando por dia para ver la productividad  | 3                                                |
| RV206 | Verificar los cortes por orden de producción      | El jefe va a verificar el progreso de los cortes de cada orden de producción  | 4                                                 |
| RV207 | Ricibir las actividades a realizar       | El operario de corte va a recibir la actividad que va realizar por cada maquina  | 4                                                 |
| RV208 | Registrar cantidad de corte y la cantidad de lote usado    | El operario de corte va a registrar la cantidad de corte que se ha hecho y la cantidad que se uso en ese lote donde se encuentra el corte  | 4                                                 |

| N°    | Interfaz | Descripción                                                                 |
|-------|----------|-----------------------------------------------------------------------------|
| IV201 | Verificar la orden     | Pantalla para visualizar datos de la orden de producción     |
| IV202 | Registar datos de las actividades | Pantalla para registrar que maquina, la fecha y orden de producción. |
| IV203 | Revisar actividades     | Pantalla para visualizar los datos que va a realizar la maquina en el dia.           |
| IV204 | Registrar cantidad de corte y lote |Pantalla para registrar los datos de la cantidad de corte con la cantidad de lote usado. |
| IV205 | Revisar actividades diarias relaizadas     | Pantalla para visualizar las actividades diarias por maquina.           |
| IV206 | Verificar los cortes  | Pantalla para visualizar el detalle de los cortes que se realizaron por cada actividad. |
| IV207 | Verificar lotes x dia    | Pantalla para visualizar detalle de numero de lotes por dia en el mes.           |
| IV2028 | Verificar los cortes por orden  | Pantalla para visualizar el detalle del numero de cortes por la orden de producción. |


### 3. Confección 

### 4. Almacén de tránsito 

| N°    | Requerimiento Funcional  | Descripción                                         | Impacto <br> (1) Bajo (2) Normal<br> (3) Alto (4) Muy alto |
|-------|--------------------------|-----------------------------------------------------|---------------------------------------------------|
| RV401 | Verificar la orden de trabajo| El jefe de almacen de transito debe verificar si la orden trabajo que recepciona es correcta. | 4                                                 |
| RV402 |Verificar que los datos de la orden de trabajo sean correctos para recepcionar  | El jefe de almacen de transito debera visualizar los datos segun la orden de trabajo que recepciona y completar algunios datos como la nombre de quien recepciona       | 3                                               |
| RV403 |Verificar las cantidades de prendas llegadas en un lote  | El jefe de almacen de transito en conjunto con el operario de recepcion verificaran que las prendas que llegue en los lotes sean las estableciadas en la orden de trabajo        | 3                                               |
| RV404 | Editar, eliminar o agregar cantidades al lote de recibido | El operario de recepcion con autorizacion del jefe de almacen de trasnito podra editar, eliminar o agregar productos al lote recibido del area de confeccion | 3                                                 |
| RV405 | Confirmar cantidades       | El jefe de almacen de transito debera confirmar las cantidades editadas o iniciales llegadas en el lote segun la orden de trabajo para poder recepcionarlas  | 4                                                 |
| RV406 | Imprimir y enviar los documentos de recepcion      | el operario de recepcion debera imprimir los documentos de recpcion para entregarselas al jefe de almacen de trasnito y este las envie al area correspondiente.  | 3                                                |

| N°    | Interfaz | Descripción                                                                 |
|-------|----------|-----------------------------------------------------------------------------|
| IV401 | Inicio     | Pantalla para verificar y buscar la orden de trabajo a recepcionar.         |
| IV402 | Recepcion | Pantalla para mostrar datos generales de la orden de trabajo a recepcionar y completar los datos de quien recepciona. |
| IV403 | Conteo de productos  | Pantalla para realizar la verificacion del contenido de cada lote que se recepciona segun la orden de trabajo. Se podra editar, eliminar o añadir de ser necesario. |
| IV404 | Verificacion  | Pantalla que mostrara la verificacion de la recepcion si esque haya sufrido cambios para su posteior resultado final |
| IV405 | Resultado final  | Pantalla para mostrar los datos finales que se estan recepcionando  |
| IV406 | Documentos de recepcion | Pantalla para mostrar los documentos de recepcion e imprimirlos en formato .pdf |


### 5. Acabados

| N°    | Requerimiento Funcional  | Descripción                                         | Impacto <br> (1) Bajo (2) Normal<br> (3) Alto (4) Muy alto |
|-------|--------------------------|-----------------------------------------------------|---------------------------------------------------|
| RV501 | Verificar y buscar cajas | Pantalla para verificar y buscar cajas.  | 3                                                 |
| RV502 | Detalle por Caja   | Ver los detalles generales por caja.       | 4                                                |
| RV503 | Reporte | Pantalla para realizar el reporte online e impresion del reporte en pdf. | 2                                                |
| RV504 | Ver Operario      | Ver detalles basicos del operario | 2                                                |
| RV505 | Reporte por operario       | Pantalla para mostrar detalles de cajas asignadas por operarios y sus datos generales  | 4    |
| RV506 | Datos generales de acabados     | Verificar y modificación de acabados por cajas y prendas.  | 4    |

| N°    | Interfaz | Descripción                                                                 |
|-------|----------|-----------------------------------------------------------------------------|
| IV501 | Lote     | Pantalla para verificar y buscar cajas y hacer reporte.         |
| IV502 | Detalle de caja  | Pantalla para mostrar datos generales de cada caja y su prenda. |
| IV503 | Reporte  | Pantalla para realizar el reporte online e impresion del reporte en pdf. |
| IV504 | Operario  | Popup para mostrar datos básicos del operario. |
| IV505 | Busqueda y detalle de operario  | Pantalla para mostrar detalles de cajas asignadas por operarios y sus datos generales  |
| IV506 | Detalle de caja y acabados | Pantalla para verificar y modificación de acabados por cajas y prendas.  |



### 6. Calidad 

| N°    | Requerimiento Funcional  | Descripción                                         | Impacto <br> (1) Bajo (2) Normal<br> (3) Alto (4) Muy alto |
|-------|--------------------------|-----------------------------------------------------|---------------------------------------------------|
| RV601 | Registrar Solicitud de Inspeccion de calidad | El sistema debe permitir al usuario registrar datos de una solicitud de inspeccion de calidad | 4                                                 |
| RV602 | Revisar Inspecciones de Calidad | El sistema debe permitir al usuario revisar inspecciones de calidad | 3                                                 |
| RV603 | Registrar resultados de Inspeccion de calidad | El sistema debe permitir al usuario registrar datos de una inspeccion de calidad | 4                                                 |

| N°    | Interfaz | Descripción                                                                 |
|-------|----------|-----------------------------------------------------------------------------|
| IV601 | Registrar Solicitudes de Inspeccion | Pantalla para ingresar datos de solicitudes de inspeccion de calidad y registrarlas |
| IV602 | Revisar Inspecciones | Pantalla para visualizar datos sobre inspecciones de calidad |
| IV603 | Registrar datos de Inspeccion | Pantalla para ingresar datos de inspeccion de calidad y registrarlas |

### 7. PCP 

| N°    | Requerimiento Funcional  | Descripción                                         | Impacto <br> (1) Bajo (2) Normal<br> (3) Alto (4) Muy alto |
|-------|--------------------------|-----------------------------------------------------|---------------------------------------------------|
| RV701 | Ingresar orden de pedido a linea de producción | El sistema debe permitir al usuario revisar las órdenes de pedido e ingresar a la línea de producción.  | 4                                                 |
| RV702 | Programar órdendes de producción | El sistema debe permitir al usuario asignar una programación a la orden de producción.       | 4                                                |
| RV703 | Controlar órdenes de producción | El sistema debe permitir al usuario controlar las órdenes de producción. | 4                                                |
| RV704 | Reprogramar órdenes de producción | El sistema debe permitir al usuario reprogramar parcialmente o en su totalidad las órdenes de producción | 3                                                |
| RV705 | Visualizar órdenes de trabajo | El sistema debe permitir al usuario visualizar las órdenes de trabajo según las órdenes de producción.  | 2    |

| N°    | Interfaz | Descripción                                                                 |
|-------|----------|-----------------------------------------------------------------------------|
| IV701 | Registro de órdenes de pedido     | Pantalla para ver el registro de las órdenes de pedido e iniciar con la programación.        |
| IV702 | Programar producción | Pantalla para ingresar los datos para la programación de la Orden de Producción.         |
| IV703 | Controlar producción  | Pantalla para ver el registro de las órdenes de producción e iniciar con la reprogramación en caso sea necesario. |
| IV704 | Reprogramar producción | Pantalla para ingresar los nuevos datos para la reprogramación de la Orden de Producción. |
| IV705 | Visualizar orden de trabajo | Pantalla para mostrar el detalle de la orden de trabajo de una orden de producción y que permitirá hacer la impresión del mismo.  |



**[Ir a la seccion 3](3-sentencias-sql.md)**

***[Regresar al índice](./entregable%203-indice.md)***
