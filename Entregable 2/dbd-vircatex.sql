--Nivel 1
CREATE TABLE Direccion
(
  id_direccion NUMERIC(6) NOT NULL,
  descripcion VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_direccion)
);

CREATE TABLE Correo
(
  id_correo NUMERIC(6) NOT NULL,
  direccion_correo VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_correo)
);

CREATE TABLE Telefono
(
  id_telefono NUMERIC(6) NOT NULL,
  numero VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_telefono),
  UNIQUE (numero)
);

CREATE TABLE Cargo
(
  id_cargo NUMERIC(1) NOT NULL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_cargo),
  UNIQUE (nombre)
);

CREATE TABLE Maquina
(
  id_maquina NUMERIC(3) NOT NULL,
  capacidad_total INT NOT NULL,
  estado VARCHAR(20) NOT NULL,
  capacidad_usada INT NOT NULL,
  capacidad_disponible INT NOT NULL,
  PRIMARY KEY (id_maquina)
);

CREATE TABLE Tipo_corte
(
  id_tipo_corte VARCHAR(3) NOT NULL,
  descripcion VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_tipo_corte)
);

CREATE TABLE Tipo_lote
(
  id_tipo_lote NUMERIC(1) NOT NULL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_tipo_lote),
  UNIQUE (nombre)
);

CREATE TABLE Talla
(
  id_talla NUMERIC(1) NOT NULL,
  nombre VARCHAR(4) NOT NULL,
  PRIMARY KEY (id_talla),
  UNIQUE (nombre)
);

CREATE TABLE Genero
(
  id_genero NUMERIC(1) NOT NULL,
  nombre VARCHAR(10) NOT NULL,
  PRIMARY KEY (id_genero),
  UNIQUE (nombre)
);

CREATE TABLE Nombre_parte_prenda
(
  id_nombre_parte_prenda NUMERIC(2) NOT NULL,
  nombre VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_nombre_parte_prenda),
  UNIQUE (nombre)
);

CREATE TABLE Tipo_materia_prima
(
  id_tipo_materia_prima NUMERIC(5) NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_tipo_materia_prima),
  UNIQUE (nombre)
);

CREATE TABLE Color
(
  id_color NUMERIC(3) NOT NULL,
  nombre_color VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_color),
  UNIQUE (nombre_color)
);

CREATE TABLE Guia_confeccion_talla_genero
(
  id_guia_confeccion NUMERIC(10) NOT NULL,
  medida_pecho FLOAT,
  medida_cintura FLOAT,
  medida_cadera FLOAT,
  medida_hombro FLOAT,
  medida_longitud FLOAT,
  medida_manga FLOAT,
  medida_muslo FLOAT,
  PRIMARY KEY (id_guia_confeccion)
);

CREATE TABLE Tipo_prenda
(
  id_tipo_prenda NUMERIC(2) NOT NULL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_tipo_prenda),
  UNIQUE (nombre)
);

CREATE TABLE Estilo_prenda
(
  id_estilo_prenda NUMERIC(2) NOT NULL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_estilo_prenda),
  UNIQUE (nombre)
);

CREATE TABLE Acabado
(
  id_acabado NUMERIC(1) NOT NULL,
  nombre VARCHAR(9) NOT NULL,
  PRIMARY KEY (id_acabado),
  UNIQUE (nombre)
);

CREATE TABLE Area
(
  id_area NUMERIC(1) NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_area),
  UNIQUE (nombre)
);

CREATE TABLE Tipo_division
(
  id_tipo_division NUMERIC(1) NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_tipo_division),
  UNIQUE (nombre)
);

CREATE TABLE Orden_pedido
(
  fecha_creacion DATE NOT NULL,
  estado VARCHAR(15) NOT NULL,
  fecha_fin DATE NOT NULL,
  id_orden_pedido NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_orden_pedido)
);

CREATE TABLE Inspeccion_descripcion
(
  id_descripcion NUMERIC(10) NOT NULL,
  descripcion VARCHAR(200) NOT NULL,
  PRIMARY KEY (id_descripcion)
);

CREATE TABLE AQL_nivel
(
  id_aql_nivel NUMERIC(1) NOT NULL,
  nombre CHAR(2) NOT NULL,
  PRIMARY KEY (id_aql_nivel),
  UNIQUE (nombre)
);

CREATE TABLE AQL_lote_rango
(
  id_aql_lote_rango NUMERIC(2) NOT NULL,
  min_lote INT NOT NULL,
  max_lote INT NOT NULL,
  PRIMARY KEY (id_aql_lote_rango)
);

CREATE TABLE AQL_codigo
(
  id_aql_codigo CHAR(1) NOT NULL,
  tamano_muestra INT NOT NULL,
  PRIMARY KEY (id_aql_codigo),
  UNIQUE (tamano_muestra)
);

CREATE TABLE AQL_significancia
(
  id_aql_significancia NUMERIC(1) NOT NULL,
  nivel_significancia FLOAT NOT NULL,
  PRIMARY KEY (id_aql_significancia),
  UNIQUE (nivel_significancia)
);

CREATE TABLE Tipo_resultado
(
  id_resultado NUMERIC(1) NOT NULL,
  descripcion VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_resultado)
);

CREATE TABLE Gantt
(
  id_gantt NUMERIC(10) NOT NULL,
  fecha_creacion DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  estado VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_gantt)
);

--Nivel 2
CREATE TABLE Proveedor
(
  ruc NUMERIC(11) NOT NULL,
  denominacion_social VARCHAR(100) NOT NULL,
  id_direccion NUMERIC(6) NOT NULL,
  id_telefono NUMERIC(6) NOT NULL,
  id_correo NUMERIC(6) NOT NULL,
  PRIMARY KEY (ruc),
  FOREIGN KEY (id_direccion) REFERENCES Direccion(id_direccion),
  FOREIGN KEY (id_telefono) REFERENCES Telefono(id_telefono),
  FOREIGN KEY (id_correo) REFERENCES Correo(id_correo)
);

CREATE TABLE Empleado
(
  id_empleado NUMERIC(5) NOT NULL,
  dni CHAR(8) NOT NULL,
  nombre VARCHAR(30) NOT NULL,
  segundo_apellido VARCHAR(15) NOT NULL,
  primer_apellido VARCHAR(15) NOT NULL,
  id_area NUMERIC(1) NOT NULL,
  id_direccion NUMERIC(6) NOT NULL,
  id_telefono NUMERIC(6) NOT NULL,
  id_correo NUMERIC(6) NOT NULL,
  id_cargo NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_empleado),
  FOREIGN KEY (id_area) REFERENCES Area(id_area),
  FOREIGN KEY (id_direccion) REFERENCES Direccion(id_direccion),
  FOREIGN KEY (id_telefono) REFERENCES Telefono(id_telefono),
  FOREIGN KEY (id_correo) REFERENCES Correo(id_correo),
  FOREIGN KEY (id_cargo) REFERENCES Cargo(id_cargo),
  UNIQUE (dni)
);

CREATE TABLE Corte_medida
(
  id_corte_medida NUMERIC(10) NOT NULL,
  medida FLOAT NOT NULL,
  id_tipo_corte VARCHAR(3) NOT NULL,
  PRIMARY KEY (id_corte_medida),
  FOREIGN KEY (id_tipo_corte) REFERENCES Tipo_corte(id_tipo_corte)
);

CREATE TABLE Guia_corte_talla_genero
(
  id_guia_corte NUMERIC(10) NOT NULL,
  id_genero NUMERIC(1) NOT NULL,
  id_talla NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_guia_corte),
  FOREIGN KEY (id_genero) REFERENCES Genero(id_genero),
  FOREIGN KEY (id_talla) REFERENCES Talla(id_talla)
);

CREATE TABLE Dimension_materia_prima
(
  id_dim_materia_prima NUMERIC(10) NOT NULL,
  id_color NUMERIC(3) NOT NULL,
  id_tipo_materia_prima NUMERIC(5) NOT NULL,
  PRIMARY KEY (id_dim_materia_prima),
  FOREIGN KEY (id_color) REFERENCES Color(id_color),
  FOREIGN KEY (id_tipo_materia_prima) REFERENCES Tipo_materia_prima(id_tipo_materia_prima)
);

CREATE TABLE Dimension_confeccion
(
  id_dim_confeccion NUMERIC(10) NOT NULL,
  id_tipo_prenda NUMERIC(2) NOT NULL,
  id_estilo_prenda NUMERIC(2) NOT NULL,
  id_guia_confeccion NUMERIC(10) NOT NULL,
  id_talla NUMERIC(1) NOT NULL,
  id_genero NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_dim_confeccion),
  FOREIGN KEY (id_tipo_prenda) REFERENCES Tipo_prenda(id_tipo_prenda),
  FOREIGN KEY (id_estilo_prenda) REFERENCES Estilo_prenda(id_estilo_prenda),
  FOREIGN KEY (id_guia_confeccion) REFERENCES Guia_confeccion_talla_genero(id_guia_confeccion),
  FOREIGN KEY (id_talla) REFERENCES Talla(id_talla),
  FOREIGN KEY (id_genero) REFERENCES Genero(id_genero)
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

CREATE TABLE Orden_trabajo
(
  id_orden_trabajo NUMERIC(10) NOT NULL,
  fecha_creacion DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  estado VARCHAR(15) NOT NULL,
  prioridad INT NOT NULL,
  PRIMARY KEY (id_orden_trabajo)
);

CREATE TABLE AQL_muestra
(
  id_aql_codigo CHAR(1) NOT NULL,
  id_aql_lote_rango NUMERIC(2) NOT NULL,
  id_aql_nivel NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_aql_lote_rango, id_aql_nivel),
  FOREIGN KEY (id_aql_codigo) REFERENCES AQL_codigo(id_aql_codigo),
  FOREIGN KEY (id_aql_lote_rango) REFERENCES AQL_lote_rango(id_aql_lote_rango),
  FOREIGN KEY (id_aql_nivel) REFERENCES AQL_nivel(id_aql_nivel)
);

CREATE TABLE AQL_resultado_rango
(
  max_aceptacion INT NOT NULL,
  min_rechazo INT NOT NULL,
  id_aql_codigo CHAR(1) NOT NULL,
  id_aql_significancia NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_aql_codigo, id_aql_significancia),
  FOREIGN KEY (id_aql_codigo) REFERENCES AQL_codigo(id_aql_codigo),
  FOREIGN KEY (id_aql_significancia) REFERENCES AQL_significancia(id_aql_significancia)
);

--Nivel 3
CREATE TABLE Guia_corte_detalle
(
  id_corte_medida NUMERIC(10) NOT NULL,
  id_guia_corte NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_corte_medida, id_guia_corte),
  FOREIGN KEY (id_corte_medida) REFERENCES Corte_medida(id_corte_medida),
  FOREIGN KEY (id_guia_corte) REFERENCES Guia_corte_talla_genero(id_guia_corte)
);

CREATE TABLE Dimension_parte_prenda
(
  id_dim_parte_prenda NUMERIC(10) NOT NULL,
  id_guia_corte NUMERIC(10) NOT NULL,
  id_nombre_parte_prenda NUMERIC(2) NOT NULL,
  PRIMARY KEY (id_dim_parte_prenda),
  FOREIGN KEY (id_guia_corte) REFERENCES Guia_corte_talla_genero(id_guia_corte),
  FOREIGN KEY (id_nombre_parte_prenda) REFERENCES Nombre_parte_prenda(id_nombre_parte_prenda)
);

CREATE TABLE Dimension_prenda
(
  id_dim_prenda NUMERIC(10) NOT NULL,
  id_dim_confeccion NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_dim_prenda),
  FOREIGN KEY (id_dim_confeccion) REFERENCES Dimension_confeccion(id_dim_confeccion)
);

CREATE TABLE Orden_trabajo_x_pedido
(
  id_orden_pedido NUMERIC(10) NOT NULL,
  id_orden_trabajo NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_orden_pedido, id_orden_trabajo),
  FOREIGN KEY (id_orden_pedido) REFERENCES Orden_pedido(id_orden_pedido),
  FOREIGN KEY (id_orden_trabajo) REFERENCES Orden_trabajo(id_orden_trabajo)
);

--Nivel 4
CREATE TABLE Dimension_corte
(
  id_dim_corte NUMERIC(10) NOT NULL,
  id_dim_materia_prima NUMERIC(10) NOT NULL,
  id_dim_parte_prenda NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_dim_corte),
  FOREIGN KEY (id_dim_materia_prima) REFERENCES Dimension_materia_prima(id_dim_materia_prima),
  FOREIGN KEY (id_dim_parte_prenda) REFERENCES Dimension_parte_prenda(id_dim_parte_prenda)
);

CREATE TABLE Dim_prenda_detalle
(
  id_acabado NUMERIC(1) NOT NULL,
  id_dim_prenda NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_acabado, id_dim_prenda),
  FOREIGN KEY (id_acabado) REFERENCES Acabado(id_acabado),
  FOREIGN KEY (id_dim_prenda) REFERENCES Dimension_prenda(id_dim_prenda)
);

CREATE TABLE Caja
(
  id_caja NUMERIC(10) NOT NULL,
  cantidad INT NOT NULL,
  fecha_creacion DATE NOT NULL,
  id_dim_prenda NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_caja),
  FOREIGN KEY (id_dim_prenda) REFERENCES Dimension_prenda(id_dim_prenda)
);

CREATE TABLE Descripcion
(
  id_descripcion NUMERIC(10) NOT NULL,
  id_dim_prenda NUMERIC(10) NOT NULL,
  id_orden_trabajo NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_descripcion),
  FOREIGN KEY (id_dim_prenda) REFERENCES Dimension_prenda(id_dim_prenda),
  FOREIGN KEY (id_orden_trabajo) REFERENCES Orden_trabajo(id_orden_trabajo)
);

CREATE TABLE Pedido_detalle
(
  id_dim_prenda NUMERIC(10) NOT NULL,
  id_orden_pedido NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_dim_prenda, id_orden_pedido),
  FOREIGN KEY (id_dim_prenda) REFERENCES Dimension_prenda(id_dim_prenda),
  FOREIGN KEY (id_orden_pedido) REFERENCES Orden_pedido(id_orden_pedido)
);

--Nivel 5

CREATE TABLE Lote
(
  cantidad INT NOT NULL,
  estado VARCHAR(15) NOT NULL,
  id_lote NUMERIC(10) NOT NULL,
  fecha_creacion DATE NOT NULL,
  id_tipo_lote NUMERIC(1) NOT NULL,
  id_dim_corte NUMERIC(10),
  id_dim_confeccion NUMERIC(10),
  id_dim_materia_prima NUMERIC(10),
  PRIMARY KEY (id_lote),
  FOREIGN KEY (id_tipo_lote) REFERENCES Tipo_lote(id_tipo_lote),
  FOREIGN KEY (id_dim_corte) REFERENCES Dimension_corte(id_dim_corte),
  FOREIGN KEY (id_dim_confeccion) REFERENCES Dimension_confeccion(id_dim_confeccion),
  FOREIGN KEY (id_dim_materia_prima) REFERENCES Dimension_materia_prima(id_dim_materia_prima)
);

CREATE TABLE Dim_confeccion_detalle
(
  id_dim_confeccion NUMERIC(10) NOT NULL,
  id_dim_corte NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_dim_confeccion, id_dim_corte),
  FOREIGN KEY (id_dim_confeccion) REFERENCES Dimension_confeccion(id_dim_confeccion),
  FOREIGN KEY (id_dim_corte) REFERENCES Dimension_corte(id_dim_corte)
);

CREATE TABLE Transferencia_caja
(
  fecha_transferencia DATE NOT NULL,
  id_caja NUMERIC(10) NOT NULL,
  id_reserva CHAR(10) NOT NULL,
  area_envio NUMERIC(1) NOT NULL,
  area_destino NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_caja, id_reserva),
  FOREIGN KEY (id_caja) REFERENCES Caja(id_caja),
  FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva),
  FOREIGN KEY (area_envio) REFERENCES Area(id_area),
  FOREIGN KEY (area_destino) REFERENCES Area(id_area)
);

--Nivel 6
CREATE TABLE Reporte_uso
(
  cantidad_merma INT NOT NULL,
  fecha_fin_uso DATE NOT NULL,
  lote_usado NUMERIC(10) NOT NULL,
  lote_producido NUMERIC(10) NOT NULL,
  PRIMARY KEY (lote_usado, lote_producido),
  FOREIGN KEY (lote_usado) REFERENCES Lote(id_lote),
  FOREIGN KEY (lote_producido) REFERENCES Lote(id_lote)
);

CREATE TABLE Materia_Prima
(
  id_materia_prima NUMERIC(10) NOT NULL,
  id_lote NUMERIC(10) NOT NULL,
  id_dim_materia_prima NUMERIC(10) NOT NULL,
  ruc NUMERIC(11) NOT NULL,
  PRIMARY KEY (id_materia_prima),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote),
  FOREIGN KEY (id_dim_materia_prima) REFERENCES Dimension_materia_prima(id_dim_materia_prima),
  FOREIGN KEY (ruc) REFERENCES Proveedor(ruc)
);

CREATE TABLE Corte
(
  id_corte NUMERIC(10) NOT NULL,
  id_lote NUMERIC(10) NOT NULL,
  id_dim_corte NUMERIC(10) NOT NULL,
  id_maquina NUMERIC(3) NOT NULL,
  PRIMARY KEY (id_corte),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote),
  FOREIGN KEY (id_dim_corte) REFERENCES Dimension_corte(id_dim_corte),
  FOREIGN KEY (id_maquina) REFERENCES Maquina(id_maquina)
);

CREATE TABLE Confeccion
(
  id_confeccion NUMERIC(10) NOT NULL,
  id_lote NUMERIC(10) NOT NULL,
  id_dim_confeccion NUMERIC(10) NOT NULL,
  id_empleado NUMERIC(5) NOT NULL,
  PRIMARY KEY (id_confeccion),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote),
  FOREIGN KEY (id_dim_confeccion) REFERENCES Dimension_confeccion(id_dim_confeccion),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

CREATE TABLE Prenda
(
  id_prenda NUMERIC(10) NOT NULL,
  id_dim_prenda NUMERIC(10) NOT NULL,
  id_empleado NUMERIC(5) NOT NULL,
  PRIMARY KEY (id_prenda),
  FOREIGN KEY (id_dim_prenda) REFERENCES Dimension_prenda(id_dim_prenda),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

CREATE TABLE Orden_division
(
  id_orden_division NUMERIC(10) NOT NULL,
  estado VARCHAR(15) NOT NULL,
  fecha_creacion DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  id_lote NUMERIC(10) NOT NULL,
  id_descripcion NUMERIC(10) NOT NULL,
  id_tipo_division NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_orden_division),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote),
  FOREIGN KEY (id_descripcion) REFERENCES Descripcion(id_descripcion),
  FOREIGN KEY (id_tipo_division) REFERENCES Tipo_division(id_tipo_division)
);

CREATE TABLE Transferencia_lote
(
  fecha_transferencia DATE NOT NULL,
  id_reserva CHAR(10) NOT NULL,
  id_lote NUMERIC(10) NOT NULL,
  area_envio NUMERIC(1) NOT NULL,
  area_destino NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_reserva, id_lote),
  FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote),
  FOREIGN KEY (area_envio) REFERENCES Area(id_area),
  FOREIGN KEY (area_destino) REFERENCES Area(id_area)
);

CREATE TABLE Inspeccion_calidad
(
  fecha_inspeccion DATE NOT NULL,
  id_inspeccion NUMERIC(10) NOT NULL,
  estado VARCHAR(15) NOT NULL,
  cantidad_defectuosos INT NOT NULL,
  id_lote NUMERIC(10) NOT NULL,
  id_aql_lote_rango NUMERIC(2) NOT NULL,
  id_aql_nivel NUMERIC(1) NOT NULL,
  id_aql_codigo CHAR(1) NOT NULL,
  id_aql_significancia NUMERIC(1) NOT NULL,
  id_descripcion NUMERIC(10) NOT NULL,
  id_resultado NUMERIC(1) NOT NULL,
  PRIMARY KEY (id_inspeccion),
  FOREIGN KEY (id_lote) REFERENCES Lote(id_lote),
  FOREIGN KEY (id_aql_lote_rango, id_aql_nivel) REFERENCES AQL_muestra(id_aql_lote_rango, id_aql_nivel),
  FOREIGN KEY (id_aql_codigo, id_aql_significancia) REFERENCES AQL_resultado_rango(id_aql_codigo, id_aql_significancia),
  FOREIGN KEY (id_descripcion) REFERENCES Inspeccion_descripcion(id_descripcion),
  FOREIGN KEY (id_resultado) REFERENCES Tipo_resultado(id_resultado)
);

--Nivel 7
CREATE TABLE Maquina_programacion_orden
(
  fecha_programacion DATE NOT NULL,
  cantidad INT NOT NULL,
  id_maquina NUMERIC(3) NOT NULL,
  id_orden_division NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_maquina, id_orden_division),
  FOREIGN KEY (id_maquina) REFERENCES Maquina(id_maquina),
  FOREIGN KEY (id_orden_division) REFERENCES Orden_division(id_orden_division)
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

CREATE TABLE Caja_detalle_final
(
  id_caja_fin NUMERIC(10) NOT NULL,
  id_caja NUMERIC(10) NOT NULL,
  id_prenda NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_caja_fin),
  FOREIGN KEY (id_caja) REFERENCES Caja(id_caja),
  FOREIGN KEY (id_prenda) REFERENCES Prenda(id_prenda)
);

CREATE TABLE Gantt_progreso
(
  progreso_orden FLOAT NOT NULL,
  fecha_actualizacion DATE NOT NULL,
  id_gantt NUMERIC(10) NOT NULL,
  id_orden NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_gantt, id_orden),
  FOREIGN KEY (id_gantt) REFERENCES Gantt(id_gantt),
  FOREIGN KEY (id_orden) REFERENCES Orden_division(id_orden_division)
);

--Nivel 8
CREATE TABLE Reporte_acabado
(
  fecha_transformacion DATE NOT NULL,
  id_caja_inicio NUMERIC(10) NOT NULL,
  id_caja_fin NUMERIC(10) NOT NULL,
  PRIMARY KEY (id_caja_inicio, id_caja_fin),
  FOREIGN KEY (id_caja_inicio) REFERENCES Caja_detalle_inicial(id_caja_inicio),
  FOREIGN KEY (id_caja_fin) REFERENCES Caja_detalle_final(id_caja_fin)
);