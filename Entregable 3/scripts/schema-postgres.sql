--Limpiador de base de datos
--Nivel 1
DROP TABLE IF EXISTS direccion CASCADE;
DROP TABLE IF EXISTS correo CASCADE;
DROP TABLE IF EXISTS telefono CASCADE;
DROP TABLE IF EXISTS cargo CASCADE;
DROP TABLE IF EXISTS estado CASCADE;
DROP TABLE IF EXISTS tipo_materia_prima CASCADE;
DROP TABLE IF EXISTS color CASCADE;
DROP TABLE IF EXISTS tipo_parte_prenda CASCADE;
DROP TABLE IF EXISTS tipo_corte CASCADE;
DROP TABLE IF EXISTS tipo_lote CASCADE;
DROP TABLE IF EXISTS guia_confeccion CASCADE;
DROP TABLE IF EXISTS tipo_prenda CASCADE;
DROP TABLE IF EXISTS estilo_prenda CASCADE;
DROP TABLE IF EXISTS talla CASCADE;
DROP TABLE IF EXISTS genero CASCADE;
DROP TABLE IF EXISTS acabado CASCADE;
DROP TABLE IF EXISTS area CASCADE;
DROP TABLE IF EXISTS inspeccion_descripcion CASCADE;
DROP TABLE IF EXISTS aql_nivel CASCADE;
DROP TABLE IF EXISTS aql_lote_rango CASCADE;
DROP TABLE IF EXISTS aql_codigo CASCADE;
DROP TABLE IF EXISTS aql_significancia CASCADE;
DROP TABLE IF EXISTS tipo_resultado CASCADE;
--Nivel 2
DROP TABLE IF EXISTS proveedor CASCADE;
DROP TABLE IF EXISTS empleado CASCADE;
DROP TABLE IF EXISTS maquina CASCADE;
DROP TABLE IF EXISTS dimension_materia_prima CASCADE;
DROP TABLE IF EXISTS dimension_parte_prenda CASCADE;
DROP TABLE IF EXISTS dimension_confeccion CASCADE;
DROP TABLE IF EXISTS orden_pedido CASCADE;
DROP TABLE IF EXISTS plan_produccion CASCADE;
DROP TABLE IF EXISTS zona CASCADE;
DROP TABLE IF EXISTS aql_muestra CASCADE;
DROP TABLE IF EXISTS aql_resultado_rango CASCADE;
--Nivel 3
DROP TABLE IF EXISTS dimension_corte CASCADE;
DROP TABLE IF EXISTS parte_corte_detalle CASCADE;
DROP TABLE IF EXISTS dimension_prenda CASCADE;
DROP TABLE IF EXISTS orden_trabajo CASCADE;
DROP TABLE IF EXISTS pasillo CASCADE;
--Nivel 4
DROP TABLE IF EXISTS dim_confeccion_detalle CASCADE;
DROP TABLE IF EXISTS dim_prenda_detalle CASCADE;
DROP TABLE IF EXISTS pedido_detalle CASCADE;
DROP TABLE IF EXISTS estanteria CASCADE;
--Nivel 5
DROP TABLE IF EXISTS orden_producción CASCADE;
--Nivel 6
DROP TABLE IF EXISTS actividad_diaria CASCADE;
--Nivel 7
DROP TABLE IF EXISTS lote CASCADE;
DROP TABLE IF EXISTS empleado_actividad CASCADE;
DROP TABLE IF EXISTS maquina_actividad CASCADE;
DROP TABLE IF EXISTS caja_prenda CASCADE;
--Nivel 8
DROP TABLE IF EXISTS materia_prima CASCADE;
DROP TABLE IF EXISTS corte CASCADE;
DROP TABLE IF EXISTS registro_uso_lote CASCADE;
DROP TABLE IF EXISTS caja_lote CASCADE;
DROP TABLE IF EXISTS prenda CASCADE;
DROP TABLE IF EXISTS espacio CASCADE;
DROP TABLE IF EXISTS lote_salida CASCADE;
DROP TABLE IF EXISTS inspeccion_calidad CASCADE;
--Nivel 9
DROP TABLE IF EXISTS confeccion CASCADE;
DROP TABLE IF EXISTS registro_lote_caja CASCADE;
DROP TABLE IF EXISTS registro_transformacion_caja CASCADE;
DROP TABLE IF EXISTS caja_salida CASCADE;
DROP TABLE IF EXISTS lote_entrada CASCADE;

--Creador de tablas
--Nivel 1
CREATE TABLE direccion
(
  id_direccion SERIAL,
  descripcion VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_direccion)
);

CREATE TABLE correo
(
  id_correo SERIAL,
  direccion_correo VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_correo)
);

CREATE TABLE telefono
(
  id_telefono SERIAL,
  numero VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_telefono),
  UNIQUE (numero)
);

CREATE TABLE cargo
(
  id_cargo SERIAL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_cargo),
  UNIQUE (nombre)
);

CREATE TABLE estado
(
  id_estado SERIAL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_estado),
  UNIQUE (nombre)
);

CREATE TABLE tipo_materia_prima
(
  id_tipo_materia_prima SERIAL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_tipo_materia_prima),
  UNIQUE (nombre)
);

CREATE TABLE color
(
  id_color SERIAL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_color),
  UNIQUE (nombre)
);

CREATE TABLE tipo_parte_prenda
(
  id_tipo_parte_prenda SERIAL,
  nombre VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_tipo_parte_prenda),
  UNIQUE (nombre)
);

CREATE TABLE tipo_corte
(
  id_tipo_corte SERIAL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_tipo_corte),
  UNIQUE (nombre)
);

CREATE TABLE tipo_lote
(
  id_tipo_lote SERIAL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_tipo_lote),
  UNIQUE (nombre)
);

CREATE TABLE guia_confeccion
(
  id_guia_confeccion SERIAL,
  medida_pecho NUMERIC(2,2),
  medida_cintura NUMERIC(2,2),
  medida_cadera NUMERIC(2,2),
  medida_hombro NUMERIC(2,2),
  medida_longitud NUMERIC(2,2),
  medida_manga NUMERIC(2,2),
  medida_muslo NUMERIC(2,2),
  PRIMARY KEY (id_guia_confeccion)
);

CREATE TABLE tipo_prenda
(
  id_tipo_prenda SERIAL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_tipo_prenda),
  UNIQUE (nombre)
);

CREATE TABLE estilo_prenda
(
  id_estilo_prenda SERIAL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_estilo_prenda),
  UNIQUE (nombre)
);

CREATE TABLE talla
(
  id_talla SERIAL,
  nombre VARCHAR(4) NOT NULL,
  PRIMARY KEY (id_talla),
  UNIQUE (nombre)
);

CREATE TABLE genero
(
  id_genero SERIAL,
  nombre VARCHAR(10) NOT NULL,
  PRIMARY KEY (id_genero),
  UNIQUE (nombre)
);

CREATE TABLE acabado
(
  id_acabado SERIAL,
  nombre VARCHAR(9) NOT NULL,
  PRIMARY KEY (id_acabado),
  UNIQUE (nombre)
);

CREATE TABLE area
(
  id_area SERIAL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_area),
  UNIQUE (nombre)
);

CREATE TABLE inspeccion_descripcion
(
  id_descripcion SERIAL,
  descripcion VARCHAR(200) NOT NULL,
  PRIMARY KEY (id_descripcion)
);

CREATE TABLE aql_nivel
(
  id_aql_nivel SERIAL,
  nombre CHAR(2) NOT NULL,
  PRIMARY KEY (id_aql_nivel),
  UNIQUE (nombre)
);

CREATE TABLE aql_lote_rango
(
  id_aql_lote_rango SERIAL,
  min_lote INT NOT NULL,
  max_lote INT NOT NULL,
  PRIMARY KEY (id_aql_lote_rango)
);

CREATE TABLE aql_codigo
(
  id_aql_codigo CHAR(1),
  tamano_muestra INT NOT NULL,
  PRIMARY KEY (id_aql_codigo),
  UNIQUE (tamano_muestra)
);

CREATE TABLE aql_significancia
(
  id_aql_significancia SERIAL,
  nivel_significancia NUMERIC(1,3) NOT NULL,
  PRIMARY KEY (id_aql_significancia),
  UNIQUE (nivel_significancia)
);

CREATE TABLE tipo_resultado
(
  id_resultado SERIAL,
  nombre VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_resultado),
  UNIQUE (nombre)
);

-- Nivel 2
CREATE TABLE proveedor
(
  id_proveedor SERIAL,
  ruc NUMERIC(11) NOT NULL,
  denominacion_social VARCHAR(100) NOT NULL,
  id_direccion INT NOT NULL,
  id_telefono INT NOT NULL,
  id_correo INT NOT NULL,
  PRIMARY KEY (id_proveedor),
  FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion),
  FOREIGN KEY (id_telefono) REFERENCES telefono(id_telefono),
  FOREIGN KEY (id_correo) REFERENCES correo(id_correo),
  UNIQUE (ruc)
);

CREATE TABLE empleado
(
  id_empleado SERIAL,
  dni NUMERIC(8) NOT NULL,
  nombre VARCHAR(30) NOT NULL,
  segundo_apellido VARCHAR(15) NOT NULL,
  primer_apellido VARCHAR(15) NOT NULL,
  id_area INT NOT NULL,
  id_direccion INT NOT NULL,
  id_telefono INT NOT NULL,
  id_correo INT NOT NULL,
  id_cargo INT NOT NULL,
  PRIMARY KEY (id_empleado),
  FOREIGN KEY (id_area) REFERENCES area(id_area),
  FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion),
  FOREIGN KEY (id_telefono) REFERENCES telefono(id_telefono),
  FOREIGN KEY (id_correo) REFERENCES correo(id_correo),
  FOREIGN KEY (id_cargo) REFERENCES cargo(id_cargo),
  UNIQUE (dni)
);

CREATE TABLE maquina
(
  id_maquina SERIAL,
  capacidad_total INT NOT NULL,
  id_estado INT NOT NULL,
  PRIMARY KEY (id_maquina),
  FOREIGN KEY (id_estado) REFERENCES estado(id_estado)
);

CREATE TABLE dimension_materia_prima
(
  id_dim_materia_prima SERIAL,
  id_tipo_materia_prima INT NOT NULL,
  id_color INT NOT NULL,
  PRIMARY KEY (id_dim_materia_prima),
  FOREIGN KEY (id_color) REFERENCES color(id_color),
  FOREIGN KEY (id_tipo_materia_prima) REFERENCES tipo_materia_prima(id_tipo_materia_prima)
);

CREATE TABLE dimension_parte_prenda
(
  id_dim_parte_prenda SERIAL,
  id_tipo_parte_prenda INT NOT NULL,
  PRIMARY KEY (id_dim_parte_prenda),
  FOREIGN KEY (id_tipo_parte_prenda) REFERENCES tipo_parte_prenda(id_tipo_parte_prenda)
);

CREATE TABLE dimension_confeccion
(
  id_dim_confeccion SERIAL,
  id_tipo_prenda INT NOT NULL,
  id_estilo_prenda INT NOT NULL,
  id_guia_confeccion INT NOT NULL,
  id_talla INT NOT NULL,
  id_genero INT NOT NULL,
  PRIMARY KEY (id_dim_confeccion),
  FOREIGN KEY (id_tipo_prenda) REFERENCES tipo_prenda(id_tipo_prenda),
  FOREIGN KEY (id_estilo_prenda) REFERENCES estilo_prenda(id_estilo_prenda),
  FOREIGN KEY (id_guia_confeccion) REFERENCES guia_confeccion(id_guia_confeccion),
  FOREIGN KEY (id_talla) REFERENCES talla(id_talla),
  FOREIGN KEY (id_genero) REFERENCES genero(id_genero)
);

CREATE TABLE orden_pedido
(
  id_orden_pedido SERIAL,
  fecha_entrega TIMESTAMPTZ NOT NULL,
  id_estado INT NOT NULL,
  fecha_creacion TIMESTAMP NOT NULL,
  PRIMARY KEY (id_orden_pedido),
  FOREIGN KEY (id_estado) REFERENCES estado(id_estado)
);

CREATE TABLE plan_produccion
(
  id_plan SERIAL,
  fecha_inicio DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  id_estado INT NOT NULL,
  fecha_creacion TIMESTAMP NOT NULL,
  PRIMARY KEY (id_plan),
  FOREIGN KEY (id_estado) REFERENCES estado(id_estado)
);

CREATE TABLE zona
(
  id_zona NUMERIC(3),
  nombre VARCHAR(19) NOT NULL,
  id_area INT NOT NULL,
  PRIMARY KEY (id_zona),
  FOREIGN KEY (id_area) REFERENCES area(id_area),
  UNIQUE (nombre)
);

CREATE TABLE aql_muestra
(
  id_aql_nivel INT,
  id_aql_lote_rango INT,
  id_aql_codigo CHAR(1) NOT NULL,
  PRIMARY KEY (id_aql_nivel, id_aql_lote_rango),
  FOREIGN KEY (id_aql_codigo) REFERENCES aql_codigo(id_aql_codigo),
  FOREIGN KEY (id_aql_lote_rango) REFERENCES aql_lote_rango(id_aql_lote_rango),
  FOREIGN KEY (id_aql_nivel) REFERENCES aql_nivel(id_aql_nivel)
);

CREATE TABLE aql_resultado_rango
(
  id_aql_codigo CHAR(1),
  id_aql_significancia INT,
  max_aceptacion INT NOT NULL,
  min_rechazo INT NOT NULL,
  PRIMARY KEY (id_aql_codigo, id_aql_significancia),
  FOREIGN KEY (id_aql_codigo) REFERENCES aql_codigo(id_aql_codigo),
  FOREIGN KEY (id_aql_significancia) REFERENCES aql_significancia(id_aql_significancia)
);

--Nivel 3
CREATE TABLE dimension_corte
(
  id_dim_corte SERIAL,
  id_dim_materia_prima INT NOT NULL,
  id_dim_parte_prenda INT NOT NULL,
  PRIMARY KEY (id_dim_corte),
  FOREIGN KEY (id_dim_materia_prima) REFERENCES dimension_materia_prima(id_dim_materia_prima),
  FOREIGN KEY (id_dim_parte_prenda) REFERENCES dimension_parte_prenda(id_dim_parte_prenda)
);

CREATE TABLE parte_corte_detalle
(
  id_dim_parte_prenda INT,
  id_tipo_corte INT,
  medida NUMERIC(2,2) NOT NULL,
  PRIMARY KEY (id_dim_parte_prenda, id_tipo_corte),
  FOREIGN KEY (id_dim_parte_prenda) REFERENCES dimension_parte_prenda(id_dim_parte_prenda),
  FOREIGN KEY (id_tipo_corte) REFERENCES tipo_corte(id_tipo_corte)
);

CREATE TABLE dimension_prenda
(
  id_dim_prenda SERIAL,
  id_dim_confeccion INT NOT NULL,
  PRIMARY KEY (id_dim_prenda),
  FOREIGN KEY (id_dim_confeccion) REFERENCES dimension_confeccion(id_dim_confeccion)
);

CREATE TABLE orden_trabajo
(
  id_orden_trabajo SERIAL,
  fecha_inicio DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  prioridad INT NOT NULL,
  id_estado INT NOT NULL,
  id_plan INT NOT NULL,
  id_orden_pedido INT NOT NULL,
  fecha_creacion TIMESTAMP NOT NULL,
  PRIMARY KEY (id_orden_trabajo),
  FOREIGN KEY (id_estado) REFERENCES estado(id_estado),
  FOREIGN KEY (id_plan) REFERENCES plan_produccion(id_plan),
  FOREIGN KEY (id_orden_pedido) REFERENCES orden_pedido(id_orden_pedido)  
);

CREATE TABLE pasillo
(
  id_pasillo NUMERIC(5),
  largo_pasillo NUMERIC(2,2) NOT NULL,
  ancho_pasillo NUMERIC(2,2) NOT NULL,
  id_zona NUMERIC(3) NOT NULL,
  PRIMARY KEY (id_pasillo),
  FOREIGN KEY (id_zona) REFERENCES zona(id_zona)
);

--Nivel 4
CREATE TABLE dim_confeccion_detalle
(
  id_dim_confeccion SERIAL,
  id_dim_corte INT NOT NULL,
  PRIMARY KEY (id_dim_confeccion, id_dim_corte),
  FOREIGN KEY (id_dim_confeccion) REFERENCES dimension_confeccion(id_dim_confeccion),
  FOREIGN KEY (id_dim_corte) REFERENCES dimension_corte(id_dim_corte)
);

CREATE TABLE dim_prenda_detalle
(
  id_dim_prenda INT,
  id_acabado INT,
  PRIMARY KEY (id_dim_prenda, id_acabado),
  FOREIGN KEY (id_dim_prenda) REFERENCES dimension_prenda(id_dim_prenda),
  FOREIGN KEY (id_acabado) REFERENCES acabado(id_acabado)
);

CREATE TABLE pedido_detalle
(
  id_orden_pedido INT,
  id_dim_prenda INT,
  PRIMARY KEY (id_orden_pedido, id_dim_prenda),
  FOREIGN KEY (id_orden_pedido) REFERENCES orden_pedido(id_orden_pedido),
  FOREIGN KEY (id_dim_prenda) REFERENCES dimension_prenda(id_dim_prenda)
);

CREATE TABLE estanteria
(
  id_estanteria NUMERIC(7),
  ancho_estanteria NUMERIC(2,2) NOT NULL,
  largo_estanteria NUMERIC(2,2) NOT NULL,
  alto_estanteria NUMERIC(2,2) NOT NULL,
  id_pasillo NUMERIC(5) NOT NULL,
  PRIMARY KEY (id_estanteria),
  FOREIGN KEY (id_pasillo) REFERENCES pasillo(id_pasillo)
);

--Nivel 5
CREATE TABLE orden_producción
(
  id_orden_producción SERIAL,
  fecha_fin DATE NOT NULL,
  fecha_inicio DATE NOT NULL,
  cantidad INT NOT NULL,
  estado VARCHAR(15) NOT NULL,
  id_area INT NOT NULL,
  id_dim_prenda INT,
  id_dim_confeccion INT,
  id_dim_corte INT,
  id_orden_trabajo INT NOT NULL,
  fecha_creacion TIMESTAMP NOT NULL,
  PRIMARY KEY (id_orden_producción),
  FOREIGN KEY (id_area) REFERENCES area(id_area),
  FOREIGN KEY (id_dim_prenda) REFERENCES dimension_prenda(id_dim_prenda),
  FOREIGN KEY (id_dim_confeccion) REFERENCES dimension_confeccion(id_dim_confeccion),
  FOREIGN KEY (id_dim_corte) REFERENCES dimension_corte(id_dim_corte),
  FOREIGN KEY (id_orden_trabajo) REFERENCES orden_trabajo(id_orden_trabajo)
);

--Nivel 6
CREATE TABLE actividad_diaria
(
  id_actividad SERIAL,
  fecha_actividad DATE NOT NULL,
  id_orden_producción INT NOT NULL,
  PRIMARY KEY (id_actividad),
  FOREIGN KEY (id_orden_producción) REFERENCES orden_producción(id_orden_producción)
);

--Nivel 7
CREATE TABLE lote
(
  id_lote SERIAL,
  cantidad INT NOT NULL,
  estado VARCHAR(15) NOT NULL,
  id_tipo_lote INT NOT NULL,
  id_dim_corte INT,
  id_dim_confeccion INT,
  id_dim_materia_prima INT,
  id_actividad INT NOT NULL,
  fecha_creacion TIMESTAMP NOT NULL,
  PRIMARY KEY (id_lote),
  FOREIGN KEY (id_tipo_lote) REFERENCES tipo_lote(id_tipo_lote),
  FOREIGN KEY (id_dim_corte) REFERENCES dimension_corte(id_dim_corte),
  FOREIGN KEY (id_dim_confeccion) REFERENCES dimension_confeccion(id_dim_confeccion),
  FOREIGN KEY (id_dim_materia_prima) REFERENCES dimension_materia_prima(id_dim_materia_prima),
  FOREIGN KEY (id_actividad) REFERENCES actividad_diaria(id_actividad)
);

CREATE TABLE empleado_actividad
(
  id_actividad INT,
  id_empleado INT,
  cantidad_hecha INT NOT NULL,
  PRIMARY KEY (id_actividad, id_empleado),
  FOREIGN KEY (id_actividad) REFERENCES actividad_diaria(id_actividad),
  FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
);

CREATE TABLE maquina_actividad
(
  id_actividad INT,
  id_maquina INT,
  cantidad_hecha INT NOT NULL,
  PRIMARY KEY (id_actividad, id_maquina),
  FOREIGN KEY (id_actividad) REFERENCES actividad_diaria(id_actividad),
  FOREIGN KEY (id_maquina) REFERENCES maquina(id_maquina)
);

CREATE TABLE caja_prenda
(
  id_caja SERIAL,
  cantidad INT NOT NULL,
  fecha_creacion INT NOT NULL,
  estado VARCHAR(15) NOT NULL,
  id_dim_prenda INT NOT NULL,
  id_actividad INT NOT NULL,
  PRIMARY KEY (id_caja),
  FOREIGN KEY (id_dim_prenda) REFERENCES dimension_prenda(id_dim_prenda),
  FOREIGN KEY (id_actividad) REFERENCES actividad_diaria(id_actividad)
);
--Nivel 8
CREATE TABLE materia_Prima
(
  id_materia_prima SERIAL,
  id_lote INT NOT NULL,
  id_dim_materia_prima INT NOT NULL,
  id_proveedor INT NOT NULL,
  PRIMARY KEY (id_materia_prima),
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote),
  FOREIGN KEY (id_dim_materia_prima) REFERENCES dimension_materia_prima(id_dim_materia_prima),
  FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor)
);

CREATE TABLE corte
(
  id_corte SERIAL,
  id_lote INT NOT NULL,
  id_dim_corte INT NOT NULL,
  id_maquina INT NOT NULL,
  PRIMARY KEY (id_corte),
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote),
  FOREIGN KEY (id_dim_corte) REFERENCES dimension_corte(id_dim_corte),
  FOREIGN KEY (id_maquina) REFERENCES maquina(id_maquina)
);

CREATE TABLE registro_uso_lote
(
  id_actividad INT,
  id_lote INT,
  cantidad_usada INT NOT NULL,
  PRIMARY KEY (id_actividad, id_lote),
  FOREIGN KEY (id_actividad) REFERENCES actividad_diaria(id_actividad),
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote)
);

CREATE TABLE caja_lote
(
  id_caja SERIAL,
  cantidad INT NOT NULL,
  id_lote INT NOT NULL,
  id_estado INT NOT NULL,
  PRIMARY KEY (id_caja),
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote),
  FOREIGN KEY (id_estado) REFERENCES estado(id_estado)
);

CREATE TABLE prenda
(
  id_prenda SERIAL,
  id_dim_prenda INT NOT NULL,
  id_empleado INT NOT NULL,
  id_caja INT NOT NULL,
  PRIMARY KEY (id_prenda),
  FOREIGN KEY (id_dim_prenda) REFERENCES dimension_prenda(id_dim_prenda),
  FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado),
  FOREIGN KEY (id_caja) REFERENCES caja_prenda(id_caja)
);

CREATE TABLE espacio
(
  id_espacio NUMERIC(9),
  ancho NUMERIC(2,2) NOT NULL,
  largo NUMERIC(2,2) NOT NULL,
  alto NUMERIC(2,2) NOT NULL,
  estado VARCHAR(20) NOT NULL,
  id_lote INT,
  id_estanteria NUMERIC(7) NOT NULL,
  PRIMARY KEY (id_espacio),
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote),
  FOREIGN KEY (id_estanteria) REFERENCES estanteria(id_estanteria),
  UNIQUE (id_lote)
);

CREATE TABLE lote_salida
(
  id_salida SERIAL,
  fecha_salida TIMESTAMP NOT NULL,
  id_lote INT NOT NULL,
  area_envio INT NOT NULL,
  PRIMARY KEY (id_salida),
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote),
  FOREIGN KEY (area_envio) REFERENCES area(id_area)
);

CREATE TABLE inspeccion_calidad
(
  id_inspeccion SERIAL,
  fecha_inspeccion TIMESTAMP NOT NULL,
  estado VARCHAR(15) NOT NULL,
  cantidad_defectuosos INT NOT NULL,
  id_lote INT NOT NULL,
  id_aql_lote_rango INT NOT NULL,
  id_aql_nivel INT NOT NULL,
  id_aql_codigo CHAR(1) NOT NULL,
  id_aql_significancia INT NOT NULL,
  id_descripcion INT NOT NULL,
  id_resultado INT NOT NULL,
  PRIMARY KEY (id_inspeccion),
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote),
  FOREIGN KEY (id_aql_lote_rango, id_aql_nivel) REFERENCES aql_muestra(id_aql_lote_rango, id_aql_nivel),
  FOREIGN KEY (id_aql_codigo, id_aql_significancia) REFERENCES aql_resultado_rango(id_aql_codigo, id_aql_significancia),
  FOREIGN KEY (id_descripcion) REFERENCES inspeccion_descripcion(id_descripcion),
  FOREIGN KEY (id_resultado) REFERENCES tipo_resultado(id_resultado)
);

--Nivel 9
CREATE TABLE confeccion
(
  id_confeccion SERIAL,
  id_lote INT NOT NULL,
  id_dim_confeccion INT NOT NULL,
  id_empleado INT NOT NULL,
  id_caja INT,
  PRIMARY KEY (id_confeccion),
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote),
  FOREIGN KEY (id_dim_confeccion) REFERENCES dimension_confeccion(id_dim_confeccion),
  FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado),
  FOREIGN KEY (id_caja) REFERENCES caja_lote(id_caja)
);

CREATE TABLE registro_lote_caja
(
  id_lote INT,
  id_caja INT,
  fecha_transicion DATE NOT NULL,
  PRIMARY KEY (id_lote, id_caja),
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote),
  FOREIGN KEY (id_caja) REFERENCES caja_lote(id_caja)
);

CREATE TABLE registro_transformacion_caja
(
  id_actividad SERIAL,
  id_caja INT NOT NULL,
  PRIMARY KEY (id_actividad, id_caja),
  FOREIGN KEY (id_actividad) REFERENCES actividad_diaria(id_actividad),
  FOREIGN KEY (id_caja) REFERENCES caja_lote(id_caja)
);

CREATE TABLE caja_salida
(
  id_salida SERIAL,
  fecha_salida TIMESTAMP NOT NULL,
  id_caja INT NOT NULL,
  id_area INT NOT NULL,
  PRIMARY KEY (id_salida),
  FOREIGN KEY (id_caja) REFERENCES caja_lote(id_caja),
  FOREIGN KEY (id_area) REFERENCES area(id_area)
);

CREATE TABLE Lote_entrada
(
  id_entrada SERIAL,
  fecha_entrada TIMESTAMP NOT NULL,
  id_lote INT NOT NULL,
  id_espacio INT NOT NULL,
  PRIMARY KEY (id_entrada),
  FOREIGN KEY (id_lote) REFERENCES lote(id_lote),
  FOREIGN KEY (id_espacio) REFERENCES espacio(id_espacio)
);




