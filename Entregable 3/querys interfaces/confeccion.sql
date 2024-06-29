-- Vistas

	-- Crear vista de ordenes de confección
	DROP VIEW IF EXISTS vista_op_confección;
	CREATE VIEW vista_op_confección AS
				SELECT op.id_orden_producción, op.fecha_inicio, op.fecha_fin, e.nombre AS estado
				FROM orden_producción op
				INNER JOIN dimension_confeccion dc ON dc.id_dim_confeccion = op.id_dim_confeccion
				INNER JOIN estado e ON e.id_estado = op.id_estado
				WHERE e.nombre <> 'Completado' AND e.nombre <> 'Cancelado'
				ORDER BY op.fecha_inicio DESC, op.fecha_fin DESC;

	-- Crear vista descripción de orden de confección
	DROP VIEW IF EXISTS vista_op_conf_descripción;
	CREATE VIEW vista_op_conf_descripción AS
		SELECT	op.id_orden_producción, op.fecha_inicio, op.fecha_fin, e.nombre AS estado,
				tp.nombre AS prenda, ep.nombre AS estilo,
				tl.nombre AS talla, gn.nombre AS genero,
				gc.medida_pecho, gc.medida_cintura, gc.medida_cadera,
			    gc.medida_hombro, gc.medida_longitud, gc.medida_manga, gc.medida_muslo
		FROM dimension_confeccion dc
		INNER JOIN tipo_prenda tp ON tp.id_tipo_prenda = dc.id_tipo_prenda
		INNER JOIN estilo_prenda ep ON ep.id_estilo_prenda = dc.id_estilo_prenda
		INNER JOIN talla tl ON tl.id_talla = dc.id_talla
		INNER JOIN genero gn ON gn.id_genero = dc.id_genero
		INNER JOIN guia_confeccion gc ON gc.id_guia_confeccion = dc.id_guia_confeccion
		INNER JOIN orden_producción op ON op.id_dim_confeccion = dc.id_dim_confeccion
		INNER JOIN estado e ON e.id_estado = op.id_estado;

	-- Crear vista de empleados de confección
	DROP VIEW IF EXISTS vista_emp_confección;
	CREATE VIEW vista_emp_confección AS
		SELECT e.id_empleado, e.nombre, e.primer_apellido, e.segundo_apellido
		FROM empleado e
		INNER JOIN area a ON a.id_area = e.id_area
		INNER JOIN cargo ca ON ca.id_cargo = e.id_cargo
		WHERE a.nombre = 'Confección' AND ca.nombre = 'Costurero';

	-- Crear vista de ordenes asignadas al empleado de confección
	DROP VIEW IF EXISTS vista_op_emp_conf;
	CREATE VIEW vista_op_emp_conf AS
		SELECT op.id_orden_producción, ea.id_empleado, ad.fecha_actividad
		FROM orden_producción op
		INNER JOIN actividad_diaria ad ON ad.id_orden_producción = op.id_orden_producción
		INNER JOIN empleado_actividad ea ON ea.id_actividad = ad.id_actividad;

	-- Crear vista de empleados con ordenes de confección
	DROP VIEW IF EXISTS vista_emp_ops_confección;
	CREATE VIEW vista_emp_ops_confección AS
		SELECT e.id_empleado, e.nombre, e.primer_apellido, e.segundo_apellido,
			   ad.id_actividad, ad.fecha_actividad, op.id_orden_producción
		FROM empleado e
		INNER JOIN empleado_actividad ea ON ea.id_empleado = e.id_empleado
		INNER JOIN actividad_diaria ad ON ad.id_actividad = ea.id_actividad
		INNER JOIN orden_producción op ON op.id_orden_producción = ad.id_orden_producción
		INNER JOIN area a ON a.id_area = op.id_area
		WHERE a.nombre = 'Confección';

	-- Crear vista de lotes de corte que se puede usar
	DROP VIEW IF EXISTS vista_lote_corte_emp;
	CREATE VIEW vista_lote_corte_emp AS
		SELECT	l.id_lote, op.id_orden_producción
		FROM lote l
		INNER JOIN dimension_corte dct ON dct.id_dim_corte = l.id_dim_corte
		INNER JOIN dim_confeccion_detalle dcd ON dcd.id_dim_corte = dct.id_dim_corte
		INNER JOIN dimension_confeccion dc ON dc.id_dim_confeccion = dcd.id_dim_confeccion
		INNER JOIN orden_producción op ON op.id_dim_confeccion = dc.id_dim_confeccion
		INNER JOIN estado e ON e.id_estado = l.id_estado
		WHERE e.nombre = 'Disponible';

-- Orden Confeccion 1

	-- Mostrar ordenes de producción de confección
	SELECT * FROM vista_op_confección;

	-- Filtros por estado
	SELECT * FROM vista_op_confección
	WHERE estado = 'No iniciado';

	SELECT * FROM vista_op_confección
	WHERE estado = 'En proceso';
	
	SELECT * FROM vista_op_confección
	WHERE estado = 'Atrasado';

	--Filtros por fecha
	SELECT * FROM vista_op_confección
	WHERE fecha_inicio >= '2024-02-04';

	SELECT * FROM vista_op_confección
	WHERE fecha_fin <= '2024-07-04';

	SELECT * FROM vista_op_confección
	WHERE fecha_inicio >= '2024-02-04' AND fecha_fin <= '2024-07-04';

-- Orden Confeccion 2
	
	-- Mostrar descripción de confección
	SELECT * FROM vista_op_conf_descripción
	WHERE id_orden_producción = 29;

-- Orden Confeccion 3

	-- Mostrar empleados
	SELECT * FROM vista_emp_confección;

	-- Filtros por empleado
	
	-- Por nombre
	SELECT * FROM vista_emp_confección
	WHERE nombre = 'Armida Bernardo';

	-- Por primer apellido
	SELECT * FROM vista_emp_confección
	WHERE primer_apellido = 'Vidal';

	-- Por segundo apellido
	SELECT * FROM vista_emp_confección
	WHERE segundo_apellido = 'Mena';

	-- Por nombre y primer apellido
	SELECT * FROM vista_emp_confección
	WHERE nombre = 'Nélida Albina' AND primer_apellido = 'Vidal';

	-- Por nombre y segundo apellido
	SELECT * FROM vista_emp_confección
	WHERE nombre = 'Armida Bernardo' AND segundo_apellido = 'Mena';

	-- Por primer_apellido y segundo apellido
	SELECT * FROM vista_emp_confección
	WHERE primer_apellido = 'Vidal' AND segundo_apellido = 'Mena';

	-- Por nombre, primer_apellido y segundo apellido
	SELECT * FROM vista_emp_confección
	WHERE nombre = 'Armida Bernardo' AND primer_apellido = 'Vidal' AND segundo_apellido = 'Mena';

	-- Asignar empleados
		-- Si es el primer empleado creado para la actividad de hoy
		INSERT INTO actividad_diaria (fecha_actividad, id_orden_producción)
		VALUES ('26/06/2024', 29);

	INSERT INTO empleado_actividad (id_empleado, id_actividad, cantidad_hecha)
	VALUES (24, 29, 0);

-- Ordenes Asignadas 1

	-- Mostrar ordenes asignadas de hoy
	SELECT id_orden_producción FROM vista_op_emp_conf
	WHERE id_empleado = 24 AND fecha_actividad = '19/04/2024';

-- Ordenes Asignadas 2

	-- Mostrar descripción de confección
	SELECT * FROM vista_op_conf_descripción
	WHERE id_orden_producción = 20;

-- Registro de progreso 1

	-- Mostrar Empleado con la cantidad de ordenes asignadas
	SELECT id_empleado, nombre, primer_apellido, segundo_apellido,
		   COUNT(id_actividad) AS ordenes
	FROM vista_emp_ops_confección
	WHERE fecha_actividad = '19/04/2024'
	GROUP BY id_empleado, nombre, primer_apellido, segundo_apellido;

	-- Filtros por empleado
	
	-- Por nombre
	SELECT id_empleado, nombre, primer_apellido, segundo_apellido,
		   COUNT(id_actividad) AS ordenes
	FROM vista_emp_ops_confección
	WHERE fecha_actividad = '19/04/2024'
	GROUP BY id_empleado, nombre, primer_apellido, segundo_apellido
	HAVING nombre = 'Nélida Albina';

	-- Por primer apellido
	SELECT id_empleado, nombre, primer_apellido, segundo_apellido,
		   COUNT(id_actividad) AS ordenes
	FROM vista_emp_ops_confección
	WHERE fecha_actividad = '19/04/2024'
	GROUP BY id_empleado, nombre, primer_apellido, segundo_apellido
	HAVING primer_apellido = 'Zorrilla';

	-- Por segundo apellido
	SELECT id_empleado, nombre, primer_apellido, segundo_apellido,
		   COUNT(id_actividad) AS ordenes
	FROM vista_emp_ops_confección
	WHERE fecha_actividad = '19/04/2024'
	GROUP BY id_empleado, nombre, primer_apellido, segundo_apellido
	HAVING segundo_apellido = 'Santamaria';

	-- Por nombre y primer apellido
	SELECT id_empleado, nombre, primer_apellido, segundo_apellido,
		   COUNT(id_actividad) AS ordenes
	FROM vista_emp_ops_confección
	WHERE fecha_actividad = '19/04/2024'
	GROUP BY id_empleado, nombre, primer_apellido, segundo_apellido
	HAVING nombre = 'Nélida Albina' AND primer_apellido = 'Zorrilla';

	-- Por nombre y segundo apellido
	SELECT id_empleado, nombre, primer_apellido, segundo_apellido,
		   COUNT(id_actividad) AS ordenes
	FROM vista_emp_ops_confección
	WHERE fecha_actividad = '19/04/2024'
	GROUP BY id_empleado, nombre, primer_apellido, segundo_apellido
	HAVING nombre = 'Nélida Albina' AND segundo_apellido = 'Santamaria';

	-- Por primer_apellido y segundo apellido
	SELECT id_empleado, nombre, primer_apellido, segundo_apellido,
		   COUNT(id_actividad) AS ordenes
	FROM vista_emp_ops_confección
	WHERE fecha_actividad = '19/04/2024'
	GROUP BY id_empleado, nombre, primer_apellido, segundo_apellido
	HAVING primer_apellido = 'Zorrilla' AND segundo_apellido = 'Santamaria';

	-- Por nombre, primer_apellido y segundo apellido
	SELECT id_empleado, nombre, primer_apellido, segundo_apellido,
		   COUNT(id_actividad) AS ordenes
	FROM vista_emp_ops_confección
	WHERE fecha_actividad = '19/04/2024'
	GROUP BY id_empleado, nombre, primer_apellido, segundo_apellido
	HAVING nombre = 'Nélida Albina' AND primer_apellido = 'Zorrilla' AND segundo_apellido = 'Santamaria';

-- Registro de progreso 2

	-- Mostrar ordenes de produccion asignadas al empleado
	SELECT id_orden_producción
	FROM vista_emp_ops_confección
	WHERE fecha_actividad = '19/04/2024' AND id_empleado = 19

	-- Registrar la cantidad
	UPDATE empleado_actividad
	SET cantidad_hecha = 20
	WHERE id_empleado = 19 
		  AND id_actividad = (SELECT id_actividad
							  FROM vista_emp_ops_confección
							  WHERE fecha_actividad = '19/04/2024' 
									AND id_empleado = 19 AND id_orden_producción = 8)

-- Registro de progreso 3

	-- Mostrar descripción de confección
	SELECT * FROM vista_op_conf_descripción
	WHERE id_orden_producción = 8;

-- Registro de progreso 4

	-- Mostrar la lista de lotes de corte que el empleado puede usar según su ordenes asignadas
	SELECT id_lote
	FROM vista_lote_corte_emp
	WHERE id_orden_producción IN (SELECT id_orden_producción
								  FROM vista_emp_ops_confección
								  WHERE fecha_actividad = '19/04/2024' AND id_empleado = 19);

	-- Insertar consumo del lote
	INSERT INTO registro_uso_lote (id_actividad, id_lote, cantidad_usada)
	VALUES ((SELECT id_actividad
		  	 FROM vista_emp_ops_confección
		  	 WHERE fecha_actividad = '19/04/2024' 
				   AND id_empleado = 19 AND id_orden_producción = 8) , 80, 15);



-- Pruebas de inserts/updates
BEGIN TRANSACTION;

-- Intentar el INSERT/UPDATE

-- Revertir la transacción para no afectar la base de datos
ROLLBACK;



-- Enviar lotes a almacén
SELECT l.id_lote, l.cantidad, l.id_actividad
FROM lote l
INNER JOIN dimension_confeccion dc ON dc.id_dim_confeccion = l.id_dim_confeccion
INNER JOIN estado e ON e.id_estado = l.id_estado
LEFT JOIN lote_entrada le ON le.id_lote = l.id_lote
WHERE le.id_entrada IS NULL;





