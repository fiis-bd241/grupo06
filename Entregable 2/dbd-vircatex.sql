--Nivel 1
CREATE TABLE Orden_pedido
(
  id_orden_pedido NUMERIC(6) NOT NULL,
  fecha_pedido DATE NOT NULL,
  estado VARCHAR(12) NOT NULL,
  PRIMARY KEY (id_orden_pedido)
);

CREATE TABLE Acabado
(
  id_acabado NUMERIC(1) NOT NULL,
  nombre VARCHAR(9) NOT NULL,
  PRIMARY KEY (id_acabado)
);

CREATE TABLE Costura
(
  id_costura NUMERIC(1) NOT NULL,
  descripcion VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_costura)
);

CREATE TABLE Area
(
  nombre VARCHAR(19) NOT NULL,
  id_area CHAR(1) NOT NULL,
  PRIMARY KEY (id_area),
  UNIQUE (nombre)
);

CREATE TABLE Color
(
  id_color NUMERIC(3) NOT NULL,
  tono_color VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_color)
);

CREATE TABLE Maquina_corte
(
  id_maquina NUMERIC(3) NOT NULL,
  estado VARCHAR(13) NOT NULL,
  PRIMARY KEY (id_maquina)
);

CREATE TABLE Proveedor
(
  ruc NUMERIC(11) NOT NULL,
  denominacion_social VARCHAR(30) NOT NULL,
  correo VARCHAR(30) NOT NULL,
  dirección VARCHAR(50) NOT NULL,
  PRIMARY KEY (ruc)
);

CREATE TABLE Tipo_materia_prima
(
  Id_materia NUMERIC(5) NOT NULL,
  descripcion VARCHAR(20) NOT NULL,
  PRIMARY KEY (Id_materia)
);

CREATE TABLE Inspeccion_de_calidad
(
  id_inspeccion NUMERIC(7) NOT NULL,
  fecha_inspeccion DATE NOT NULL,
  estado VARCHAR(12) NOT NULL,
  resultado NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_inspeccion)
);

CREATE TABLE Error_prototipo
(
  descripcion_errores VARCHAR(30) NOT NULL,
  id_error INT NOT NULL,
  PRIMARY KEY (id_error)
);

CREATE TABLE AQL_Rango
(
  limite_aql FLOAT NOT NULL,
  aceptación_maxima INT NOT NULL,
  rechazo_minimo INT NOT NULL,
  PRIMARY KEY (limite_aql)
);

--Nivel 2
CREATE TABLE AQL_Codigo
(
  letra_codigo_aql CHAR(1) NOT NULL,
  nivel_inspeccion CHAR(2) NOT NULL,
  tamaño_lote_mínimo INT NOT NULL,
  tamaño_lote_máximo INT NOT NULL,
  tamaño_muestra INT NOT NULL,
  limite_aql FLOAT NOT NULL,
  PRIMARY KEY (letra_codigo_aql, nivel_inspeccion, limite_aql),
  FOREIGN KEY (limite_aql) REFERENCES AQL_Rango(limite_aql)
);

CREATE TABLE Materia_prima
(
  id_color NUMERIC(3) NOT NULL,
  Id_materia NUMERIC(5) NOT NULL,
  PRIMARY KEY (id_color, Id_materia),
  FOREIGN KEY (id_color) REFERENCES Color(id_color),
  FOREIGN KEY (Id_materia) REFERENCES Tipo_materia_prima(Id_materia)
);

CREATE TABLE Corte
(
  id_corte NUMERIC(8) NOT NULL,
  talla VARCHAR(4) NOT NULL,
  medida FLOAT NOT NULL,
  fecha_creacion DATE NOT NULL,
  id_maquina NUMERIC(3) NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  PRIMARY KEY (id_corte),
  FOREIGN KEY (id_maquina) REFERENCES Maquina_corte(id_maquina),
  FOREIGN KEY (id_color) REFERENCES Color(id_color)
);

CREATE TABLE Lote
(
  cantidad INT NOT NULL,
  id_lote NUMERIC(7) NOT NULL,
  estado VARCHAR(12) NOT NULL,
  fecha_ingreso DATE NOT NULL,
  fecha_salida DATE NOT NULL,
  area_recibe CHAR(1) NOT NULL,
  area_envia CHAR(1) NOT NULL,
  PRIMARY KEY (id_lote),
  FOREIGN KEY (area_recibe) REFERENCES Area(id_area),
  FOREIGN KEY (area_envia) REFERENCES Area(id_area)
);

CREATE TABLE Empleado
(
  dni CHAR(8) NOT NULL,
  cargo VARCHAR(10) NOT NULL,
  nombre VARCHAR(30) NOT NULL,
  segundo_apellido VARCHAR(15) NOT NULL,
  primer_apellido VARCHAR(15) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  dirección VARCHAR(50) NOT NULL,
  correo VARCHAR(30) NOT NULL,
  id_empleado NUMERIC(5) NOT NULL,
  id_area CHAR(1) NOT NULL,
  PRIMARY KEY (id_empleado),
  FOREIGN KEY (id_area) REFERENCES Area(id_area),
  UNIQUE (dni)
);

CREATE TABLE Pedido
(
  id_pedido NUMERIC(6) NOT NULL,
  tipo_prenda VARCHAR(15) NOT NULL,
  estilo_prenda VARCHAR(11) NOT NULL,
  talla VARCHAR(4) NOT NULL,
  id_orden_pedido NUMERIC(6) NOT NULL,
  PRIMARY KEY (id_pedido),
  FOREIGN KEY (id_orden_pedido) REFERENCES Orden_pedido(id_orden_pedido)
);

CREATE TABLE Orden_trabajo
(
  id_orden_trabajo NUMERIC(7) NOT NULL,
  prioridad NUMERIC(2),
  estado VARCHAR(12) NOT NULL,
  fecha_creacion DATE NOT NULL,
  fecha_fin DATE,
  id_orden_pedido NUMERIC(6) NOT NULL,
  PRIMARY KEY (id_orden_trabajo),
  FOREIGN KEY (id_orden_pedido) REFERENCES Orden_pedido(id_orden_pedido)
);

--Nivel 3
CREATE TABLE Descripcion_acabados
(
  id_desc_acab NUMERIC(2) NOT NULL,
  cantidad INT NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_desc_acab, id_orden_trabajo),
  FOREIGN KEY (id_orden_trabajo) REFERENCES Orden_trabajo(id_orden_trabajo)
);

CREATE TABLE Prenda
(
  id_prenda NUMERIC(8) NOT NULL,
  fecha_creacion DATE NOT NULL,
  tipo_prenda VARCHAR(15) NOT NULL,
  estilo_prenda VARCHAR(11) NOT NULL,
  talla VARCHAR(4) NOT NULL,
  id_empleado NUMERIC(5) NOT NULL,
  PRIMARY KEY (id_prenda),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

CREATE TABLE Acabado_pedido
(
  id_pedido NUMERIC(6) NOT NULL,
  id_acabado NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_pedido, id_acabado),
  FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
  FOREIGN KEY (id_acabado) REFERENCES Acabado(id_acabado)
);

CREATE TABLE Color_pedido
(
  id_color NUMERIC(3) NOT NULL,
  id_pedido NUMERIC(6) NOT NULL,
  PRIMARY KEY (id_color, id_pedido),
  FOREIGN KEY (id_color) REFERENCES Color(id_color),
  FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
);

CREATE TABLE Descripcion_confeccion
(
  id_desc_conf NUMERIC(2) NOT NULL,
  estilo_prenda VARCHAR(11) NOT NULL,
  tipo_prenda VARCHAR(15) NOT NULL,
  cantidad INT NOT NULL,
  talla VARCHAR(4) NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_desc_conf, id_orden_trabajo),
  FOREIGN KEY (id_orden_trabajo) REFERENCES Orden_trabajo(id_orden_trabajo)
);

CREATE TABLE Confeccion
(
  id_confeccion NUMERIC(8) NOT NULL,
  fecha_creacion DATE NOT NULL,
  tipo_prenda VARCHAR(15) NOT NULL,
  estilo_prenda VARCHAR(11) NOT NULL,
  talla VARCHAR(4) NOT NULL,
  id_empleado NUMERIC(5) NOT NULL,
  PRIMARY KEY (id_confeccion),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

CREATE TABLE Lote_acabado
(
  estilo_prenda VARCHAR(11) NOT NULL,
  tipo_prenda VARCHAR(15) NOT NULL,
  talla VARCHAR(4) NOT NULL,
  id_lote NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_lote),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote)
);

CREATE TABLE Descripcion_corte
(
  id_desc_corte NUMERIC(2) NOT NULL,
  medida FLOAT NOT NULL,
  talla VARCHAR(4) NOT NULL,
  cantidad INT NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_desc_corte, id_orden_trabajo),
  FOREIGN KEY (id_color) REFERENCES Color(id_color),
  FOREIGN KEY (id_orden_trabajo) REFERENCES Orden_trabajo(id_orden_trabajo)
);

CREATE TABLE Telefono
(
  telefono CHAR(9) NOT NULL,
  ruc NUMERIC(11),
  id_empleado NUMERIC(5),
  PRIMARY KEY (telefono),
  FOREIGN KEY (ruc) REFERENCES Proveedor(ruc),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

CREATE TABLE Reserva
(
  ubicacion VARCHAR(7) NOT NULL,
  estado VARCHAR(13) NOT NULL,
  largo FLOAT NOT NULL,
  alto FLOAT NOT NULL,
  ancho FLOAT NOT NULL,
  id_area CHAR(1) NOT NULL,
  id_lote NUMERIC(7),
  PRIMARY KEY (ubicacion, id_area),
  FOREIGN KEY (id_area) REFERENCES Area(id_area),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote)
);

CREATE TABLE Lote_confeccion
(
  tipo_prenda VARCHAR(15) NOT NULL,
  estilo_prenda VARCHAR(11) NOT NULL,
  talla VARCHAR(4) NOT NULL,
  id_lote NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_lote),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote)
);

CREATE TABLE Lote_corte
(
  merma FLOAT,
  talla VARCHAR(4) NOT NULL,
  medida FLOAT NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  id_lote NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_lote),
  FOREIGN KEY (id_color) REFERENCES Color(id_color),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote)
);

CREATE TABLE Descripcion_materia_prima
(
  id_desc_mat_prim NUMERIC(2) NOT NULL,
  cantidad INT NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  Id_materia NUMERIC(5) NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_desc_mat_prim, id_orden_trabajo),
  FOREIGN KEY (id_color, Id_materia) REFERENCES Materia_prima(id_color, Id_materia),
  FOREIGN KEY (id_orden_trabajo) REFERENCES Orden_trabajo(id_orden_trabajo)
);

CREATE TABLE Materia_pedido
(
  id_pedido NUMERIC(6) NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  Id_materia NUMERIC(5) NOT NULL,
  PRIMARY KEY (id_pedido, id_color, Id_materia),
  FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
  FOREIGN KEY (id_color, Id_materia) REFERENCES Materia_prima(id_color, Id_materia)
);

CREATE TABLE Inspeccion_muestra
(
  cantidad_errores INT NOT NULL,
  tamaño_lote INT NOT NULL,
  cantidad_muestra INT NOT NULL,
  id_inspeccion NUMERIC(7) NOT NULL,
  id_lote NUMERIC(7) NOT NULL,
  letra_codigo_aql CHAR(1) NOT NULL,
  nivel_inspeccion CHAR(2) NOT NULL,
  limite_aql FLOAT NOT NULL,
  PRIMARY KEY (id_inspeccion),
  FOREIGN KEY (id_inspeccion) REFERENCES Inspeccion_de_calidad(id_inspeccion),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote),
  FOREIGN KEY (letra_codigo_aql, nivel_inspeccion, limite_aql) REFERENCES AQL_Codigo(letra_codigo_aql, nivel_inspeccion, limite_aql)
);

--Nivel 4
CREATE TABLE Orden_compra
(
  id_orden_compra NUMERIC(7) NOT NULL,
  fecha_fin DATE NOT NULL,
  fecha_inicio DATE NOT NULL,
  estado VARCHAR(12) NOT NULL,
  cantidad INT NOT NULL,
  ruc NUMERIC(11) NOT NULL,
  id_desc_mat_prim NUMERIC(2) NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_orden_compra),
  FOREIGN KEY (ruc) REFERENCES Proveedor(ruc),
  FOREIGN KEY (id_desc_mat_prim, id_orden_trabajo) REFERENCES Descripcion_materia_prima(id_desc_mat_prim, id_orden_trabajo)
);

CREATE TABLE Registro_cortes_lote
(
  id_corte NUMERIC(8) NOT NULL,
  id_lote NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_corte, id_lote),
  FOREIGN KEY (id_corte) REFERENCES Corte(id_corte),
  FOREIGN KEY (id_lote) REFERENCES Lote_corte(id_lote)
);

CREATE TABLE Orden_confección
(
  id_orden_confeccion NUMERIC(7) NOT NULL,
  fecha_inicio DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  estado VARCHAR(12) NOT NULL,
  id_lote_corte NUMERIC(7) NOT NULL,
  id_desc_conf NUMERIC(2) NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_orden_confeccion),
  FOREIGN KEY (id_lote_corte) REFERENCES Lote_corte(id_lote),
  FOREIGN KEY (id_desc_conf, id_orden_trabajo) REFERENCES Descripcion_confeccion(id_desc_conf, id_orden_trabajo)
);

CREATE TABLE Caja_confeccion
(
  estilo_prenda VARCHAR(11) NOT NULL,
  tipo_prenda VARCHAR(15) NOT NULL,
  id_caja NUMERIC(8) NOT NULL,
  cantidad INT NOT NULL,
  talla VARCHAR(4) NOT NULL,
  id_lote NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_caja),
  FOREIGN KEY (id_lote) REFERENCES Lote_confeccion(id_lote)
);

CREATE TABLE Registro_conteo
(
  cantidad_lote INT NOT NULL,
  id_empleado NUMERIC(5) NOT NULL,
  id_lote NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_empleado, id_lote),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado),
  FOREIGN KEY (id_lote) REFERENCES Lote_confeccion(id_lote)
);

CREATE TABLE Color_lote_confeccion
(
  id_lote NUMERIC(7) NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  PRIMARY KEY (id_lote, id_color),
  FOREIGN KEY (id_lote) REFERENCES Lote_confeccion(id_lote),
  FOREIGN KEY (id_color) REFERENCES Color(id_color)
);

CREATE TABLE Color_lote_acabado
(
  id_lote NUMERIC(7) NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  PRIMARY KEY (id_lote, id_color),
  FOREIGN KEY (id_lote) REFERENCES Lote_acabado(id_lote),
  FOREIGN KEY (id_color) REFERENCES Color(id_color)
);

CREATE TABLE Registro_confeccion_lote
(
  id_confeccion NUMERIC(8) NOT NULL,
  id_lote NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_confeccion, id_lote),
  FOREIGN KEY (id_confeccion) REFERENCES Confeccion(id_confeccion),
  FOREIGN KEY (id_lote) REFERENCES Lote_confeccion(id_lote)
);

CREATE TABLE Registro_prenda_lote
(
  id_prenda NUMERIC(8) NOT NULL,
  id_lote NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_prenda, id_lote),
  FOREIGN KEY (id_prenda) REFERENCES Prenda(id_prenda),
  FOREIGN KEY (id_lote) REFERENCES Lote_acabado(id_lote)
);

CREATE TABLE Acabado_lote
(
  id_lote NUMERIC(7) NOT NULL,
  id_acabado NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_lote, id_acabado),
  FOREIGN KEY (id_lote) REFERENCES Lote_acabado(id_lote),
  FOREIGN KEY (id_acabado) REFERENCES Acabado(id_acabado)
);

CREATE TABLE Color_desc_confeccion
(
  id_color NUMERIC(3) NOT NULL,
  id_desc_conf NUMERIC(2) NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_color, id_desc_conf, id_orden_trabajo),
  FOREIGN KEY (id_color) REFERENCES color(id_color),
  FOREIGN KEY (id_desc_conf, id_orden_trabajo) REFERENCES Descripcion_confeccion(id_desc_conf, id_orden_trabajo)
);

CREATE TABLE Color_confeccion
(
  id_color NUMERIC(3) NOT NULL,
  id_confeccion NUMERIC(8) NOT NULL,
  PRIMARY KEY (id_color, id_confeccion),
  FOREIGN KEY (id_color) REFERENCES Color(id_color),
  FOREIGN KEY (id_confeccion) REFERENCES Confeccion(id_confeccion)
);

CREATE TABLE Color_prenda
(
  id_prenda NUMERIC(8) NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  PRIMARY KEY (id_prenda, id_color),
  FOREIGN KEY (id_prenda) REFERENCES Prenda(id_prenda),
  FOREIGN KEY (id_color) REFERENCES Color(id_color)
);

CREATE TABLE Confeccion_costuras
(
  id_costura NUMERIC(5) NOT NULL,
  id_desc_conf NUMERIC(2) NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_costura, id_desc_conf, id_orden_trabajo),
  FOREIGN KEY (id_costura) REFERENCES Costura(id_costura),
  FOREIGN KEY (id_desc_conf, id_orden_trabajo) REFERENCES Descripcion_confeccion(id_desc_conf, id_orden_trabajo)
);

CREATE TABLE Acabado_prenda
(
  id_prenda NUMERIC(8) NOT NULL,
  id_acabado NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_prenda, id_acabado),
  FOREIGN KEY (id_prenda) REFERENCES Prenda(id_prenda),
  FOREIGN KEY (id_acabado) REFERENCES Acabado(id_acabado)
);

CREATE TABLE Acabado_desc_acab
(
  id_acabado NUMERIC(1) NOT NULL,
  id_desc_acab NUMERIC(2) NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_acabado, id_desc_acab, id_orden_trabajo),
  FOREIGN KEY (id_acabado) REFERENCES Acabado(id_acabado),
  FOREIGN KEY (id_desc_acab, id_orden_trabajo) REFERENCES Descripcion_acabados(id_desc_acab, id_orden_trabajo)
);

--Nivel 5
CREATE TABLE Orden_acabado
(
  id_orden_acabado NUMERIC(7) NOT NULL,
  fecha_inicio DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  id_caja NUMERIC(8) NOT NULL,
  id_desc_acab NUMERIC(2) NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_orden_acabado),
  FOREIGN KEY (id_caja) REFERENCES Caja_confeccion(id_caja),
  FOREIGN KEY (id_desc_acab, id_orden_trabajo) REFERENCES Descripcion_acabados(id_desc_acab, id_orden_trabajo)
);

CREATE TABLE Acabado_caja_confeccion
(
  id_acabado NUMERIC(1) NOT NULL,
  id_caja NUMERIC(8) NOT NULL,
  PRIMARY KEY (id_acabado, id_caja),
  FOREIGN KEY (id_acabado) REFERENCES Acabado(id_acabado),
  FOREIGN KEY (id_caja) REFERENCES Caja_confeccion(id_caja)
);

CREATE TABLE Registro_caja_confeccion
(
  cantidad_caja INT NOT NULL,
  id_caja NUMERIC(8) NOT NULL,
  id_empleado NUMERIC(5) NOT NULL,
  PRIMARY KEY (id_caja, id_empleado),
  FOREIGN KEY (id_caja) REFERENCES Caja_confeccion(id_caja),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

CREATE TABLE color_caja_confeccion
(
  id_caja NUMERIC(8) NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  PRIMARY KEY (id_caja, id_color),
  FOREIGN KEY (id_caja) REFERENCES Caja_confeccion(id_caja),
  FOREIGN KEY (id_color) REFERENCES color(id_color)
);

CREATE TABLE Asignacion_costurero
(
  cantidad INT NOT NULL,
  id_empleado NUMERIC(5) NOT NULL,
  id_orden_confeccion NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_empleado, id_orden_confeccion),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado),
  FOREIGN KEY (id_orden_confeccion) REFERENCES Orden_confección(id_orden_confeccion)
);

CREATE TABLE Prototipo
(
  id_prototipo NUMERIC(7) NOT NULL,
  estado VARCHAR(12) NOT NULL,
  fecha_creacion DATE NOT NULL,
  id_orden_confeccion NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_prototipo),
  FOREIGN KEY (id_orden_confeccion) REFERENCES Orden_confección(id_orden_confeccion)
);

CREATE TABLE Lote_materia_prima
(
  id_lote NUMERIC(7) NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  Id_materia NUMERIC(5) NOT NULL,
  id_orden_compra NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_lote),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote),
  FOREIGN KEY (id_color, Id_materia) REFERENCES Materia_prima(id_color, Id_materia),
  FOREIGN KEY (id_orden_compra) REFERENCES Orden_compra(id_orden_compra)
);

--Nivel 6
CREATE TABLE Inspeccion_prototipo
(
  cantidad_errores INT NOT NULL,
  id_inspeccion NUMERIC(7) NOT NULL,
  id_prototipo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_inspeccion),
  FOREIGN KEY (id_inspeccion) REFERENCES Inspeccion_de_calidad(id_inspeccion),
  FOREIGN KEY (id_prototipo) REFERENCES Prototipo(id_prototipo)
);

CREATE TABLE Orden_corte
(
  id_orden_corte NUMERIC(7) NOT NULL,
  fecha_inicio DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  estado VARCHAR(12) NOT NULL,
  id_lote_mat_prim NUMERIC(7) NOT NULL,
  id_desc_corte NUMERIC(2) NOT NULL,
  id_orden_trabajo NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_orden_corte),
  FOREIGN KEY (id_lote_mat_prim) REFERENCES Lote_materia_prima(id_lote),
  FOREIGN KEY (id_desc_corte, id_orden_trabajo) REFERENCES Descripcion_corte(id_desc_corte, id_orden_trabajo)
);

CREATE TABLE Asignacion_operario_acabado
(
  cantidad INT NOT NULL,
  id_empleado NUMERIC(5) NOT NULL,
  id_orden_acabado NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_empleado, id_orden_acabado),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado),
  FOREIGN KEY (id_orden_acabado) REFERENCES Orden_acabado(id_orden_acabado)
);

--Nivel 7
CREATE TABLE Registro_programa_corte
(
  cantidad INT NOT NULL,
  id_orden_corte NUMERIC(7) NOT NULL,
  id_maquina NUMERIC(3) NOT NULL,
  PRIMARY KEY (id_orden_corte, id_maquina),
  FOREIGN KEY (id_orden_corte) REFERENCES Orden_corte(id_orden_corte),
  FOREIGN KEY (id_maquina) REFERENCES Maquina_corte(id_maquina)
);

CREATE TABLE Reporte_errores
(
  id_inspeccion NUMERIC(7) NOT NULL,
  id_error INT NOT NULL,
  PRIMARY KEY (id_inspeccion, id_error),
  FOREIGN KEY (id_inspeccion) REFERENCES Inspeccion_prototipo(id_inspeccion),
  FOREIGN KEY (id_error) REFERENCES Error_prototipo(id_error)
);