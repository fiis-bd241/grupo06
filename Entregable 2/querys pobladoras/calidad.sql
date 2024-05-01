INSERT INTO AQL_nivel (id_aql_nivel, nombre) VALUES
(1,'S1'),
(2,'S2'),
(3,'S3'),
(4,'S4'),
(5,'G1'),
(6,'G2'),
(7,'G3');

INSERT INTO AQL_codigo (id_aql_codigo, tamano_muestra) VALUES
('A',2),
('B',3),
('C',5),
('D',8),
('E',13),
('F',20),
('G',32),
('H',50),
('J',80),
('K',125),
('L',200),
('M',315),
('N',500),
('P',800),
('Q',1250),
('R',2000);

INSERT INTO AQL_significancia (id_aql_significancia, nivel_significancia) VALUES
(1,0.065),
(2,0.1),
(3,0.15),
(4,0.25),
(5,0.04),
(6,0.65),
(7,1),
(8,1.5),
(9,2.5),
(10,4),
(11,6.5);

INSERT INTO AQL_resultado_rango (id_aql_codigo, id_aql_significancia, max_aceptacion, min_rechazo) VALUES
('L',0.065,0,1),
('P',0.065,1,2),
('Q',0.065,2,3),
('R',0.065,3,4),
('K',0.1,0,1),
('N',0.1,1,2),
('P',0.1,2,3),
('Q',0.1,3,4),
('R',0.1,5,6),
('G',1.5,1,2),
('H',1.5,2,3),
('J',1.5,3,4),
('K',1.5,5,6),
('L',1.5,7,8),
('N',1.5,10,11),
('P',1.5,14,15),
('F',2.5,1,2),
('G',2.5,2,3),
('H',2.5,3,4),
('J',2.5,5,6),
('K',2.5,7,8),
('L',2.5,10,11),
('M',2.5,14,15),
('N',2.5,21,22),
('E',4,1,2),
('F',4,2,3),
('G',4,3,4),
('H',4,5,6),
('J',4,7,8),
('K',4,10,11),
('L',4,14,15),
('M',4,21,22),
('D',6,1,2),
('E',6,2,3),
('F',6,3,4),
('G',6,5,6),
('H',6,7,8),
('J',6,10,11),
('K',6,14,15),
('L',6,21,22);

INSERT INTO AQL_lote_rango (id_aql_lote_rango, min_lote, max_lote) VALUES
(1,2,8),
(2,9,15),
(3,16,25),
(4,26,50),
(5,51,90),
(6,91,150),
(7,151,280),
(8,281,500),
(9,501,1200),
(10,1201,3200),
(11,3201,10000),
(12,10001,35000),
(13,35001,150000),
(14,150001,500000),
(15,500001,99999999);

INSERT INTO Inspeccion_descripcion (id_descripcion, descripcion) VALUES
(1984732143, 'No se han encontrado fallas'),
(1233212208, 'No se ha realizado la inspeccion aun'),
(1431987205, 'Se ha encontrado fallos en los cuellos de los polos'),
(1436215147, 'Se ha encontrado fallos en la descripcion de las etiquetas'),
(1846573001, 'Se ha encontrado que las medidas de corte no coinciden'),
(1573541113, 'Se ha encontrado telas en mal estado');

INSERT INTO Tipo_resultado (id_resultado, descripcion) VALUES
(0, 'no aprobado'),
(1, 'aprobado');

INSERT INTO AQL_muestra (id_aql_nivel, id_aql_lote_rango, id_aql_codigo) VALUES
(6, 8, 'H'),
(6, 1, 'A'),
(5, 5, 'C'),
(7, 10, 'L'),
(7, 11, 'M'),
(5, 9, 'G'),
(6, 4, 'D'),
(5, 6, 'D'),
(6, 5, 'E');

INSERT INTO Inspeccion_calidad (id_inspeccion, fecha_inspeccion, id_lote, estado, cantidad_defectuosos, id_descripcion, id_aql_nivel, id_aql_lote_rango, id_aql_codigo, id_aql_significancia, id_resultado) VALUES
(1421124009,'2024-04-30',1147532681, 'inspeccionado', 0, 1984732143, 6, 8, 'H', 9, 1),
(1874563310,'2024-03-30',1234500789, 'inspeccionado', 5, 1233212208, 6, 8, 'H', 9, 0),
(1412156847,'2024-03-23',6768322410, 'en inspeccion', 0, 1431987205, 7, 10, 'L', 9, 0),
(1846132403,'2024-04-21',6818867703, 'en inspeccion', 0, 1984732143, 6, 4, 'D', 10, 0),
(1117655321,'2024-02-15',1345676059, 'no inspeccionado', 0, 1233212208, 5, 9, 'G', 9, 0),
(1045768307,'2024-04-25',3456784100, 'no inspeccionado', 0, 1233212208, 6, 11, 'M', 9, 0);
