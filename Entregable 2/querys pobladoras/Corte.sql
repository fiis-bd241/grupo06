INSERT INTO Tipo_corte (id_tipo_corte, descripcion) VALUES
('123', 'Largo de cuerpo'),
('124', 'Ancho de hombro'),
('125', 'Abertura de escote'),
('126', 'Caida de escote'),
('127', 'Ancho de faldon'),
('128', 'Largo de costado');

INSERT INTO Corte_medida (id_corte_medida, medida, id_tipo_corte) VALUES
(1000041234, 20.8, '123'),
(1000041235, 21, '124'),
(1000041236, 5, '125'),
(1000041237, 3, '126'),
(1000041238, 20, '127'),
(1000041239, 18, '128');

INSERT INTO Talla (id_talla, nombre) VALUES
(1, 'S'),
(2, 'M'),
(3, 'L'),
(4, 'XL'),
(5, 'XXL');

INSERT INTO Genero (id_genero, nombre) VALUES
(1, 'Masculino'),
(2, 'Femenino');

INSERT INTO Guia_corte_talla_genero (id_guia_corte, id_genero, id_talla) VALUES
(1003451232, 1, 3),
(1003451233, 2, 1),
(1003451234, 1, 4),
(1003451235, 2, 2),
(1003451236, 2, 1),
(1003451237, 1, 5);

INSERT INTO Guia_corte_detalle (id_corte_medida, id_guia_corte) VALUES
(1000041234, 1003451232),
(1000041235, 1003451234),
(1000041236, 1003451233),
(1000041237, 1003451235),
(1000041238, 1003451236),
(1000041239, 1003451237);

INSERT INTO Nombre_parte_prenda (id_nombre_parte_prenda, nombre) VALUES
(1, 'Delantero'),
(2, 'Espalda'),
(3, 'Manga'),
(4, 'Cuello'),
(5, 'Protector de cierre'),
(6, 'Garage cierre');

INSERT INTO Dimension_parte_prenda (id_dim_parte_prenda, id_guia_corte, id_nombre_parte_prenda) VALUES
(1076351421, 1003451232, 1),
(1076351422, 1003451233, 2),
(1076351423, 1003451234, 3),
(1076351424, 1003451235, 4),
(1076351425, 1003451236, 5);

INSERT INTO Dimension_corte (id_dim_corte, id_dim_materia_prima, id_dim_parte_prenda) VALUES
(1059284212, 1006034532, 1076351421),
(1059284213, 1006034533, 1076351422),
(1059284214, 1006034534, 1076351423),
(1059284215, 1006034535, 1076351424),
(1059284216, 1006034536, 1076351425);

INSERT INTO Tipo_lote (id_tipo_lote, nombre) VALUES
(1, 'Materia Prima'),
(2, 'Confeccion'),
(3, 'corte'),
(4, 'prenda');

INSERT INTO Lote (id_lote, cantidad, estado, fecha_creacion, id_tipo_lote, id_dim_corte, id_dim_confeccion, id_dim_materia_prima) values
(2003127123, 200, 'completado', '27/04/2024', 1, 1059284212, 1280003121, 1006034532),
(2003127124, 450, 'no iniciado', '06/05/2024', 2, 1059284213, 1280003122, 1006034533),
(2003127125, 500, 'en desarrollo', '01/05/2024', 3, 1059284214, 1280003123, 1006034534),
(2003127126, 470, 'en desarrollo', '29/04/2024', 4, 1059284215, 1280003124, 1006034535),
(2003127127, 550, 'no iniciado', '08/05/2024', 2, 1059284216, 1280003125, 1006034536);

INSERT INTO Orden_division (id_orden_division, estado, fecha_creacion, fecha_fin, id_lote, id_descripcion, id_tipo_division) VALUES
(3000012341, 'en desarrollo', '29/04/2024', '06/05/2024', 2003127123, 2100013112, 3321000123),
(3000012342, 'no inicado', '05/05/2024', '12/05/2024', 2003127124, 2100013113, 3321000124),
(3000012343, 'completado', '25/04/2024', '30/04/2024', 2003127125, 2100013114, 3321000125),
(3000012344, 'en desarrollo', '28/04/2024', '25/04/2024', 2003127126, 2100013115, 3321000126),
(3000012345, 'completado', '24/04/2024', '27/04/2024', 2003127127, 2100013116, 3321000127);

INSERT INTO Maquina (id_maquina, capacidad_total, estado, capacidad_usada, capacidad_disponible) VALUES
(002, 800, 'funcionando', 500, 300),
(003, 700, 'mantenimiento', 000, 700),
(004, 850, 'funcionando', 400, 450),
(005, 900, 'funcionando', 600, 300),
(006, 950, 'funcionando', 500, 450);

INSERT INTO Maquina_programacion_orden (id_maquina, id_orden_division, fecha_programacion, cantidad) VALUES
(002, 3000012341, '06/05/2024', 300),
(003, 3000012342, '25/04/2024', 500),
(004, 3000012343, '05/05/2024', 450),
(005, 3000012344, '28/04/2024', 300),
(006, 3000012345, '29/04/2024', 450);

INSERT INTO Corte (id_corte, id_lote, id_dim_corte, id_maquina) VALUES
(4002381231, 2003127123, 1059284213, 002),
(4002381232, 2003127124, 1059284214, 004),
(4002381233, 2003127125, 1059284215, 005),
(4002381234, 2003127126, 1059284216, 006);

INSERT INTO Reporte_uso (lote_usado, lote_producido, cantidad_merma, fecha_fin_uso) VALUES
(5000213121, 5392100012, 100, '01/05/2024'),
(5000213122, 5392100013, 120, '02/05/2024'),
(5000213123, 5392100014, 110, '03/05/2024'),
(5000213124, 5392100015, 104, '04/05/2024'),
(5000213125, 5392100016, 109, '05/05/2024');
