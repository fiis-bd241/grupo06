-- Tabla: direccion
CREATE TABLE direccion (
  id_direccion NUMERIC(7) PRIMARY KEY,
  descripcion VARCHAR(255) NOT NULL
);

-- Tabla: telefono
CREATE TABLE telefono (
  id_telefono NUMERIC(7) PRIMARY KEY,
  numero VARCHAR(20) NOT NULL
);

-- Tabla: correo
CREATE TABLE correo (
  id_correo NUMERIC(7) PRIMARY KEY,
  direccion_correo VARCHAR(50) NOT NULL
);

-- Tabla: cargo
CREATE TABLE cargo (
  id_cargo NUMERIC(7) PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  CONSTRAINT unique_nombre_cargo UNIQUE (nombre)
);

-- Tabla: area
CREATE TABLE area (
  id_area NUMERIC(7) PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  CONSTRAINT unique_nombre_area UNIQUE (nombre)
);

-- Tabla: proveedor
CREATE TABLE proveedor (
  ruc NUMERIC(11) PRIMARY KEY,
  denominacion_social VARCHAR(100) NOT NULL,
  id_direccion NUMERIC(7) NOT NULL,
  id_telefono NUMERIC(7) NOT NULL,
  id_correo NUMERIC(7) NOT NULL,
  FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion),
  FOREIGN KEY (id_telefono) REFERENCES telefono(id_telefono),
  FOREIGN KEY (id_correo) REFERENCES correo(id_correo)
);

-- Tabla: empleado
CREATE TABLE empleado (
  id_empleado NUMERIC(7) PRIMARY KEY,
  dni VARCHAR(8) NOT NULL,
  nombre VARCHAR(50) NOT NULL,
  primer_apellido VARCHAR(50) NOT NULL,
  segundo_apellido VARCHAR(50),
  id_area NUMERIC(7) NOT NULL,
  id_direccion NUMERIC(7) NOT NULL,
  id_telefono NUMERIC(7) NOT NULL,
  id_correo NUMERIC(7) NOT NULL,
  id_cargo NUMERIC(7) NOT NULL,
  FOREIGN KEY (id_area) REFERENCES area(id_area),
  FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion),
  FOREIGN KEY (id_telefono) REFERENCES telefono(id_telefono),
  FOREIGN KEY (id_correo) REFERENCES correo(id_correo),
  FOREIGN KEY (id_cargo) REFERENCES cargo(id_cargo)
);

-- Tabla: tipo_lote
CREATE TABLE tipo_lote (
  id_tipo_lote NUMERIC(7) PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL
);

-- Tabla: color
CREATE TABLE color (
  id_color NUMERIC(7) PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  CONSTRAINT unique_nombre_color UNIQUE (nombre)
);

-- Tabla: tipo_materia_prima
CREATE TABLE tipo_materia_prima (
  id_tipo_materia_prima NUMERIC(7) PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  CONSTRAINT unique_nombre_tipo_materia_prima UNIQUE (nombre)
);

-- Tabla: dimension_materia_prima
CREATE TABLE dimension_materia_prima (
  id_dim_materia_prima NUMERIC(7) PRIMARY KEY,
  id_tipo_materia_prima NUMERIC(7) NOT NULL,
  id_color NUMERIC(7) NOT NULL,
  FOREIGN KEY (id_tipo_materia_prima) REFERENCES tipo_materia_prima(id_tipo_materia_prima),
  FOREIGN KEY (id_color) REFERENCES color(id_color)
);

-- Tabla: lote
CREATE TABLE lote (
  id_lote NUMERIC(7) PRIMARY KEY,
  id_tipo_lote NUMERIC(7) NOT NULL,
  cantidad NUMERIC(7) NOT NULL,
  estado VARCHAR(20) NOT NULL,
  fecha_creacion DATE NOT NULL,
  id_dim_corte NUMERIC(7),
  id_dim_confeccion NUMERIC(7),
  id_dim_materia_prima NUMERIC(7),
  FOREIGN KEY (id_tipo_lote) REFERENCES tipo_lote(id_tipo_lote),
  FOREIGN KEY (id_dim_corte) REFERENCES dimension_materia_prima(id_dim_materia_prima),
  FOREIGN KEY (id_dim_confeccion) REFERENCES dimension_materia_prima(id_dim_materia_prima),
  FOREIGN KEY (id_dim_materia_prima) REFERENCES dimension_materia_prima(id_dim_materia_prima)
);

-- Tabla: materia_prima
CREATE TABLE materia_prima (
  id_materia_prima NUMERIC(7) PRIMARY KEY,
  id_lote NUMERIC(7) NOT NULL,
  id_dim_materia_prima NUMERIC(7) NOT NULL,
  ruc NUMERIC(11) NOT NULL,
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote),
  FOREIGN KEY (id_dim_materia_prima) REFERENCES dimension_materia_prima(id_dim_materia_prima),
  FOREIGN KEY (ruc) REFERENCES proveedor(ruc)
);

INSERT INTO direccion (id_direccion, descripcion) VALUES
(1, 'Calle Los Alamos 123, Lima'),
(2, 'Avenida Los Pinos 456, Lima'),
(3, 'Jirón Los Olivos 789, Lima'),
(4, 'Calle Los Cedros 321, Lima'),
(5, 'Avenida Los Eucaliptos 654, Lima'),
(6, 'Calle Los Robles 987, Lima'),
(7, 'Avenida Los Sauces 654, Lima'),
(8, 'Jirón Los Laureles 321, Lima'),
(9, 'Calle Los Naranjos 456, Lima'),
(10, 'Avenida Los Manzanos 123, Lima');

-- Insertar datos en la tabla telefono
INSERT INTO telefono (id_telefono, numero) VALUES
(1, '123456789'),
(2, '987654321'),
(3, '456123789'),
(4, '789321456'),
(5, '321789654'),
(6, '654987321'),
(7, '789654123'),
(8, '321456987'),
(9, '456789321'),
(10, '987321456');

-- Insertar datos en la tabla correo
INSERT INTO correo (id_correo, direccion_correo) VALUES
(1, 'juan.garcia@vircatex.com'),
(2, 'maria.lopez@vircatex.com'),
(3, 'pedro.martinez@vircatex.com'),
(4, 'ana.gomez@vircatex.com'),
(5, 'luis.torres@vircatex.com'),
(6, 'contacto@textilesdelsol.com'),
(7, 'ventas@tejidosandinos.com'),
(8, 'soporte@confeccionesluna.com'),
(9, 'info@telasestrella.com'),
(10, 'admin@fibrascreativas.com');

-- Insertar datos en la tabla cargo
INSERT INTO cargo (id_cargo, nombre) VALUES
(1, 'Jefe de almacén'),
(2, 'Almacenero');

-- Insertar datos en la tabla area
INSERT INTO area (id_area, nombre) VALUES
(1, 'Almacén'),
(2, 'Corte'),
(3, 'Confeccion'),
(4, 'Información'),
(5, 'Administración');

-- Insertar datos en la tabla proveedor
INSERT INTO proveedor (ruc, denominacion_social, id_direccion, id_telefono, id_correo) VALUES
(12345678901, 'Textiles del Sol', 6, 6, 6),
(98765432109, 'Tejidos Andinos', 7, 7, 7),
(56789012345, 'Confecciones Luna', 8, 8, 8),
(54321098765, 'Telas Estrella', 9, 9, 9),
(11111111111, 'Fibras Creativas', 10, 10, 10);

-- Insertar datos en la tabla empleado
INSERT INTO empleado (id_empleado, dni, nombre, primer_apellido, segundo_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo) VALUES
(1, '12345678', 'Juan', 'Pérez', 'García', 1, 1, 1, 1, 1),
(2, '87654321', 'María', 'Rodríguez', 'López', 2, 2, 2, 2, 2),
(3, '23456789', 'Pedro', 'González', 'Martínez', 3, 3, 3, 3, 2),
(4, '98765432', 'Ana', 'Fernández', 'Gómez', 4, 4, 4, 4, 2),
(5, '34567890', 'Luis', 'Ramírez', 'Torres', 5, 5, 5, 5, 2);

-- Insertar datos en la tabla tipo_lote
INSERT INTO tipo_lote (id_tipo_lote, nombre) VALUES
(1, 'Tipo 1'),
(2, 'Tipo 2'),
(3, 'Tipo 3'),
(4, 'Tipo 4'),
(5, 'Tipo 5');

-- Insertar datos en la tabla color
INSERT INTO color (id_color, nombre) VALUES
(1, 'Rojo'),
(2, 'Azul'),
(3, 'Verde'),
(4, 'Amarillo'),
(5, 'Negro');

-- Insertar datos en la tabla tipo_materia_prima
INSERT INTO tipo_materia_prima (id_tipo_materia_prima, nombre) VALUES
(1, 'Tipo A'),
(2, 'Tipo B'),
(3, 'Tipo C'),
(4, 'Tipo D'),
(5, 'Tipo E');

-- Insertar datos en la tabla dimension_materia_prima
INSERT INTO dimension_materia_prima (id_dim_materia_prima, id_tipo_materia_prima, id_color) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5);

-- Insertar datos en la tabla lote
INSERT INTO lote (id_lote, id_tipo_lote, cantidad, estado, fecha_creacion, id_dim_corte, id_dim_confeccion, id_dim_materia_prima) VALUES
(1, 1, 100, 'Disponible', CURRENT_DATE, 1, 2, 3),
(2, 2, 200, 'Disponible', CURRENT_DATE, 2, 3, 4),
(3, 3, 300, 'Disponible', CURRENT_DATE, 3, 4, 5),
(4, 4, 400, 'Disponible', CURRENT_DATE, 4, 5, 1),
(5, 5, 500, 'Disponible', CURRENT_DATE, 5, 1, 2);

-- Insertar datos en la tabla materia_prima
INSERT INTO materia_prima (id_materia_prima, id_lote, id_dim_materia_prima, ruc) VALUES
(1, 1, 1, 12345678901),
(2, 2, 2, 12345678901),
(3, 3, 3, 12345678901),
(4, 4, 4, 12345678901),
(5, 5, 5, 12345678901);