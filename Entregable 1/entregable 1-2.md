# Entregable 1 del proyecto

## 2. To Be

### 2.1 Diagrama de Procesos - To BE

#### Área de Almacén  Central

![Diagrama de Área de Almacén Central](Diagramas/To%20be/Diagrama%20de%20procesos%20de%20Vircatex%20-%20Almacen%20central%20V2.png)

#### Área de Corte

![Diagrama de Área de Corte](Diagramas/To%20be/Diagrama%20de%20procesos%20de%20Vircatex%20-%20Area%20de%20Corte%20V2.png)

#### Área de Confección

![Diagrama de Área de Confección](Diagramas/To%20be/Diagrama%20de%20procesos%20de%20Vircatex%20-%20Area%20de%20Confeccion%20V2.png)


#### Área de Almacén de Tránsito

![Diagrama de Área de Almacén de Tránsito](Diagramas/To%20be/Diagrama%20de%20procesos%20de%20Vircatex%20-%20Almacen%20de%20transito%20V2.png)

#### Área de Acabados

![Diagrama de Área de Acabados](Diagramas/To%20be/Diagrama%20de%20procesos%20de%20Vircatex%20-%20Area%20de%20acabados%20V2.png)


#### Área de Inspección de calidad

![Diagrama de Área de Calidad](Diagramas/To%20be/Diagrama%20de%20procesos%20de%20Vircatex%20-%20Area%20de%20calidad%20V2.png)

#### Área de PCP

![Diagrama de Área de PCP](Diagramas/To%20be/Diagrama%20de%20procesos%20de%20Vircatex%20-%20Area%20de%20PCP%20V2.png)

### 2.2 Módulos

#### Módulos por funcionalidad

**- Área de corte**

  - Descripción: El área de corte en la industria textil es un sector fundamental donde se lleva a cabo el proceso de corte de las telas para la confección de prendas. En esta área, se reciben las telas, se preparan las órdenes de corte, se programan las máquinas de corte, se realizan los cortes de tela siguiendo patrones específicos, se clasifican en lotes las piezas cortadas y se envían al almacén central. Además, en el área de corte se gestionan las mermas, que son los desperdicios generados durante el proceso de corte.
    
  - Responsabilidades:

    
    A.	Preparación de la orden de corte: Organizar y preparar las órdenes de corte, asegurando la correcta distribución de las telas y los patrones a seguir.
    
    B.	Programación de las máquinas de corte: Configurar y programar las máquinas de corte para realizar los cortes de tela de acuerdo con las especificaciones de las órdenes.
    
    C.	Corte de tela: Realizar los cortes de tela siguiendo los patrones establecidos y asegurando la precisión en las medidas.
    
    D.	Clasificación en lotes de las piezas cortadas: Organizar y clasificar las piezas cortadas según los patrones y tamaños requeridos.
    
    E.	Gestión de mermas: Registrar y gestionar los desperdicios o mermas generados durante el proceso de corte, asegurando un control adecuado de los materiales utilizados.
    
  - Interacción:Con el módulo de **PCP**, ya que de esa área se reciben las ordenes de trabajo y con el módulo de **calidad**, después de realizado el corte, clasificado por lotes se le envía al área de calidad.

**- Área de confección**

  - Descripción: El área de confección en la industria textil es un sector fundamental donde se lleva a cabo el proceso de confección de las telas cortadas previamente. En esta área, se reciben las telas cortadas y las ordenes de confección, se preparan el plan de confección para cada división de confección y la guía para cada costurero, se crea un prototipo de confección enviandolo a calidad, se registra el progreso diario de cada costurero, se registra un reporte final al final de cada orden de confección y se envían al almacén central.
    
  - Responsabilidades:
    
    A.	Preparación del plan de confección: Registrar los planes de confección que seguira cada division para la realización de la orden de confección recibida.
    
    B.	Preparación de la guía de confección: Registrar las intrucciones que debe realizar el costurero de la división y asignar a los costureros que realizaran esa orden de confección.
    
    C.	Registro de prototipo: Registra el prototipo de confección para su inspección en calidad.
    
    D.	Registro de reportes diarios: Registrar el progreso de cada costurero en su labor en la realización de las ordenes de confección confirmando su envio al almacén central.
    
    E.	Registro de reportes finales: Registrar el reporte de la orden de confección finalizada confirmando el termino de la orden de confección.
    
  - Interacción:Con el módulo de **PCP**, ya que de esa área se reciben las ordenes de trabajo; con el módulo de **almacén central** ya que ellos guardan los lotes de confección en proceso y con el módulo de **calidad** que inspecciona el prototipo elaborado.


#### **- Procesos de Acabados**

El proceso de acabados en nuestra empresa textil comienza con la recepción y clasificación de las prendas por el Supervisor de Acabado, seguido por su procesamiento mediante actividades como planchado, hangteado, embolsado y embalaje, llevadas a cabo por los operarios de máquinas. Posteriormente, las prendas son sometidas a una rigurosa inspección de calidad a cargo del Inspector de Calidad para garantizar que cumplan con los estándares establecidos. En caso de detectarse prendas defectuosas, se genera un informe y se gestionan adecuadamente. Finalmente, las prendas aprobadas son despachadas por el Supervisor de Acabado para su distribución a clientes o puntos de venta, marcando así el cierre del proceso de acabados. Este flujo de trabajo garantiza la calidad y eficiencia en la preparación de nuestras prendas antes de llegar a manos de nuestros clientes.

  - Responsabilidades:

    A. Verificación de lotes de prendas: Se registra que todo tipo de prenda esté completo para su trabajo con los acabados.

    B. Resgistro de acabados: Registrar el estado de cada acabado según la secuencia interna de la empresa y la necesidad de acabados por prendas.

    C. Registro de reportes finales: Registrar los diferencetes reportes por encargados del área para el seguimiento de procesos internos.

  - Interacción:

  Con el módulo de almacén de tránsito: Para que le envíe los lotes que serán procesados por los acabados.
  Con el módulo de Calidad: Para que dé el visto bueno a los cabados y los registre en el sistema, luego de ello, el supervisor podrá dar por acabado el proceso total de acabados del pedido inicial por parte del cliente final.

## 3. Requerimientos

### 3.1 Requerimientos funcionales

#### **Caso de uso N°1: Abastecimiento de materia prima para producción**

| **Objetivo:** | Abastecer de manera eficiente y oportuna la materia prima necesaria para la producción de prendas en Vircatex.|
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso de abastecimiento de materia prima, desde la recepción de pedidos de producción hasta la entrega de la materia prima en el área de producción. | 
| **Actores Primarios:** | Jefe de almacén, Almacenero.| 
| **Precondiciones:** | Se cuenta con un sistema de gestión de inventario actualizado, además de conocer los proveedores y poseer las condiciones para almacenar la materia prima y posteriores materiales.| 
| Paso | Acción |
| 1    | El jefe de almacén  realiza la recepción del pedido y también continua con la planificación |
| 2    | Se verifica en el sistema de gestión de inventario si hay suficiente materia prima disponible para el pedido. |
| 3    | Si no hay suficiente materia prima disponible, se genera un pedido al proveedor. |
| 4    | Se recibe la materia prima del proveedor y se verifica su calidad. |
| 5    | Se almacena la materia prima en el lugar adecuado según su tipo y características. |
| 6    | Se selecciona la materia prima según el pedido de producción y se prepara para su entrega al área de producción. |
| 7    | Se entrega la materia prima en el área de producción junto con la documentación correspondiente. |
| 8    | Finaliza el caso. |

#### **Caso de uso N°2: Área de corte**

| **Objetivo:** | 2.1 Visualizar el orden de tranajo |
|------|--------|
| **Descripción:** | El caso de uso se centra en la recepción y la visualización el detalle de orden de trabajo, los detalles que debe tener el corte. | 
| **Actores Primarios:** | Jefe de corte.| 
| **Precondiciones:** | La orden de trabajo se recibe de almacén.| 
| Paso | Acción |
| 1    | El jefe de corte accede al sistema de Vircatex. |
| 2    | El jefe de corte selecciona el dia para ver los detalles de orden de trabajo. |
| 3    | El jefe de corte recibe los detalles de ordenes de trabajo. |
| 4    | El jefe de corte visualiza un resumen de las órdenes de corte pendientes, indicando la cantidad de tela requerida y la prioridad. |
| 5    | El jefe de corte revisa correctamente las ordenes de trabajo. |
| 6    | El jefe de corte cierra el sistema. |
| 7    | Finaliza el caso. |

| **Objetivo:** | 2.2 Agregar ordenes de trabajo |
|------|--------|
| **Descripción:** | El caso de uso se centra en agregar las ordenes de trabajo, si almacen omiió una orden de trabajo se le agrega. | 
| **Actores Primarios:** | Jefe de corte.| 
| **Precondiciones:** | Revision de detalles de orden de trabajo.| 
| Paso | Acción |
| 1    | El jefe de corte accede al sistema de Vircatex. |
| 2    | El jefe de corte selecciona el dia para ver los detalles de orden de trabajo. |
| 3    | El jefe de corte recibe los detalles de ordenes de trabajo. |
| 4    | El jefe de corte visualiza un resumen de las órdenes de corte pendientes, indicando la cantidad de tela requerida y la prioridad. |
| 5    | El jefe de corte revisa correctamente las ordenes de trabajo. |
| 6    | El jefe de corte observa que falta ordenes de trabajo. |
| 7    | El jefe de corte agrega las ordenes de trabajo restantes. |
| 8    | El jefe de corte cierra el sistema. |
| 9    | Finaliza el caso. |

| **Objetivo:** | 2.3 Programar maquinas |
|------|--------|
| **Descripción:** | El caso de uso se centra en programar las máquinas de corte de acuerdo al orden de trabajo. | 
| **Actores Primarios:** | Operario de corte.| 
| **Precondiciones:** | Revisión correcta de detalles de orden de trabajo.| 
| Paso | Acción |
| 1    | El Operario de corte accede al sistema de Vircatex. |
| 2    | El Operario de corte recibe los detalles de orden de trabajo verificado. |
| 4    | El Operario de corte visualiza un resumen de las órdenes de corte pendientes, indicando la cantidad de tela requerida y la prioridad. |
| 5    | El Operario de corte presiona programar, donde se visualizará las configuraciones. |
| 6    | El Operario de corte selecciona maquiana, estilo, tamaño, y hora inico. 
| 7    | El Operario de corte vizualiza el detalle programar maquina para confirmar la progrmacion de la máquina. |
| 8    | Finaliza el caso. |

| **Objetivo:** | 2.4 Verificar detalle lote de corte |
|------|--------|
| **Descripción:** | El caso de uso se centra en la visualización del corte realizado de la tela, sus caracteristicas finales, si presenta merma. | 
| **Actores Primarios:** | Operario de corte.| 
| **Precondiciones:** | Revision correcta de detalles de orden de trabajo.| 
| Paso | Acción |
| 1    | El Operario de corte accede al sistema de Vircatex. |
| 2    | El Operario de corte visualiza el detalle de corte. |
| 3    | El Operario de corte verifica si todo esta en orden, si presenta merma o no. |
| 4    | Si presenta corte el lote para se envia la merma al almacén. |
| 5   | Finaliza el caso. |

#### **Caso de uso N°3: Registro y Control de Prendas Acabadas**

| **Objetivo:** | Permitir que los inspectores de calidad registren y controlen el proceso de inspección de las prendas acabadas para garantizar su calidad antes del envío.|
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso mediante el cual los inspectores de calidad llevan a cabo la inspección final de las prendas acabadas para asegurar que cumplan con los estándares de calidad establecidos por la empresa textil antes de su envío. | 
| **Actores Primarios:** | Inspector de Calidad, Operario de Máquinas.| 
| **Precondiciones:** | Las prendas han pasado por el proceso de acabado y están listas para la inspección final de calidad.| 
| Paso | Acción |
| 1    | El Inspector de Calidad accede al sistema de registro y control de calidad. |
| 2    | El sistema muestra las prendas disponibles para inspección junto con los detalles de su proceso de acabado. |
| 3    | El Inspector de Calidad selecciona una prenda para inspeccionar y registra la información correspondiente en el sistema, como el tipo de prenda y el número de lote. |
| 4    | El Inspector de Calidad lleva a cabo la inspección visual y funcional de la prenda, verificando aspectos como costuras, tejido, color y cualquier defecto o irregularidad. |
| 5    | Si se encuentran defectos, el Inspector de Calidad registra los detalles y la acción correctiva necesaria en el sistema. |
| 6    | Si la prenda pasa la inspección, el Inspector de Calidad marca la prenda como aprobada en el sistema. |
| 7    | El sistema actualiza el estado de la prenda y registra la información de la inspección. |
| 8    | El Operario de Máquinas recibe la notificación de que la prenda ha pasado la inspección y procede con el embalaje y preparación para el envío. |
| 9    | El Inspector de Calidad continúa con la inspección de las siguientes prendas de manera similar. |
| 10   | El caso termina. |

#### **Caso de uso N°4: Inspección de calidad de avíos**

| **Objetivo:** | Inspeccionar la calidad de un lote de materias primas que recibe a la empresa textil |
|------|--------|
| **Descripción:** | Este caso de uso se centrará en un tipo de lote de avíos (botones), el cual se debe someter a un proceso de inspección de calidad para poder proceder a su uso dentro de la fabricación de prendas| 
| **Actores Primarios:** | Jefe de calidad, Auditor de calidad.| 
| **Precondiciones:** | El lote de botones se encuentra en el almacén y se encuentra listo para poder realizar la inspección de calidad. | 
| Paso | Acción |
| 1    | El jefe de calidad recibe un mensaje del área de almacén que han recibido un lote de botones y requiere una inspección de calidad |
| 2    | El jefe de calidad comunica al auditor de calidad que realice una inspección de calidad |
| 3    | El auditor de calidad separa una muestra representativa del lote de botones |
| 4    | El auditor de calidad procede a medir el nivel aceptable de calidad, que debe ser mínimo del 10% |
| 5    | El auditor de calidad repite el proceso en caso el primer resultado no sea satisfactorio |
| 6    | El auditor de calidad informa al jefe de calidad sobre los resultados en el lote de botones |
| 7    | El jefe de calidad procede a redactar un reporte general a gerencia sobre los resultados de inspección de calidad en el lote de botones |
| 8    | El caso termina |

#### **Casos de uso N°5: Área de confección**

| **Objetivo:** | 5.1 Registrar plan de confeccion por división |
|------|--------|
| **Descripción:** | Este caso de uso se centra en elaborar un plan de confeccion para cada división de acuerdo al plan de confección hecho por PCP. | 
| **Actores Primarios:** | Jefe de Confección | 
| **Precondiciones:** | PCP ha elaborado un plan de confección para la orden de trabajo recibida. | 
| Paso | Acción |
| 1   | El jefe de Confección recibe la notificacion de un plan de confección. |
| 2   | El jefe de Confección accede al sistema. |
| 3   | El jefe de Confección revisa el plan de confección. |
| 4   | El jefe de Confección elabora planes de confección para cada división. |
| 5   | El jefe de Confección guarda los planes de confección por división. |
| 6   | El jefe de Confección cierra el sistema. |
| 7   | Finaliza el caso. | 
| **Flujo alternativo:** | 5.1 El jefe hace clic en "cancelar" para no guardar los planes de confección por división. | 
| **Poscondiciones:** | EL sistema almacena los planes de confección por división y notifica a cada supervisor de división |

| **Objetivo:** | 5.2 Registrar guía de confección |
|------|--------|
| **Descripción:** | Este caso de uso se centra en elaborar un guía de confección de acuerdo al plan de confección por división. | 
| **Actores Primarios:** | Supervisor de división | 
| **Precondiciones:** | El jefe de Confección ha elaborado un plan de confección por división. | 
| Paso | Acción |
| 1   | El supervisor de división recibe la notificacion de un plan de confección para su división. |
| 2   | El supervisor de división accede al sistema. |
| 3   | El supervisor de división revisa el plan de confección de su división. |
| 4   | El supervisor de división elabora una guía de confección. |
| 5   | El supervisor de división guarda los planes de confeccion por division. |
| 6   | El supervisor de división cierra el sistema. |
| 7   | Finaliza el caso. |
| **Flujo alternativo:** | 5.1 El supervisor hace clic en "cancelar" para no guardar la guía de confección. | 
| **Poscondiciones:** | EL sistema almacena la guía de confección y notifica a todos los costureros de su división. |

| **Objetivo:** | 5.3 Visualizar guía de confección |
|------|--------|
| **Descripción:** | Este caso de uso se centra la visualización de la guía de confección. | 
| **Actores Primarios:** | Costurero | 
| **Precondiciones:** | El supervisor de división ha elaborado una guía de confección. | 
| Paso | Acción |
| 1   | El costurero recibe la notificacion de una guía de confección. |
| 2   | El costurero accede al sistema. |
| 3   | El costurero visualiza la guía de confección. |
| 4   | Cierra el sistema. |
| 5   | Finaliza el caso. | 
| **Poscondiciones:** | - |

| **Objetivo:** | 5.4 Registrar progreso del costurero |
|------|--------|
| **Descripción:** | Este caso de uso se centra en el registro del progreso diario del costurero en la confección. | 
| **Actores Primarios:** | Supervisor de división | 
| **Precondiciones:** | - | 
| Paso | Acción |
| 1   | El supervisor de división accede al sistema. |
| 2   | El supervisor de división entra a la opción "Registrar progreso del costurero". |
| 3   | El supervisor de división selecciona al costurero que va a registrar. |
| 4   | El supervisor de división registrar progreso del costurero. |
| 5   | El supervisor de división guarda el progreso del costurero. |
| 6   | El supervisor de división selecciona otro costurero. |
| 7   | Finaliza el caso. | 
| **Poscondiciones:** | - |

| **Objetivo:** | 5.5 Registrar reporte de confección diaria |
|------|--------|
| **Descripción:** | Este caso de uso se centra en elaborar un reporte de confección diaria. | 
| **Actores Primarios:** | Supervisor de división | 
| **Precondiciones:** | El Supervisor de división debe haber registrado el progreso de todos los costureros. | 
| Paso | Acción |
| 1   | Al registrar a todos los costureros, el supervisor de división recibe la pantalla de "Registrar reporte". |
| 2   | El supervisor de división selecciona la opción "Aceptar". |
| 3   | El supervisor de división elabora un reporte de confección diaria. |
| 4   | El supervisor de división guarda el reporte de confección diaria. |
| 5   | Cierra el sistema. |
| 6   | Finaliza el caso. |
| **Flujo alternativo:** | 5.1 El supervisor hace clic en "cancelar" para no guardar la guía de confección. | 
| **Poscondiciones:** | EL sistema almacena el reporte de confección diaria y notifica al jefe de Confección. |

| **Objetivo:** | 5.6 Verificar guía de confección |
|------|--------|
| **Descripción:** | Este caso de uso se centra en verificar el reporte de confección diaria. | 
| **Actores Primarios:** | Jefe de Confección | 
| **Precondiciones:** | El Supervisor de división ha elaborado un reporte de confección diaria. | 
| Paso | Acción |
| 1   | El jefe de Confección recibe la notificacion de un reporte de confección diaria. |
| 2   | El jefe de Confección accede al sistema. |
| 3   | El jefe de Confección revisa el reporte de confección diaria. |
| 4   | El jefe de Confección selecciona la opción "Verificado". |
| 6   | Cierra el sistema. |
| 7   | Finaliza el caso. |
| **Flujo alternativo:** | 4.1 El jefe de Confección selecciona la opción "Corregir". | 
| **Poscondiciones:** | - |

| **Objetivo:** | 5.5 Registrar reporte de confección final |
|------|--------|
| **Descripción:** | Este caso de uso se centra en elaborar un reporte de confección final. | 
| **Actores Primarios:** | Jefe de Confección | 
| **Precondiciones:** | El Supervisor de división debe haber indicado el fin de la confección. | 
| Paso | Acción |
| 1   | El jefe de Confección recibe la notificacion de la finalizacion de la confección. |
| 2   | El jefe de Confección accede al sistema. |
| 3   | El jefe de Confección revisa los reportes de confección diaria de la orden de trabajo. |
| 4   | El jefe de Confección elabora un reporte de confección final. |
| 4   | El jefe de Confección guarda el reporte de confección final. |
| 5   | Cierra el sistema. |
| 6   | Finaliza el caso. |
| **Flujo alternativo:** | - | 
| **Poscondiciones:** | EL sistema almacena el reporte de confección final. |

#### **Caso de uso N°6: Area de transporte**

| **Objetivo:** | 6.1 Verificar el numero de cajas |
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso de registro del conteo por parte del de cajas recibidas que fueron enviadas por el area de confeccion | 
| **Actores Primarios:** | Jefe de almacen de transito | 
| **Precondiciones:** | El lote de prendas en cajas ingresa al área de transporte desde el area de confeccion | 
| Paso | Acción |
| 1    | El Jefe de almacen de transito ingresa al sistema|
| 2    | El Jefe de almacen de transito contabiliza las cajas recibidas |
| 3    | El Jefe de almacen de transito ingresa en cada campo las cantidades y datos correspondientes segun su conteo |
| 4    | El Jefe de almacen de transito da click en "Continuar" |
| 5    | El Jefe de almacen de transito pasara al siguiente frame automaticamente si los datos estan correctos|
| 6   | Finaliza el caso. |
| **Flujo alternativo:** | 4.1 El Jefe de almacen de transito visualizara un mensaje "Al parecer la cantidad contada no coincide con el envio" |
|                        | 4.2 El Jefe de almacen de transito dara click en "actualiza conteo" actualizara los datos del conteo y dara click en "Siguiente" |
| -   | Finaliza el caso. |
| **Flujo alternativo:** | 4.1.1 El Jefe de almacen de transito dara click en "generar reporte" |
| - | Finaliza el caso. | 
| **Poscondiciones:** | - | 

| **Objetivo:** | 6.2 Verificar prendas falladas |
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso de registro del conteo de prendas falladas que fueron enviadas por el area de confeccion | 
| **Actores Primarios:** | Operario de recepccion | 
| **Precondiciones:** | Contabilizacion y clasificacion de cajas recepcionadas en el area de almacen de transito | 
| Paso | Acción |
| 1    | El Operario de recepccion realiza la verificacion manual de las prendas por lote |
| 2    | El Operario de recepccion ingresa en cada campo las cantidades y datos correspondientes segun su verificacion |
| 3    | El Operario de recepccion dara click en "agregar" |
| 4    | El Operario de recepccion visualizara los datos agregados en la tabla |
| 5    | El Operario de recepccion dara click en "Continuar" |
| 6    | El Operario de recepccion pasara al siguiente frame automaticamente si no existen datos en la tabla |
| 7   | Finaliza el caso. |
| **Flujo alternativo:** | 5.1 El Operario de recepccion visualizara un mensaje "¿Desea generar el reporte?" |
|                        | 5.2 El Operario de recepccion dara click en "actualizar datos" actualizara los datos de la verificacion y dara click en "Siguiente" |
| -   | Finaliza el caso. |
| **Flujo alternativo:** | 5.1.1 El El Operario de recepccion dara click en "generar reporte" |
| - | Finaliza el caso. | 
| **Poscondiciones:** | - | 

| **Objetivo:** | 6.3 Seleccionar lote a inventariar |
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso de seleccion del lote a realizar el conteo | 
| **Actores Primarios:** | Operario de conteo | 
| **Precondiciones:** | Exclusion de prendas falladas | 
| Paso | Acción |
| 1    | El Operario de conteo ingresa los datos correpondientes en los campos asignados |
| 2    | El Operario de conteo da click en "siguiente" |
| - | Finaliza el caso. | 
| **Poscondiciones:** | - |

| **Objetivo:** | 6.4 Generar plantilla de conteo por lote |
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso de generacion de una tirilla de conteo por lote para el conteo | 
| **Actores Primarios:** | Operario de conteo | 
| **Precondiciones:** | Seleccionar el lote a inventariar | 
| Paso | Acción |
| 1    | El Operario de conteo ingresa el codigo de barra del producto o lo pistolea con un lector de codigo de barras |
| 2    | El Operario de conteo da click en "Insertar" |
| 3    | El Operario de conteo visualizara los datos en la tbla y dara click en "siguiente"|
| - | Finaliza el caso. | 
| **Poscondiciones:** | - |

| **Objetivo:** | 6.5 Impresion de plantilla de conteo |
|------|--------|
| **Descripción:** | Este caso de uso describe la seleccion de la plantilla de conteo y su impresion| 
| **Actores Primarios:** | Operario de conteo | 
| **Precondiciones:** | Generar la plantilla de conteo | 
| Paso | Acción |
| 1    | El Operario de conteo dara click en "ingresar plantilla" y la visualizara en la tabla  |
| 2    | El Operario de conteo da click en "imprimir plantilla" |
| - | Finaliza el caso. | 
| **Poscondiciones:** | - |

| **Objetivo:** | 6.6 Inicio de conteo |
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso de conteo de prendas del lote seleccionado | 
| **Actores Primarios:** | Operario de conteo | 
| **Precondiciones:** | Seleccion del lote a inventariar | 
| Paso | Acción |
| 1    | El Operario de conteo realiza el conteo manual de las prendas por lote |
| 2    | El Operario de conteo ingresa en cada campo de la tabla las cantidades y datos correspondientes segun su conteo |
| 3    | El Operario de conteo dara click en "agregar dato" para su guardado |
| 4    | El Operario de conteo dara click en "Siguiente" para ver las diferencias |
| - | Finaliza el caso. | 
| **Poscondiciones:** | - | 

| **Objetivo:** | 6.7 Visualizacion de diferencias |
|------|--------|
| **Descripción:** | Este caso de uso describe la visualizacion de las primeras diferencias del conteo realizado| 
| **Actores Primarios:** | Operario de conteo | 
| **Precondiciones:** | Realizar el conteo de prendas | 
| Paso | Acción |
| 1    | El Operario de conteo visualizara su conteo y las difernecias positivas o ngetivas obtenidas segun el sistema  |
| 2    | El Operario de conteo da click en "continuar" |
| - | Finaliza el caso. | 
| **Poscondiciones:** | - |

| **Objetivo:** | 6.8 Inicio del 2do conteo |
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso del 2do conteo de prendas del lote seleccionado | 
| **Actores Primarios:** | Operario de conteo | 
| **Precondiciones:** | Realizar primer conteo | 
| Paso | Acción |
| 1    | El Operario de conteo realiza el conteo manual de las prendas por lote |
| 2    | El Operario de conteo ingresa en cada campo de la tabla las cantidades y datos correspondientes segun su conteo |
| 3    | El Operario de conteo dara click en "agregar dato" para su guardado |
| 4    | El Operario de conteo dara click en "Siguiente" para ver las diferencias |
| - | Finaliza el caso. | 
| **Poscondiciones:** | - | 

| **Objetivo:** | 6.9 Visualizacion de diferencias |
|------|--------|
| **Descripción:** | Este caso de uso describe la visualizacion las diferencias del 2do conteo realizado| 
| **Actores Primarios:** | Operario de conteo | 
| **Precondiciones:** | Realizar el 2do conteo de prendas | 
| Paso | Acción |
| 1    | El Operario de conteo visualizara su conteo y las difernecias positivas o ngetivas obtenidas segun el sistema  |
| 2    | El Operario de conteo da click en "continuar" |
| - | Finaliza el caso. | 
| **Poscondiciones:** | - |

| **Objetivo:** | 6.10 Cuadre de prendas |
|------|--------|
| **Descripción:** | Este caso de uso describe el cuadre exitoso del los 2 conteos realizados| 
| **Actores Primarios:** | Operario de conteo | 
| **Precondiciones:** | Realizar los 2 conteos de prendas | 
| Paso | Acción |
| 1    | El Operario de conteo visualizara el mensaje "Cuadre exitoso"  |
| 2    | El Operario de conteo da click en "Generar reporte general" |
| - | Finaliza el caso. | 
| **Poscondiciones:** | - |

#### **Casos de uso N°7: Área de acabados**

| **Objetivo:** | 7.1 Verificar ingreso de lote |
|------|--------|
| **Descripción:** | Este caso de uso describe verificación del nuevo lote al área de acabados por el Supervisor| 
| **Actores Primarios:** | Supervisor | 
| **Precondiciones:** | El lote de prendas ingresa al área de acabados desde almacén | 
| Paso | Acción |
| 1    | El supervisor ingresa al sistema|
| 2    | El supervisor mira el reporte de lotes |
| 3    | El supervisor ubica los reporte en la lista de la pantalla  |
| 4   | Finaliza el caso. |
| **Poscondiciones:** | - | 


| **Objetivo:** | 7.2 Realizar registro de procesos de acabados |
|------|--------|
| **Descripción:** | Este caso de uso describe los procesos registro de cada proceso de acabados (Hanteado, planchado, embalado) | 
| **Actores Primarios:** | Operario de máquinas | 
| **Precondiciones:** | Debe haber lotes de prendas registradas en el sistema | 
| Paso | Acción |
| 1    | El operario de máquinas ingresa al sistema |
| 2    | El operario de máquinas mira el reporte de lotes en item acabados |
| 3    | El operario de máquinas hace clic en el icono lupa para ver el detalle del lote. |
| 4    | El operario de máquinas mira el detalle del reporte. |
| 5    | El operario de máquinas procede a editar con el botón de editar |
| 6    | El operario de máquinas cambia el estado a "Proceso" o "Terminado"|
| 7    | El operario de máquinas cambia la etapa según el proceso que comienza |
| 8    | El operario de máquinas termina la edición con el botón "Aceptar Cambios" |
| 9   | Finaliza el caso. |
| **Poscondiciones:** | - | 

| **Objetivo:** | 7.3 Realizar reporte de acabados |
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso de la generacion e impresión del reporte del detalle de los procesos de acabados | 
| **Actores Primarios:** | Operario de máquinas | 
| **Precondiciones:** | - | 
| Paso | Acción |
| 1    | El operario de máquinas ingresa al sistema |
| 2    | El operario de máquinas mira el reporte de lotes en item acabados |
| 3    | El operario de máquinas hace clic en el icono lupa para ver el detalle del lote. |
| 4    | El operario de máquinas mira el detalle del reporte. |
| 5    | El operario de máquinas hace clic en el boton reporte |
| 6    | El sistema genera una vista en forma de popup con un documento generado del reporte |
| 7    | El operario de máquinas hace clic en aceptar para imprimir el reporte |
| 8   | Finaliza el caso. |
| **Flujo alternativo:** | 7.1 El operario de máquinas hace clic en cancelar para salir de la vista de popup y no imprimir  | 
| - | El operario de máquinas hace clic en cancelar para salir de la vista de popup y no imprimir  | 
| **Poscondiciones:** | - | 


| **Objetivo:** | 7.4 Realizar reporte de lote de prendas |
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso de la generacion e impresión del reporte del detalle de los lotes de prendas | 
| **Actores Primarios:** | Supervisor de acabados | 
| **Precondiciones:** | Debe haber lotes de prendas con estado de Terminado en el sistema | 
| Paso | Acción |
| 1    | El Supervisor de acabados ingresa al sistema |
| 2    | El Supervisor de acabados mira la lista de lotes en el sistemas |
| 3    | El Supervisor de acabadoss hace clic en el boton reporte |
| 4    | El sistema genera una vista en forma de popup con un documento generado del reporte |
| 5    | El Supervisor de acabados hace clic en aceptar para imprimir el reporte |
| 6   | Finaliza el caso. |
| **Flujo alternativo:** | 5.1 El operario de máquinas hace clic en cancelar para salir de la vista de popup y no imprimir  | 
| - | Supervisor de acabados hace clic en cancelar para salir de la vista de popup y no imprimir  |
| - | Finaliza el caso. | 
| **Poscondiciones:** | - | 


| **Objetivo:** | 7.5 Búsqueda de un lote de prenda |
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso búsqueda de un lote de prendas por el número de lote | 
| **Actores Primarios:** | Supervisor de acabados | 
| **Precondiciones:** | - | 
| Paso | Acción |
| 1    | El Supervisor de acabados ingresa al sistema. |
| 2    | El Supervisor de acabados mira la lista de lotes en el sistema. |
| 3    | El Supervisor de acabados hace clic en el campo de "Número de lote" y apreta enter |
| 4    | El sistema valida el valor ingresado con los registros de lotes |
| 5    | El sistema genera actualiza la lista de lotes al registro que corresponda con el campo anterior |
| 6    | El Supervisor de acabados mira la nueva lista en el sistema. |
| 7   | Finaliza el caso. |
| **Flujo alternativo:** | 5.1 Si el sistema no encuentra el valor aparece un popup que dice "No se encuentra lote en el sistema"  | 
| - | Supervisor de acabados hace clic en cancelar para salir de la vista de popup. | 
| - | Finaliza el caso. | 
| **Poscondiciones:** | - | 

| **Objetivo:** | 7.6 Búsqueda de un lote en acabados |
|------|--------|
| **Descripción:** | Este caso de uso describe el proceso búsqueda de un lote la sección de acabados.  | 
| **Actores Primarios:** | Operario de máquinas | 
| **Precondiciones:** | - | 
| Paso | Acción |
| 1    | El Operario de máquinas ingresa al sistema. |
| 2    | El Operario de máquinas ingresa al área de acabados en el submenú "acabados". |
| 3    | El Operario de máquinas  mira la lista de lotes en el sistema |
| 4    | El Operario de máquinas hace clic en el campo de "Número de lote" y apreta enter |
| 5    | El sistema valida el valor ingresado con los registros de lotes |
| 6    | El sistema genera actualiza la lista de lotes al registro que corresponda con el campo anterior |
| 7    | El Operario de máquinas mira la nueva lista en el sistema. |
| 8   | Finaliza el caso. |
| **Flujo alternativo:** | 5.1 Si el sistema no encuentra el valor aparece un popup que dice "No se encuentra lote en el sistema"  | 
| - | Operario de máquinas hace clic en cancelar para salir de la vista de popup. | 
| - | Finaliza el caso. | 
| **Poscondiciones:** | - | 

| **Objetivo:** | 7.7 Verificar la finalización de procesos de acabados |
|------|--------|
| **Descripción:** | Este caso de uso describe la verificación del supervisor del término de las subárea de acabados, el proceso de verificación de aprobación del área de calidad para luego realizar el lote a despacho o distrubución de la empresa  | 
| **Actores Primarios:** | Supervisor de acabados | 
| **Precondiciones:** | El Operario de máquinas tiene que haber de acabado con los procesos de acabados y registrado en el sistema el último proceso con estado de Terminado.  | 
| Paso | Acción |
| 1    | El Supervisor de acabados ingresa al sistema. |
| 2    | El Supervisor de acabados ingresa al área de acabados en el submenú "acabados". |
| 3    | El Supervisor de acabados  mira la lista de lotes de prendas en el sistema |
| 4    | El Supervisor de acabados hace visualiza el número de lote y hace clic en la lupa  situada junto a él. |
| 5    | El Supervisor de acabados visualiza el detalle de las etapas y con estado de "Terminado". |
| 6   | Finaliza el caso. |
| **Poscondiciones:** | En el detalle del lote aparece el campo distribución: "Enviado". | 

#### **Caso de uso N°8: Monitorear el proceso de producción de las prendas**

| **Objetivo:** | Controlar que los niveles de producción estén acorde a lo planificado |
|------|--------|
| **Descripción:** | Este caso de uso describe las revisiones periódicas de los niveles de producción de las áreas operativas.| 
| **Actores Primarios:** | Jefe de PCP, Analista PCP.| 
| **Precondiciones:** | El Jefe de PCP ha designado las actividades y metas semanales a las áreas de producción. | 
| Paso | Acción |
| 1    | Los jefes de área reciben un correo con notificación de sus metas de producción. |
| 2    | El Analista de PCP centraliza las metas en el WIP, principal herramienta de gestión. |
| 3    | El Analista de PCP programa los plazos para la salida de producción por áreas.|
| 4    | El Analista de PCP revisa la ejecución una semana después de la programación. |
| 5    | El Analista de PCP concluye si existió o no algún retraso en la salida de programación. |
| 6    | El Jefe de PCP reprograma las metas y reajusta las materias primas a utilizar. |
| 7    | El Analista de PCP actualiza los plazos para la salida de producción por áreas. |
| 8    | El Analista de PCP actualiza el WIP con los nuevos niveles de producción asignados. |
| 9    | El Jefe de PCP notifica a las demás áreas por los cambios realizados. |
| 10    | Finaliza el caso. |

### GLOSARIO

- **WIP**: Work in Progress, documento en Excel para hacer seguimiento a cada área de negocio en la empresa.
- **AQL**: (Acceptable Quality Level en inglés) se traduce como Límite de Calidad Aceptable en español y es un término relacionado con la cantidad máxima de defectos que los compradores y proveedores acordaron en un lote.
- **Ficha técnica**: documento de cada área donde se registran los datos pertinentes de seguimiento.
- **Prototipo**: Muestra de confección, es el producto final que se pasa al almacen central. Sirve para ver la calidad promedio de la confección.
- **Packing o Embalaje**: Empaque de cada unidad de pedido en una caja de ropa.
- **Auditoría**: Son procedimientos especializados que consisten en revisar, verificar, investigar y evaluar procesos específicos, gestión, energía, etc. A fin de subsanar, rediseñar según sea el caso.
- **Confección**: Es el proceso productivo para elaborar una prenda.
- **Corte**: Es un proceso de la industria de la confección, donde se corta el tizado, el cual contiene todos los patrones de la prenda.
- **Hangtado**: Subproceso de colocado de avíos de plástico y metal en prendas o telas para dar un acabado a la ropa.
- **Prenda acabada**: Es aquella prenda que ha sido sometida al proceso de acabado respecto a algunas características, como apariencia, tacto, etc., según las especificaciones de calidad.
- **Planchado**: Proceso que consiste en usar una máquina industrial para quitar las arrugas y defectos de doblaje de las prendas acabadas.
- **Prendas defectuosas**: Prendas terminadas que no pasan los estándares de calidad.

[Ver diagramas](Diagramas/diagramas.md)

**[Ir a la seccion 3](entregable%201-3.md)**

**[Regresar al índice](../README.md)**
