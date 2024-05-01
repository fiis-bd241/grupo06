CREATE TABLE Reporte_acabado
(
  fecha_transformacion DATE NOT NULL,
  id_caja_inicio NUMERIC(10) NOT NULL,
  id_caja_fin NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_caja_inicio, id_caja_fin),
  FOREIGN KEY (id_caja_inicio) REFERENCES Caja_detalle_inicial(id_caja_inicio),
  FOREIGN KEY (id_caja_fin) REFERENCES Caja_detalle_final(id_caja_fin)
);

CREATE TABLE Caja_detalle_final
(
  id_caja_fin NUMERIC(10) NOT NULL,
  id_caja NUMERIC(10) NOT NULL,
  id_prenda NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_caja_fin),
  FOREIGN KEY (id_caja) REFERENCES Caja(id_caja),
  FOREIGN KEY (id_prenda) REFERENCES Prenda(id_prenda)
);

CREATE TABLE Caja_detalle_inicial
(
  id_caja_inicio NUMERIC(10) NOT NULL,
  id_caja NUMERIC(10) NOT NULL,
  id_confeccion NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_caja_inicio),
  FOREIGN KEY (id_caja) REFERENCES Caja(id_caja),
  FOREIGN KEY (id_confeccion) REFERENCES Confeccion(id_confeccion)
);

CREATE TABLE Area
(
  id_area NUMERIC(1) NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_area),
  UNIQUE (nombre)
);

CREATE TABLE Reserva
(
  id_reserva CHAR(10) NOT NULL,
  estado VARCHAR(20) NOT NULL,
  largo FLOAT NOT NULL,
  ancho FLOAT NOT NULL,
  alto FLOAT NOT NULL,
  id_area NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_reserva),
  FOREIGN KEY (id_area) REFERENCES Area(id_area)
);

INSERT INTO Reporte_acabado (fecha_transformacion, id_caja_inicio, id_caja_fin) 
VALUES
    ('2024-05-01', 1, 1),
    ('2024-05-02', 2, 2),
    ('2024-05-03', 3, 3),
    ('2024-05-04', 4, 4),
    ('2024-05-05', 5, 5),
    ('2024-05-06', 6, 6),
    ('2024-05-07', 7, 7),
    ('2024-05-08', 8, 8),
    ('2024-05-09', 9, 9),
    ('2024-05-10', 10, 10),
    ('2024-05-11', 11, 11),
    ('2024-05-12', 12, 12),
    ('2024-05-13', 13, 13),
    ('2024-05-14', 14, 14),
    ('2024-05-15', 15, 15),
    ('2024-05-16', 16, 16),
    ('2024-05-17', 17, 17),
    ('2024-05-18', 18, 18),
    ('2024-05-19', 19, 19),
    ('2024-05-20', 20, 20);

INSERT INTO Caja_detalle_final (id_caja_fin, id_caja, id_prenda) 
VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5),
    (6, 6, 6),
    (7, 7, 7),
    (8, 8, 8),
    (9, 9, 9),
    (10, 10, 10);

INSERT INTO Caja_detalle_inicial (id_caja_inicio, id_caja, id_confeccion) 
VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5),
    (6, 6, 6),
    (7, 7, 7),
    (8, 8, 8),
    (9, 9, 9),
    (10, 10, 10);

INSERT INTO Reserva (id_reserva, estado, largo, ancho, alto, id_area) 
VALUES
    ('1', 'Activa', 10.5, 8.2, 4.3, 1),
    ('2', 'Pendiente', 7.8, 6.5, 3.9, 2),
    ('3', 'Activa', 9.2, 7.4, 4.1, 3),
    ('4', 'Cancelada', 6.6, 5.9, 3.5, 4),
    ('5', 'Activa', 8.7, 6.8, 3.7, 5),
    ('6', 'Pendiente', 11.1, 8.9, 4.6, 1),
    ('7', 'Activa', 7.3, 5.6, 3.2, 2),
    ('8', 'Activa', 9.8, 7.2, 4.0, 3),
    ('9', 'Pendiente', 6.4, 5.2, 3.0, 4),
    ('10', 'Activa', 8.5, 6.7, 3.8, 5);


INSERT INTO area (id_area, nombre) VALUES
(1, 'Almacén'),
(2, 'Corte'),
(3, 'Confeccion'),
(4, 'Información'),
(5, 'Administración');