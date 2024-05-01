-- nivel 1
INSERT INTO direccion (id_direccion, descripcion) VALUES
(100001, 'avenida jefe'),
(100002, 'avenida supervisor'),
(100003, 'jiron costura 1'),
(100004, 'jiron costurero 2');

INSERT INTO correo (id_correo, direccion_correo) VALUES
(100001, 'jefe@gmail.com'),
(100002, 'supervisor@gmail.com'),
(100003, 'costurero1@gmail.com'),
(100004, 'costurero2@gmail.com');

INSERT INTO telefono (id_telefono, numero) VALUES
(100001, '953695876'),
(100002, '864367865'),
(100003, '124466890'),
(100004, '797327422');

INSERT INTO cargo (id_cargo, nombre) VALUES
(1, 'Jefe'),
(2, 'Supervisor'),
(3, 'Costurero');

INSERT INTO tipo_lote (id_tipo_lote, nombre) VALUES
(1,'Materia prima'),
(2,'Corte'),
(3,'Confeccion');

INSERT INTO talla (id_talla, nombre) VALUES
(1,'XXXS'),
(2,'XXS'),
(3,'XS'),
(4,'S'),
(5,'M'),
(6,'L'),
(7,'XL'),
(8,'XXL'),
(9,'XXXL');

INSERT INTO genero (id_genero, nombre) VALUES
(1,'Masculino'),
(2,'Femenino');

INSERT INTO guia_confeccion_talla_genero (id_guia_confeccion, medida_longitud, medida_hombro, medida_pecho, medida_manga) VALUES
(1000000001, 60.5, 35.5, 24.5, 45),
(1000000002, 58.5, 35.5, 24.5, 46.5),
(1000000003, 58.5, 32.5, 28.5, 46.5);

INSERT INTO guia_confeccion_talla_genero (id_guia_confeccion, medida_longitud, medida_cintura, medida_cadera, medida_muslo) VALUES
(1000000004 , 95.5, 40.5, 42.5, 45.5),
(1000000005 , 95.5, 40.5, 42.5, 45.5),
(1000000006 , 45.5, 38.5, 41.5, 44.5);

INSERT INTO tipo_prenda (id_tipo_prenda, nombre) VALUES
(01,'Camisa'),
(02,'Polo'),
(03,'Camiseta'),
(04,'Sudadera'),
(05,'Blusa'),
(06,'Pantalon'),
(07,'Jean'),
(08,'Falda');

INSERT INTO estilo_prenda (id_estilo_prenda, nombre) VALUES
(01,'Casual'),
(02,'Clasico'),
(03,'Romantico'),
(04,'Vintage'),
(05,'Rockero'),
(06,'Deportivo');

INSERT INTO area (id_area, nombre) VALUES
(1, 'Almacen central'),
(2, 'Corte'),
(3, 'Confeccion'),
(4, 'Almacen de transito'),
(5, 'Acabados'),
(6, 'Calidad'),
(7, 'PCP');

-- nivel 2
INSERT INTO empleado (id_empleado, dni, nombre, primer_apellido, segundo_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo) VALUES
(10001, 72925346, 'Alejandro Manolo', 'Magno', 'Bonaparte', 3, 100001, 100001, 100001, 1),
(10002, 72923346, 'Luis Ignacio', 'De la Cruz', 'Yulca', 3, 100002, 100002, 100002, 2),
(10003, 72924346, 'Luisito', 'Perez', 'Godinez', 3, 100003, 100003, 100003, 3),
(10004, 72913246, 'Pablo', 'Chancana', 'Sulca', 3, 100004, 100004, 100004, 3);

INSERT INTO dimension_confeccion (id_dim_confeccion, id_guia_confeccion, id_talla, id_genero, id_tipo_prenda, id_estilo_prenda) VALUES
(1000000001, 1000000001, 5, 1, 1, 2),
(1000000002, 1000000004, 5, 1, 6, 6);

-- nivel 5
INSERT INTO lote (id_lote, id_tipo_lote, cantidad, estado, fecha_creacion, id_dim_confeccion) VALUES
(1000000001, 3, 2, 'En proceso', '23-04-2024', 1000000001),
(1000000002, 3, 2, 'Completado', '10-04-2024', 1000000002);

-- nivel 6
INSERT INTO confeccion (id_confeccion, id_lote, id_dim_confeccion, id_empleado) VALUES
(1000000011, 1000000001, 1000000001, 10003),
(1000000021, 1000000002, 1000000002, 10003),
(1000000022, 1000000002, 1000000002, 10004);
