import psycopg2
import tkinter as tk
from tkinter import simpledialog, messagebox
import random
from faker import Faker
import re
from datetime import timedelta
import pytz

fake = Faker('es_ES')  # Usamos es_ES para generar datos en español

def connect_to_database(host, port, database, user, password): #Conecta a la base de datos
    try:
        # Conectar a la base de datos
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        messagebox.showinfo('Éxito', 'Conexión exitosa')
        return connection
    except psycopg2.Error as e:
        messagebox.showerror('Error', f'Error al conectar a la base de datos: {e}')
        return None

def insert_cargos(cursor, cargos): #Inserta cargos
    try:
        for cargo in cargos:
            cursor.execute("INSERT INTO cargo (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_cargo;", (cargo,))
            id_cargo = cursor.fetchone()
            if id_cargo:
                print(f"Inserted cargo: {cargo}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar cargos: {e}")

def insert_estados(cursor, estados): #Inserta estados
    try:
        for estado in estados:
            cursor.execute("INSERT INTO estado (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_estado;", (estado,))
            id_estado = cursor.fetchone()
            if id_estado:
                print(f"Inserted estado: {estado}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar estados: {e}")

def insert_tipos_mp(cursor, tipos_mp): #Inserta tipos de materia prima
    try:
        for tipo_mp in tipos_mp:
            cursor.execute("INSERT INTO tipo_materia_prima (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_tipo_materia_prima;", (tipo_mp,))
            id_tipo_materia_prima = cursor.fetchone()
            if id_tipo_materia_prima:
                print(f"Inserted tipo de materia prima: {tipo_mp}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar tipos de materia prima: {e}")

def insert_colores(cursor, colores): #Inserta colores
    try:
        for color in colores:
            cursor.execute("INSERT INTO color (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_color;", (color,))
            id_color = cursor.fetchone()
            if id_color:
                print(f"Inserted color: {color}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar colores: {e}")

def insert_tipos_partes_prenda(cursor, tipos_partes_prenda): #Inserta tipos de partes de prenda
    try:
        for tipo_parte_prenda in tipos_partes_prenda:
            cursor.execute("INSERT INTO tipo_parte_prenda (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_tipo_parte_prenda;", (tipo_parte_prenda,))
            id_tipo_parte_prenda = cursor.fetchone()
            if id_tipo_parte_prenda:
                print(f"Inserted tipo de parte de prenda: {tipo_parte_prenda}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar tipos de partes de prenda: {e}")

def insert_tipos_cortes(cursor, tipos_cortes): #Inserta tipos de cortes
    try:
        for tipo_corte in tipos_cortes:
            cursor.execute("INSERT INTO tipo_corte (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_tipo_corte;", (tipo_corte,))
            id_tipo_corte = cursor.fetchone()
            if id_tipo_corte:
                print(f"Inserted tipo de corte: {tipo_corte}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar tipos de cortes: {e}")

def insert_tipos_lotes(cursor, tipos_lotes): #Inserta tipos de lotes
    try:
        for tipo_lote in tipos_lotes:
            cursor.execute("INSERT INTO tipo_lote (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_tipo_lote;", (tipo_lote,))
            id_tipo_lote = cursor.fetchone()
            if id_tipo_lote:
                print(f"Inserted tipo de lote: {tipo_lote}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar tipos de lotes: {e}")

def insert_tipos_prendas(cursor, tipos_prendas): #Inserta tipos de prendas
    try:
        for tipo_prenda in tipos_prendas:
            cursor.execute("INSERT INTO tipo_prenda (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_tipo_prenda;", (tipo_prenda,))
            id_tipo_prenda = cursor.fetchone()
            if id_tipo_prenda:
                print(f"Inserted tipo de prenda: {tipo_prenda}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar tipos de prendas: {e}")

def insert_estilos_prendas(cursor, estilos_prendas): #Inserta estilos de prendas
    try:
        for estilo_prenda in estilos_prendas:
            cursor.execute("INSERT INTO estilo_prenda (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_estilo_prenda;", (estilo_prenda,))
            id_estilo_prenda = cursor.fetchone()
            if id_estilo_prenda:
                print(f"Inserted estilo de prenda: {estilo_prenda}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar estilos de prendas: {e}")

def insert_tallas(cursor, tallas): #Inserta tallas
    try:
        for talla in tallas:
            cursor.execute("INSERT INTO talla (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_talla;", (talla,))
            id_talla = cursor.fetchone()
            if id_talla:
                print(f"Inserted talla: {talla}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar tallas: {e}")

def insert_generos(cursor, generos): #Inserta géneros
    try:
        for genero in generos:
            cursor.execute("INSERT INTO genero (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_genero;", (genero,))
            id_genero = cursor.fetchone()
            if id_genero:
                print(f"Inserted género: {genero}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar géneros: {e}")

def insert_acabados(cursor, acabados): #Inserta acabados
    try:
        for acabado in acabados:
            cursor.execute("INSERT INTO acabado (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_acabado;", (acabado,))
            id_acabado = cursor.fetchone()
            if id_acabado:
                print(f"Inserted acabado: {acabado}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar acabados: {e}")

def insert_areas(cursor, areas): #Inserta áreas
    try:
        for area in areas:
            cursor.execute("INSERT INTO area (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_area;", (area,))
            id_area = cursor.fetchone()
            if id_area:
                print(f"Inserted area: {area}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar áreas: {e}")

def insert_aql_niveles(cursor, aql_niveles): #Inserta niveles AQL
    try:
        for aql_nivel in aql_niveles:
            cursor.execute("INSERT INTO aql_nivel (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_aql_nivel;", (aql_nivel,))
            id_aql_nivel = cursor.fetchone()
            if id_aql_nivel:
                print(f"Inserted nivel AQL: {aql_nivel}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar niveles AQL: {e}")

def insert_aql_lote_rangos(cursor, aql_lote_rangos): #Inserta rangos de lote AQL
    try:
        for aql_lote_rango in aql_lote_rangos:
            cursor.execute("INSERT INTO aql_lote_rango (min_lote, max_lote) VALUES (%s, %s) RETURNING id_aql_lote_rango;", (aql_lote_rango[0],aql_lote_rango[1]))
            id_aql_lote_rango = cursor.fetchone()
            if id_aql_lote_rango:
                print(f"Inserted rango de lote AQL: min_lote={aql_lote_rango[0]}, max_lote={aql_lote_rango[1]}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar rangos de lote AQL: {e}")

def insert_aql_codigos(cursor, aql_codigos): #Inserta códigos AQL
    try:
        for aql_codigo in aql_codigos:
            cursor.execute("INSERT INTO aql_codigo (id_aql_codigo, tamaño_muestra) VALUES (%s, %s) ON CONFLICT (tamaño_muestra) DO NOTHING RETURNING id_aql_codigo;", (aql_codigo[0], aql_codigo[1]))
            id_aql_codigo = cursor.fetchone()
            if id_aql_codigo:
                print(f"Inserted código AQL: id_aql_codigo={aql_codigo[0]}, tamaño_muestra={aql_codigo[1]}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar códigos AQL: {e}")

def insert_aql_significancias(cursor, aql_significancias): #Inserta significancias AQL
    try:
        for aql_significancia in aql_significancias:
            cursor.execute("INSERT INTO aql_significancia (nivel_significancia) VALUES (%s) ON CONFLICT (nivel_significancia) DO NOTHING RETURNING id_aql_significancia;", (aql_significancia,))
            id_aql_significancia = cursor.fetchone()
            if id_aql_significancia:
                print(f"Inserted significancia AQL: {aql_significancia}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar significancias AQL: {e}")

def insert_resultados(cursor, resultados): #Inserta tipos de resultados
    try:
        for resultado in resultados:
            cursor.execute("INSERT INTO resultado (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_resultado;", (resultado,))
            id_resultado = cursor.fetchone()
            if id_resultado:
                print(f"Inserted resultado: {resultado}")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar resultados: {e}")

def insert_proveedor(cursor): #Inserta proveedores, direccion, telefono y email
    try:

        # Función para generar correos basados en la denominación social del proveedor
        def generate_email(denominacion_social):
            denominacion_social = denominacion_social.replace(' ', '_').lower()
            return f"comercial@{re.sub('[^0-9a-zA-Z_]', '', denominacion_social)}.com"

        # Generar registros para proveedor
        for _ in range(20):
            ruc = fake.unique.random_number(digits=11)
            denominacion_social = fake.company()[:30]

            direccion = fake.address()
            cursor.execute("INSERT INTO direccion (descripcion) VALUES (%s) RETURNING id_direccion;", (direccion,))
            id_direccion = cursor.fetchone()[0]

            telefono = fake.unique.random_number(digits=8, fix_len=True)
            telefono = f"9{telefono}"  # Aseguramos que empieza con 9 y tiene 9 dígitos
            cursor.execute("INSERT INTO telefono (numero) VALUES (%s) RETURNING id_telefono;", (telefono,))
            id_telefono = cursor.fetchone()[0]

            correo = generate_email(denominacion_social)
            cursor.execute("INSERT INTO correo (direccion_correo) VALUES (%s) RETURNING id_correo;", (correo,))
            id_correo = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO proveedor (ruc, denominacion_social, id_direccion, id_telefono, id_correo)
                VALUES (%s, %s, %s, %s, %s);
            """, (ruc, denominacion_social, id_direccion, id_telefono, id_correo))

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar proveedores: {e}")

def insert_empleados(cursor): #Inserta empleados, direccion, telefono y email
    try:
        area_cargo_relations = {
            'Almacén Central': ('Almacenero', 'Jefe'),
            'Corte': ('Operario', 'Jefe'),
            'Confección': ('Costurero', 'Jefe'),
            'Almacén de tránsito': ('Almacenero', 'Jefe'),
            'Acabado': ('Operario', 'Jefe'),
            'Calidad': ('Inspector', 'Jefe'),
            'Planeamiento': ('Planificador', 'Jefe')
        }

        # Función para generar correos basados en nombre y primer apellido
        def generate_email(nombre, primer_apellido):
            email_domain = fake.free_email_domain()
            return f"{nombre}.{primer_apellido}@{email_domain}".lower()

        # Generar registros para empleado
        for area, (empleado_cargo, jefe_cargo) in area_cargo_relations.items():
            # Insertar jefe
            for _ in range(1):  # Un solo empleado jefe por área
                dni = fake.unique.random_number(digits=8)
                nombre = fake.first_name()[:15] + ' ' + fake.first_name()[:14]
                primer_apellido = fake.last_name()[:15]
                segundo_apellido = fake.last_name()[:15]

                cursor.execute("SELECT id_area FROM area WHERE nombre=%s;", (area,))
                id_area = cursor.fetchone()[0]

                cursor.execute("SELECT id_cargo FROM cargo WHERE nombre=%s;", (jefe_cargo,))
                id_cargo = cursor.fetchone()[0]

                direccion = fake.address()
                cursor.execute("INSERT INTO direccion (descripcion) VALUES (%s) RETURNING id_direccion;", (direccion,))
                id_direccion = cursor.fetchone()[0]

                telefono = fake.unique.random_number(digits=8, fix_len=True)
                telefono = f"9{telefono}"  # Aseguramos que empieza con 9 y tiene 9 dígitos
                cursor.execute("INSERT INTO telefono (numero) VALUES (%s) RETURNING id_telefono;", (telefono,))
                id_telefono = cursor.fetchone()[0]

                correo = generate_email(nombre, primer_apellido)
                cursor.execute("INSERT INTO correo (direccion_correo) VALUES (%s) RETURNING id_correo;", (correo,))
                id_correo = cursor.fetchone()[0]

                cursor.execute("""
                    INSERT INTO empleado (dni, nombre, segundo_apellido, primer_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (dni, nombre, segundo_apellido, primer_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo))
                
                print(f"Inserted jefe: {dni}, {nombre} {primer_apellido} {segundo_apellido}, área: {area}, cargo: {jefe_cargo}")
            
            # Insertar otros empleados
            for _ in range(10):  # Diez empleados por área con otros cargos
                dni = fake.unique.random_number(digits=8)
                nombre = fake.first_name()[:15] + ' ' + fake.first_name()[:14]
                primer_apellido = fake.last_name()[:15]
                segundo_apellido = fake.last_name()[:15]

                cursor.execute("SELECT id_area FROM area WHERE nombre=%s;", (area,))
                id_area = cursor.fetchone()[0]

                cursor.execute("SELECT id_cargo FROM cargo WHERE nombre=%s;", (empleado_cargo,))
                id_cargo = cursor.fetchone()[0]

                direccion = fake.address()
                cursor.execute("INSERT INTO direccion (descripcion) VALUES (%s) RETURNING id_direccion;", (direccion,))
                id_direccion = cursor.fetchone()[0]

                telefono = fake.unique.random_number(digits=8, fix_len=True)
                telefono = f"9{telefono}"  # Aseguramos que empieza con 9 y tiene 9 dígitos
                cursor.execute("INSERT INTO telefono (numero) VALUES (%s) RETURNING id_telefono;", (telefono,))
                id_telefono = cursor.fetchone()[0]

                correo = generate_email(nombre, primer_apellido)
                cursor.execute("INSERT INTO correo (direccion_correo) VALUES (%s) RETURNING id_correo;", (correo,))
                id_correo = cursor.fetchone()[0]

                cursor.execute("""
                    INSERT INTO empleado (dni, nombre, segundo_apellido, primer_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (dni, nombre, segundo_apellido, primer_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo))

                print(f"Inserted empleado: {dni}, {nombre} {primer_apellido} {segundo_apellido}, área: {area}, cargo: {empleado_cargo}")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar empleados: {e}")

def insert_maquinas(cursor): #Inserta máquinas
    try:
        maquina_estado_relations = {
            'Maquina': ('Disponible', 'No disponible', 'En mantenimiento'),
        }
        # Obtener todos los id_estado relacionados con 'Orden_pedido'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(maquina_estado_relations['Maquina']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]
        
        if not estado_ids:
            raise ValueError("No se encontraron estados válidos en la tabla estado")

        for _ in range(30):
            capacidad_total = random.randint(2, 5) * 1000
            id_estado = random.choice(estado_ids)  # Seleccionar un estado aleatorio

            cursor.execute("INSERT INTO maquina (capacidad_total, id_estado) VALUES (%s, %s) RETURNING id_maquina;", (capacidad_total, id_estado))
            id_maquina = cursor.fetchone()[0]
            if id_maquina:
                print(f"Inserted máquina: {id_maquina}, capacidad_total: {capacidad_total}, id_estado: {id_estado}")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar máquinas: {e}")

def insert_dimension_materia_prima(cursor): #Inserta dimensiones de materia prima
    try:
        # Obtener todos los id_tipo_materia_prima
        cursor.execute("SELECT id_tipo_materia_prima FROM tipo_materia_prima;")
        tipos_materia_prima = cursor.fetchall()
        tipo_materia_prima_ids = [tipo[0] for tipo in tipos_materia_prima]

        # Obtener todos los id_color
        cursor.execute("SELECT id_color FROM color;")
        colores = cursor.fetchall()
        color_ids = [color[0] for color in colores]

        if not tipo_materia_prima_ids:
            raise ValueError("No se encontraron tipos de materia prima en la tabla tipo_materia_prima")
        if not color_ids:
            raise ValueError("No se encontraron colores en la tabla color")

        for _ in range(100):
            id_tipo_materia_prima = random.choice(tipo_materia_prima_ids)
            id_color = random.choice(color_ids)

            cursor.execute("""
                INSERT INTO dimension_materia_prima (id_tipo_materia_prima, id_color)
                VALUES (%s, %s) RETURNING id_dim_materia_prima;
            """, (id_tipo_materia_prima, id_color))
            id_dim_materia_prima = cursor.fetchone()[0]
            if id_dim_materia_prima:
                print(f"Inserted dimension_materia_prima: {id_dim_materia_prima}, id_tipo_materia_prima: {id_tipo_materia_prima}, id_color: {id_color}")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar dimensiones de materia prima: {e}")

def insert_dimension_parte_prenda(cursor): #Inserta dimensiones de materia prima
    try:
        # Obtener todos los id_tipo_parte_prenda
        cursor.execute("SELECT id_tipo_parte_prenda FROM tipo_parte_prenda;")
        tipos_parte_prenda = cursor.fetchall()
        tipo_parte_prenda_ids = [tipo[0] for tipo in tipos_parte_prenda]

        if not tipo_parte_prenda_ids:
            raise ValueError("No se encontraron tipos de parte de prenda en la tabla tipo_parte_prenda")

        for _ in range(100):
            id_tipo_parte_prenda = random.choice(tipo_parte_prenda_ids)

            cursor.execute("""
                INSERT INTO dimension_parte_prenda (id_tipo_parte_prenda)
                VALUES (%s) RETURNING id_dim_parte_prenda;
            """, (id_tipo_parte_prenda,))
            id_dim_parte_prenda = cursor.fetchone()[0]
            if id_dim_parte_prenda:
                print(f"Inserted dimension_parte_prenda: {id_dim_parte_prenda}, id_tipo_parte_prenda: {id_tipo_parte_prenda}")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar dimensiones de parte de prenda: {e}")

def insert_dimension_confeccion(cursor): #Inserta dimensiones de materia prima
    try:
        # Obtener todos los id_tipo_prenda
        cursor.execute("SELECT id_tipo_prenda FROM tipo_prenda;")
        tipos_prenda = cursor.fetchall()
        tipo_prenda_ids = [tipo[0] for tipo in tipos_prenda]

        # Obtener todos los id_estilo_prenda
        cursor.execute("SELECT id_estilo_prenda FROM estilo_prenda;")
        estilos_prenda = cursor.fetchall()
        estilo_prenda_ids = [estilo[0] for estilo in estilos_prenda]

        # Obtener todos los id_talla
        cursor.execute("SELECT id_talla FROM talla;")
        tallas = cursor.fetchall()
        talla_ids = [talla[0] for talla in tallas]

        # Obtener todos los id_genero
        cursor.execute("SELECT id_genero FROM genero;")
        generos = cursor.fetchall()
        genero_ids = [genero[0] for genero in generos]

        # Verificación de listas
        if not tipo_prenda_ids:
            raise ValueError("No se encontraron tipos de prenda en la tabla tipo_prenda")
        if not estilo_prenda_ids:
            raise ValueError("No se encontraron estilos de prenda en la tabla estilo_prenda")
        if not talla_ids:
            raise ValueError("No se encontraron tallas en la tabla talla")
        if not genero_ids:
            raise ValueError("No se encontraron géneros en la tabla genero")

        for _ in range(100):
            id_tipo_prenda = random.choice(tipo_prenda_ids)
            id_estilo_prenda = random.choice(estilo_prenda_ids)
            id_talla = random.choice(talla_ids)
            id_genero = random.choice(genero_ids)

            # Generar y insertar guía de confección
            medida_pecho = round(random.uniform(70, 90), 2)
            medida_cintura = round(random.uniform(60, 90), 2)
            medida_cadera = round(random.uniform(80, 90), 2)
            medida_hombro = round(random.uniform(35, 60), 2)
            medida_longitud = round(random.uniform(50, 90), 2)
            medida_manga = round(random.uniform(50, 80), 2)
            medida_muslo = round(random.uniform(40, 70), 2)

            cursor.execute("""
                INSERT INTO guia_confeccion (medida_pecho, medida_cintura, medida_cadera, medida_hombro, medida_longitud, medida_manga, medida_muslo)
                VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_guia_confeccion;
            """, (medida_pecho, medida_cintura, medida_cadera, medida_hombro, medida_longitud, medida_manga, medida_muslo))
            id_guia_confeccion = cursor.fetchone()[0]

            # Insertar dimensión de confección
            cursor.execute("""
                INSERT INTO dimension_confeccion (id_tipo_prenda, id_estilo_prenda, id_guia_confeccion, id_talla, id_genero)
                VALUES (%s, %s, %s, %s, %s) RETURNING id_dim_confeccion;
            """, (id_tipo_prenda, id_estilo_prenda, id_guia_confeccion, id_talla, id_genero))
            id_dim_confeccion = cursor.fetchone()[0]
            if id_dim_confeccion:
                print(f"Inserted dimension_confeccion: {id_dim_confeccion}, id_tipo_prenda: {id_tipo_prenda}, id_estilo_prenda: {id_estilo_prenda}, id_guia_confeccion: {id_guia_confeccion}, id_talla: {id_talla}, id_genero: {id_genero}")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar dimensiones de confección: {e}")

def insert_orden_pedido(cursor): #Inserta órdenes de pedido    
    try:
        orden_pedido_estado_relations = {
            'Orden_pedido': ('No iniciado', 'En proceso', 'Completado', 'Atrasado', 'Cancelado'),
        }
        # Obtener todos los id_estado relacionados con 'Orden_pedido'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(orden_pedido_estado_relations['Orden_pedido']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        if not estado_ids:
            raise ValueError("No se encontraron estados en la tabla estado")

        for _ in range(100):
            id_estado = random.choice(estado_ids)
            cantidad = random.randint(5, 9) * 10000
            fecha_creacion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            
            # Seleccionar un huso horario aleatorio
            tz = random.choice(pytz.all_timezones)
            timezone = pytz.timezone(tz)
            fecha_entrega = fake.date_time_between_dates(datetime_start=fecha_creacion, datetime_end=fecha_creacion + timedelta(days=90), tzinfo=timezone)


            cursor.execute("""
                INSERT INTO orden_pedido (fecha_entrega, cantidad, id_estado, fecha_creacion)
                VALUES (%s, %s, %s, %s) RETURNING id_orden_pedido;
            """, (fecha_entrega, cantidad, id_estado, fecha_creacion))
            id_orden_pedido = cursor.fetchone()
            if id_orden_pedido:
                print(f"Inserted orden_pedido: {id_orden_pedido}, cantidad: {cantidad}, id_estado: {id_estado}, fecha_creacion: {fecha_creacion}, fecha_entrega: {fecha_entrega}")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar órdenes de pedido: {e}")

def insert_plan_produccion(cursor): # Inserta órdenes de pedido
    try:
        plan_produccion_estado_relations = {
            'Plan_produccion': ('No iniciado', 'En proceso', 'Completado', 'Atrasado', 'Cancelado'),
        }

        # Obtener todos los id_estado relacionados con 'Orden_pedido'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(plan_produccion_estado_relations['Plan_produccion']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        if not estado_ids:
            raise ValueError("No se encontraron estados en la tabla estado")

        for _ in range(100):
            id_estado = random.choice(estado_ids)
            
            fecha_creacion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            fecha_inicio = fake.date_time_between_dates(datetime_start=fecha_creacion, datetime_end=fecha_creacion + timedelta(days=10), tzinfo=None)
            fecha_fin = fake.date_time_between_dates(datetime_start=fecha_inicio, datetime_end=fecha_inicio + timedelta(days=30), tzinfo=None)

            cursor.execute("""
                INSERT INTO plan_produccion (fecha_inicio, fecha_fin, id_estado, fecha_creacion)
                VALUES (%s, %s, %s, %s) RETURNING id_plan;
            """, (fecha_inicio, fecha_fin, id_estado, fecha_creacion))
            id_plan = cursor.fetchone()
            if id_plan:
                print(f"Inserted orden_pedido: {id_plan}, id_estado: {id_estado}, fecha_creacion: {fecha_creacion}, fecha_inicio: {fecha_inicio}, fecha_fin: {fecha_fin}")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar órdenes de producción: {e}")

def insert_zonas(cursor): # Inserta zonas
    try:
        area_zona_relations = {
            'Almacén Central': ('Materia prima', 'Corte', 'Confección', 'Producto terminado'),
            'Almacén de tránsito': ('Tránsito',),
        }

        for area, zona_list in area_zona_relations.items():
            # Obtener el id_area correspondiente
            cursor.execute("SELECT id_area FROM area WHERE nombre=%s;", (area,))
            id_area = cursor.fetchone()

            if not id_area:
                raise ValueError(f"No se encontró el área '{area}' en la tabla area")

            id_area = id_area[0]

            # Obtener el último número de zona para este id_area
            cursor.execute("SELECT MAX(id_zona) FROM zona WHERE id_zona BETWEEN %s AND %s;", (id_area * 100 + 1, id_area * 100 + 99))
            
            last_zone_number = cursor.fetchone()[0]

            if last_zone_number is None:
                last_zone_number = id_area * 100

            for zona in zona_list:
                # Incrementar el número de zona
                next_zone_number = last_zone_number + 1
                last_zone_number = next_zone_number  # Update the last zone number for the next iteration

                cursor.execute("INSERT INTO zona (id_zona, nombre, id_area) VALUES (%s, %s, %s) ON CONFLICT (nombre) DO NOTHING RETURNING id_zona;", (next_zone_number, zona, id_area))
                inserted_id_zona = cursor.fetchone()
                if inserted_id_zona:
                    print(f"Inserted zona: {zona}, id_zona: {next_zone_number}, id_area: {id_area}")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar zonas: {e}")

def insert_aql_muestra(cursor): #Inserta AQL muestra
    try:
        aql_muestra_relations = {
            'G1': {(2, 8): 'A', (9, 15): 'A', (16, 25): 'B', (26, 50): 'C', (51, 90): 'C', (91, 150): 'D', (151, 280): 'E', (281, 500): 'F', (501, 1200): 'G', (1201, 3200): 'H', (3201, 10000): 'J', (10001, 35000): 'K', (35001, 150000): 'L', (150001, 500000): 'M', (500001, 1000000): 'N'},
            'G2': {(2, 8): 'A', (9, 15): 'B', (16, 25): 'C', (26, 50): 'D', (51, 90): 'E', (91, 150): 'F', (151, 280): 'G', (281, 500): 'H', (501, 1200): 'J', (1201, 3200): 'K', (3201, 10000): 'L', (10001, 35000): 'M', (35001, 150000): 'N', (150001, 500000): 'P', (500001, 1000000): 'Q'},
            'G3': {(2, 8): 'B', (9, 15): 'C', (16, 25): 'D', (26, 50): 'E', (51, 90): 'F', (91, 150): 'G', (151, 280): 'H', (281, 500): 'J', (501, 1200): 'K', (1201, 3200): 'L', (3201, 10000): 'M', (10001, 35000): 'N', (35001, 150000): 'P', (150001, 500000): 'Q', (500001, 1000000): 'R'},
            'S1': {(2, 8): 'A', (9, 15): 'A', (16, 25): 'A', (26, 50): 'A', (51, 90): 'B', (91, 150): 'B', (151, 280): 'B', (281, 500): 'B', (501, 1200): 'C', (1201, 3200): 'C', (3201, 10000): 'C', (10001, 35000): 'C', (35001, 150000): 'D', (150001, 500000): 'D', (500001, 1000000): 'D'},
            'S2': {(2, 8): 'A', (9, 15): 'A', (16, 25): 'A', (26, 50): 'B', (51, 90): 'B', (91, 150): 'B', (151, 280): 'C', (281, 500): 'C', (501, 1200): 'C', (1201, 3200): 'D', (3201, 10000): 'D', (10001, 35000): 'D', (35001, 150000): 'E', (150001, 500000): 'E', (500001, 1000000): 'E'},
            'S3': {(2, 8): 'A', (9, 15): 'A', (16, 25): 'B', (26, 50): 'B', (51, 90): 'C', (91, 150): 'C', (151, 280): 'D', (281, 500): 'D', (501, 1200): 'E', (1201, 3200): 'E', (3201, 10000): 'F', (10001, 35000): 'F', (35001, 150000): 'G', (150001, 500000): 'G', (500001, 1000000): 'H'},
            'S4': {(2, 8): 'A', (9, 15): 'A', (16, 25): 'B', (26, 50): 'C', (51, 90): 'C', (91, 150): 'D', (151, 280): 'E', (281, 500): 'E', (501, 1200): 'F', (1201, 3200): 'G', (3201, 10000): 'G', (10001, 35000): 'H', (35001, 150000): 'J', (150001, 500000): 'J', (500001, 1000000): 'K'}
        }

        # Obtener todos los id_aql_nivel
        cursor.execute("SELECT id_aql_nivel, nombre FROM aql_nivel;")
        niveles = cursor.fetchall()
        nivel_dict = {nivel[1]: nivel[0] for nivel in niveles}

        # Obtener todos los id_aql_lote_rango
        cursor.execute("SELECT id_aql_lote_rango, min_lote, max_lote FROM aql_lote_rango;")
        lote_rangos = cursor.fetchall()
        lote_rango_dict = {(lote[1], lote[2]): lote[0] for lote in lote_rangos}

        # Obtener todos los id_aql_codigo
        cursor.execute("SELECT id_aql_codigo FROM aql_codigo;")
        codigos = cursor.fetchall()
        codigo_dict = {codigo[0]: codigo[0] for codigo in codigos}

        for nivel, rangos_codigos in aql_muestra_relations.items():
            id_aql_nivel = nivel_dict.get(nivel)
            if not id_aql_nivel:
                raise ValueError(f"No se encontró el nivel '{nivel}' en la tabla aql_nivel")

            for lote_rango, codigo in rangos_codigos.items():
                id_aql_lote_rango = lote_rango_dict.get(lote_rango)
                id_aql_codigo = codigo_dict.get(codigo)
                if not id_aql_lote_rango:
                    raise ValueError(f"No se encontró el rango de lote '{lote_rango}' en la tabla aql_lote_rango")
                if not id_aql_codigo:
                    raise ValueError(f"No se encontró el código '{codigo}' en la tabla aql_codigo")

                cursor.execute("""
                    INSERT INTO aql_muestra (id_aql_nivel, id_aql_lote_rango, id_aql_codigo)
                    VALUES (%s, %s, %s) ON CONFLICT DO NOTHING RETURNING id_aql_nivel, id_aql_lote_rango;
                """, (id_aql_nivel, id_aql_lote_rango, id_aql_codigo))
                inserted_ids = cursor.fetchone()
                if inserted_ids:
                    print(f"Inserted aql_muestra: nivel {id_aql_nivel}, lote_rango {id_aql_lote_rango}, codigo {id_aql_codigo}")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar aql_muestra: {e}")

def insert_aql_resultado_rango(cursor): #Inserta AQL resultado rango
    try:
        # Relaciones de aql_resultado_rango
        aql_resultado_rango_relations = {
            0.065: {'A': (0, 1), 'B': (0, 1), 'C': (0, 1), 'D': (0, 1), 'E': (0, 1), 'F': (0, 1), 'G': (0, 1), 'H': (0, 1), 'J': (0, 1), 'K': (0, 1), 'L': (0, 1), 'M': (0, 1), 'N': (1, 2), 'P': (1, 2), 'Q': (2, 3), 'R': (3, 4)},
            0.10: {'A': (0, 1), 'B': (0, 1), 'C': (0, 1), 'D': (0, 1), 'E': (0, 1), 'F': (0, 1), 'G': (0, 1), 'H': (0, 1), 'J': (0, 1), 'K': (0, 1), 'L': (0, 1), 'M': (1, 2), 'N': (1, 2), 'P': (2, 3), 'Q': (3, 4), 'R': (5, 6)},
            0.15: {'A': (0, 1), 'B': (0, 1), 'C': (0, 1), 'D': (0, 1), 'E': (0, 1), 'F': (0, 1), 'G': (0, 1), 'H': (0, 1), 'J': (0, 1), 'K': (0, 1), 'L': (1, 2), 'M': (1, 2), 'N': (2, 3), 'P': (3, 4), 'Q': (5, 6), 'R': (7, 8)},
            0.25: {'A': (0, 1), 'B': (0, 1), 'C': (0, 1), 'D': (0, 1), 'E': (0, 1), 'F': (0, 1), 'G': (0, 1), 'H': (0, 1), 'J': (0, 1), 'K': (1, 2), 'L': (1, 2), 'M': (2, 3), 'N': (3, 4), 'P': (5, 6), 'Q': (7, 8), 'R': (10, 11)},
            0.40: {'A': (0, 1), 'B': (0, 1), 'C': (0, 1), 'D': (0, 1), 'E': (0, 1), 'F': (0, 1), 'G': (0, 1), 'H': (0, 1), 'J': (1, 2), 'K': (1, 2), 'L': (2, 3), 'M': (3, 4), 'N': (5, 6), 'P': (7, 8), 'Q': (10, 11), 'R': (14, 15)},
            0.65: {'A': (0, 1), 'B': (0, 1), 'C': (0, 1), 'D': (0, 1), 'E': (0, 1), 'F': (0, 1), 'G': (0, 1), 'H': (1, 2), 'J': (1, 2), 'K': (2, 3), 'L': (3, 4), 'M': (5, 6), 'N': (7, 8), 'P': (10, 11), 'Q': (14, 15), 'R': (21, 22)},
            1.0: {'A': (0, 1), 'B': (0, 1), 'C': (0, 1), 'D': (0, 1), 'E': (0, 1), 'F': (0, 1), 'G': (1, 2), 'H': (1, 2), 'J': (2, 3), 'K': (3, 4), 'L': (5, 6), 'M': (7, 8), 'N': (10, 11), 'P': (14, 15), 'Q': (21, 22), 'R': (21, 22)},
            1.5: {'A': (0, 1), 'B': (0, 1), 'C': (0, 1), 'D': (0, 1), 'E': (0, 1), 'F': (1, 2), 'G': (1, 2), 'H': (2, 3), 'J': (3, 4), 'K': (5, 6), 'L': (7, 8), 'M': (10, 11), 'N': (14, 5), 'P': (21, 22), 'Q': (21, 22), 'R': (21, 22)},
            2.5: {'A': (0, 1), 'B': (0, 1), 'C': (0, 1), 'D': (0, 1), 'E': (1, 2), 'F': (1, 2), 'G': (2, 3), 'H': (3, 4), 'J': (5, 6), 'K': (7, 8), 'L': (10, 11), 'M': (14, 15), 'N': (21, 22), 'P': (21, 22), 'Q': (21, 22), 'R': (21, 22)},
            4.0: {'A': (0, 1), 'B': (0, 1), 'C': (0, 1), 'D': (1, 2), 'E': (1, 2), 'F': (2, 3), 'G': (3, 4), 'H': (5, 6), 'J': (7, 8), 'K': (10, 11), 'L': (14, 15), 'M': (21, 22), 'N': (21, 22), 'P': (21, 22), 'Q': (21, 22), 'R': (21, 22)},
            6.5: {'A': (0, 1), 'B': (0, 1), 'C': (1, 2), 'D': (1, 2), 'E': (3, 4), 'F': (5, 6), 'G': (7, 8), 'H': (10, 11), 'J': (14, 15), 'K': (21, 22), 'L': (21, 22), 'M': (21, 22), 'N': (21, 22), 'P': (21, 22), 'Q': (21, 22), 'R': (21, 22)}
        }
    
        # Obtener todos los códigos AQL
        cursor.execute("SELECT id_aql_codigo, tamaño_muestra FROM aql_codigo;")
        codigos = cursor.fetchall()
        codigo_dict = {codigo[1]: codigo[0] for codigo in codigos}

        # Obtener todos los niveles de significancia AQL
        cursor.execute("SELECT id_aql_significancia, nivel_significancia FROM aql_significancia;")
        significancias = cursor.fetchall()
        significancia_dict = {significancia[1]: significancia[0] for significancia in significancias}

        for nivel_significancia, rango_codigos in aql_resultado_rango_relations.items():
            id_aql_significancia = significancia_dict.get(nivel_significancia)
            if not id_aql_significancia:
                raise ValueError(f"No se encontró la significancia '{nivel_significancia}' en la tabla aql_significancia")

            for codigo, rango in rango_codigos.items():
                id_aql_codigo = codigo_dict.get(codigo)
                if not id_aql_codigo:
                    raise ValueError(f"No se encontró el código AQL '{codigo}' en la tabla aql_codigo")

                min_rechazo, max_aceptacion = rango
                cursor.execute("""
                    INSERT INTO aql_resultado_rango (id_aql_codigo, id_aql_significancia, max_aceptacion, min_rechazo)
                    VALUES (%s, %s, %s, %s);
                """, (id_aql_codigo, id_aql_significancia, max_aceptacion, min_rechazo))

    except (psycopg2.Error, ValueError) as e:
        print(f"Error al insertar en la tabla aql_resultado_rango: {e}")

def insert_dimension_corte(cursor): #Inserta dimensiones de corte
    try:
        # Obtener todos los id_dim_materia_prima
        cursor.execute("SELECT id_dim_materia_prima FROM dimension_materia_prima;")
        dimensiones_materia_prima = cursor.fetchall()
        dim_materia_prima_ids = [dim[0] for dim in dimensiones_materia_prima]

        # Obtener todos los id_dim_parte_prenda
        cursor.execute("SELECT id_dim_parte_prenda FROM dimension_parte_prenda;")
        dimensiones_parte_prenda = cursor.fetchall()
        dim_parte_prenda_ids = [dim[0] for dim in dimensiones_parte_prenda]

        if not dim_materia_prima_ids:
            raise ValueError("No se encontraron dimensiones de materia prima en la tabla dimension_materia_prima")
        if not dim_parte_prenda_ids:
            raise ValueError("No se encontraron dimensiones de parte de prenda en la tabla dimension_parte_prenda")

        for _ in range(100):
            id_dim_materia_prima = random.choice(dim_materia_prima_ids)
            id_dim_parte_prenda = random.choice(dim_parte_prenda_ids)

            cursor.execute("""
                INSERT INTO dimension_corte (id_dim_materia_prima, id_dim_parte_prenda)
                VALUES (%s, %s);
            """, (id_dim_materia_prima, id_dim_parte_prenda))

    except (psycopg2.Error, ValueError) as e:
        print(f"Error al insertar en la tabla dimension_corte: {e}")

def insert_parte_corte_detalle(cursor): #Inserta parte de corte detalle
    try:
        # Obtener todos los id_dim_parte_prenda
        cursor.execute("SELECT id_dim_parte_prenda FROM dimension_parte_prenda;")
        dimensiones_parte_prenda = cursor.fetchall()
        dim_parte_prenda_ids = [dim[0] for dim in dimensiones_parte_prenda]

        # Obtener todos los id_tipo_corte
        cursor.execute("SELECT id_tipo_corte FROM tipo_corte;")
        tipos_corte = cursor.fetchall()
        tipo_corte_ids = [tipo[0] for tipo in tipos_corte]

        if not dim_parte_prenda_ids:
            raise ValueError("No se encontraron dimensiones de parte de prenda en la tabla dimension_parte_prenda")
        if not tipo_corte_ids:
            raise ValueError("No se encontraron tipos de corte en la tabla tipo_corte")

        for _ in range(100):
            id_dim_parte_prenda = random.choice(dim_parte_prenda_ids)
            id_tipo_corte = random.choice(tipo_corte_ids)
            medida = round(random.uniform(0.5, 10), 2)

            cursor.execute("""
                INSERT INTO parte_corte_detalle (id_dim_parte_prenda, id_tipo_corte, medida)
                VALUES (%s, %s, %s);
            """, (id_dim_parte_prenda, id_tipo_corte, medida))

    except (psycopg2.Error, ValueError) as e:
        print(f"Error al insertar en la tabla parte_corte_detalle: {e}")

def insert_dimension_prenda(cursor): #Inserta dimensiones de prenda
    try:
        # Obtener todos los id_dim_confeccion
        cursor.execute("SELECT id_dim_confeccion FROM dimension_confeccion;")
        dimensiones_confeccion = cursor.fetchall()
        dim_confeccion_ids = [dim[0] for dim in dimensiones_confeccion]

        if not dim_confeccion_ids:
            raise ValueError("No se encontraron dimensiones de confección en la tabla dimension_confeccion")

        for _ in range(100):
            id_dim_confeccion = random.choice(dim_confeccion_ids)

            cursor.execute("""
                INSERT INTO dimension_prenda (id_dim_confeccion)
                VALUES (%s);
            """, (id_dim_confeccion,))

    except (psycopg2.Error, ValueError) as e:
        print(f"Error al insertar en la tabla dimension_prenda: {e}")

def insert_orden_trabajo(cursor):
    try:
        entidad_estado_relations = {
            'Orden_trabajo': ('No iniciado', 'En proceso', 'Completado', 'Atrasado', 'Cancelado'),
        }

        # Obtener todos los id_estado relacionados con 'Orden_pedido'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(entidad_estado_relations['Orden_trabajo']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        # Obtener todos los id_plan
        cursor.execute("SELECT id_plan FROM plan_produccion;")
        planes = cursor.fetchall()
        plan_ids = [plan[0] for plan in planes]

        # Obtener todos los id_orden_pedido
        cursor.execute("SELECT id_orden_pedido FROM orden_pedido;")
        ordenes_pedido = cursor.fetchall()
        orden_pedido_ids = [orden_pedido[0] for orden_pedido in ordenes_pedido]

        if not estado_ids:
            raise ValueError("No se encontraron estados en la tabla estado")
        if not plan_ids:
            raise ValueError("No se encontraron planes de producción en la tabla plan_produccion")
        if not orden_pedido_ids:
            raise ValueError("No se encontraron órdenes de pedido en la tabla orden_pedido")
     
        for _ in range(100):
            fecha_creacion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            fecha_inicio = fake.date_time_between_dates(datetime_start=fecha_creacion, datetime_end=fecha_creacion + timedelta(days=5), tzinfo=None)
            fecha_fin = fake.date_time_between_dates(datetime_start=fecha_inicio, datetime_end=fecha_inicio + timedelta(days=10), tzinfo=None)
            prioridad = random.randint(1, 5)
            id_plan = random.choice(plan_ids)
            id_orden_pedido = random.choice(orden_pedido_ids)
            id_estado = random.choice(estado_ids)  # Escoger un estado aleatorio

            cursor.execute("""
                INSERT INTO orden_trabajo (fecha_inicio, fecha_fin, prioridad, id_estado, id_plan, id_orden_pedido, fecha_creacion)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """, (fecha_inicio, fecha_fin, prioridad, id_estado, id_plan, id_orden_pedido, fecha_creacion))

    except (psycopg2.Error, ValueError) as e:
        print(f"Error al insertar en la tabla orden_trabajo: {e}")

def insert_pasillo(cursor): # Inserta pasillos
    try:
        cursor.execute("SELECT id_pasillo FROM pasillo;")
        pasillos = cursor.fetchall()

        for pasillo in pasillos:
            pasillo_id = pasillo[0]
            for _ in range(5):
                ancho_estanteria = round(random.uniform(0.5, 2.0), 2)
                largo_estanteria = round(random.uniform(0.5, 2.0), 2)

                cursor.execute("SELECT COALESCE(MAX(CAST(SUBSTRING(id_estanteria, 4) AS INTEGER)), 0) FROM estanteria WHERE id_pasillo = %s;", (pasillo_id,))
                last_shelf_number = cursor.fetchone()[0]

                next_shelf_number = last_shelf_number + 1
                id_estanteria = f"{pasillo_id}{next_shelf_number:02d}"

                cursor.execute("INSERT INTO estanteria (id_estanteria, ancho_estanteria, largo_estanteria, id_pasillo) VALUES (%s, %s, %s, %s, %s) RETURNING id_estanteria;", (id_estanteria, ancho_estanteria, largo_estanteria, pasillo_id))
                inserted_id_estanteria = cursor.fetchone()
                if inserted_id_estanteria:
                    print(f"Inserted estanteria: {id_estanteria}, id_pasillo: {pasillo_id}")

    except (psycopg2.Error, ValueError) as e:
        print(f"Error al insertar estanterias: {e}")

def insert_dim_confeccion_detalle(cursor): # Inserta dim_confeccion_detalle
    try:
        # Obtener todos los id_dim_confeccion de la tabla dimension_confeccion
        cursor.execute("SELECT id_dim_confeccion FROM dimension_confeccion;")
        dim_confeccion_ids = cursor.fetchall()
        dim_confeccion_ids = [dim[0] for dim in dim_confeccion_ids]

        # Obtener todos los id_dim_corte de la tabla dimension_corte
        cursor.execute("SELECT id_dim_corte FROM dimension_corte;")
        dim_corte_ids = cursor.fetchall()
        dim_corte_ids = [dim[0] for dim in dim_corte_ids]

        if not dim_confeccion_ids or not dim_corte_ids:
            raise ValueError("No se encontraron registros en una o ambas tablas relacionadas")

        for _ in range(100):
            id_dim_confeccion = random.choice(dim_confeccion_ids)
            id_dim_corte = random.choice(dim_corte_ids)

            cursor.execute("""
                INSERT INTO dim_confeccion_detalle (id_dim_confeccion, id_dim_corte)
                VALUES (%s, %s) ON CONFLICT DO NOTHING;
            """, (id_dim_confeccion, id_dim_corte))

            print(f"Inserted dim_confeccion_detalle: id_dim_confeccion = {id_dim_confeccion}, id_dim_corte = {id_dim_corte}")

    except (psycopg2.Error, ValueError) as e:
        print(f"Error al insertar en la tabla dim_confeccion_detalle: {e}")

def insert_dim_prenda_detalle(cursor): # Inserta dim_prenda_detalle
    try:
        # Obtener todos los id_dim_prenda de la tabla dimension_prenda
        cursor.execute("SELECT id_dim_prenda FROM dimension_prenda;")
        dim_prenda_ids = cursor.fetchall()
        dim_prenda_ids = [dim[0] for dim in dim_prenda_ids]

        # Obtener todos los id_acabado de la tabla acabado
        cursor.execute("SELECT id_acabado FROM acabado;")
        acabado_ids = cursor.fetchall()
        acabado_ids = [acabado[0] for acabado in acabado_ids]

        if not dim_prenda_ids or not acabado_ids:
            raise ValueError("No se encontraron registros en una o ambas tablas relacionadas")

        for _ in range(100):
            id_dim_prenda = random.choice(dim_prenda_ids)
            id_acabado = random.choice(acabado_ids)

            cursor.execute("""
                INSERT INTO dim_prenda_detalle (id_dim_prenda, id_acabado)
                VALUES (%s, %s) ON CONFLICT DO NOTHING;
            """, (id_dim_prenda, id_acabado))

            print(f"Inserted dim_prenda_detalle: id_dim_prenda = {id_dim_prenda}, id_acabado = {id_acabado}")

    except (psycopg2.Error, ValueError) as e:
        print(f"Error al insertar en la tabla dim_prenda_detalle: {e}")

def insert_pedido_detalle(cursor): # Inserta pedido_detalle
    try:
        # Obtener todos los id_orden_pedido de la tabla orden_pedido
        cursor.execute("SELECT id_orden_pedido FROM orden_pedido;")
        orden_pedido_ids = cursor.fetchall()
        orden_pedido_ids = [pedido[0] for pedido in orden_pedido_ids]

        # Obtener todos los id_dim_prenda de la tabla dimension_prenda
        cursor.execute("SELECT id_dim_prenda FROM dimension_prenda;")
        dim_prenda_ids = cursor.fetchall()
        dim_prenda_ids = [dim[0] for dim in dim_prenda_ids]

        if not orden_pedido_ids or not dim_prenda_ids:
            raise ValueError("No se encontraron registros en una o ambas tablas relacionadas")

        for _ in range(100):
            id_orden_pedido = random.choice(orden_pedido_ids)
            id_dim_prenda = random.choice(dim_prenda_ids)

            cursor.execute("""
                INSERT INTO pedido_detalle (id_orden_pedido, id_dim_prenda)
                VALUES (%s, %s) ON CONFLICT DO NOTHING;
            """, (id_orden_pedido, id_dim_prenda))

            print(f"Inserted pedido_detalle: id_orden_pedido = {id_orden_pedido}, id_dim_prenda = {id_dim_prenda}")

    except (psycopg2.Error, ValueError) as e:
        print(f"Error al insertar en la tabla pedido_detalle: {e}")

def insert_estanterias(cursor): # Inserta estanterias
    try:
        # Obtener los identificadores de los pasillos
        cursor.execute("SELECT id_pasillo FROM pasillo;")
        pasillos = cursor.fetchall()

        for pasillo in pasillos:
            pasillo_id = pasillo[0]
            for _ in range(5):  # Insertar 5 estanterías por pasillo
                # Generar dimensiones aleatorias para la estantería
                ancho = round(random.uniform(0.5, 2.0), 2)
                largo = round(random.uniform(0.5, 2.0), 2)
                alto = round(random.uniform(1.0, 2.5), 2)

                # Generar el ID de la estantería (usando un contador para cada pasillo)
                cursor.execute("SELECT MAX(CAST(SUBSTRING(id_estanteria, 6) AS INTEGER)) FROM estanteria WHERE id_pasillo = %s;", (pasillo_id,))
                last_shelf_number = cursor.fetchone()[0]

                if last_shelf_number is None:
                    last_shelf_number = 0

                next_shelf_number = last_shelf_number + 1
                id_estanteria = f"{pasillo_id}{next_shelf_number:02d}"

                # Insertar la estantería en la base de datos
                cursor.execute("INSERT INTO estanteria (id_estanteria, ancho_estanteria, largo_estanteria, alto_estanteria, id_pasillo) VALUES (%s, %s, %s, %s, %s) RETURNING id_estanteria;", (id_estanteria, ancho, largo, alto, pasillo_id))
                inserted_id_estanteria = cursor.fetchone()
                if inserted_id_estanteria:
                    print(f"Inserted estanteria: {id_estanteria}, id_pasillo: {pasillo_id}")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar estanterias: {e}")

def insert_ordenes_produccion(cursor): # Inserta órdenes de producción
    orden_produccion_estado_relations = {
        'Orden_produccion': ('No iniciado', 'En proceso', 'Completado', 'Atrasado', 'Cancelado'),
    }
    
    try:
        # Obtener los identificadores de áreas
        cursor.execute("SELECT id_area FROM area;")
        areas = cursor.fetchall()

        # Obtener todos los id_estado relacionados con 'orden_produccion'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(orden_produccion_estado_relations['Orden_produccion']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        # Obtener los identificadores de las órdenes de trabajo
        cursor.execute("SELECT id_orden_trabajo FROM orden_trabajo;")
        ordenes_trabajo = cursor.fetchall()

        for _ in range(150):  # Insertar 100 órdenes de producción
            fecha_creacion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            fecha_inicio = fake.date_time_between_dates(datetime_start=fecha_creacion, datetime_end=fecha_creacion + timedelta(days=5), tzinfo=None)
            fecha_fin = fake.date_time_between_dates(datetime_start=fecha_inicio, datetime_end=fecha_inicio + timedelta(days=20), tzinfo=None)

            cantidad = random.randint(10, 1000)

            # Seleccionar un área aleatoria
            id_area = random.choice(areas)

            # Seleccionar un estado aleatorio
            id_estado = random.choice(estado_ids)

            # Seleccionar una orden de trabajo aleatoria
            id_orden_trabajo = random.choice(ordenes_trabajo)

            # Determinar qué dimensiones se van a llenar
            dim_a_llenar = random.choice(['id_dim_prenda', 'id_dim_confeccion', 'id_dim_corte'])

           # Obtener el identificador de la dimensión respectiva
            if dim_a_llenar == 'id_dim_prenda':
                cursor.execute("SELECT id_dim_prenda FROM dimension_prenda;")
            elif dim_a_llenar == 'id_dim_confeccion':
                cursor.execute("SELECT id_dim_confeccion FROM dimension_confeccion;")
            else:
                cursor.execute("SELECT id_dim_corte FROM dimension_corte;")

            dim_id = random.choice(cursor.fetchall())[0]

            # Insertar la orden de producción
            cursor.execute("""
                INSERT INTO orden_producción (fecha_inicio, fecha_fin, cantidad, id_estado, id_area, {}, id_orden_trabajo, fecha_creacion)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """.format(dim_a_llenar), (fecha_inicio, fecha_fin, cantidad, id_estado, id_area, dim_id, id_orden_trabajo, fecha_creacion))

            print("Inserted orden de producción")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar órdenes de producción: {e}")

def insert_actividades_diarias(cursor): # Inserta actividades diarias
    try:
        # Obtener los identificadores de las órdenes de producción
        cursor.execute("SELECT id_orden_producción FROM orden_producción;")
        ordenes_produccion = cursor.fetchall()

        for _ in range(300):  # Insertar 100 actividades diarias
            fecha_actividad = fake.date_between(start_date='-1y', end_date='today')

            # Seleccionar una orden de producción aleatoria
            id_orden_produccion = random.choice(ordenes_produccion)[0]

            # Insertar la actividad diaria
            cursor.execute("""
                INSERT INTO actividad_diaria (fecha_actividad, id_orden_producción)
                VALUES (%s, %s);
            """, (fecha_actividad, id_orden_produccion))

            print("Inserted actividad diaria")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar actividades diarias: {e}")

def insert_lotes(cursor):
    lote_estado_relations = {
        'Lote': ('Disponible', 'En proceso', 'Usado', 'Obsoleto'),
    }
    
    try:
        # Obtener todos los id_estado relacionados con 'lote'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(lote_estado_relations['Lote']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        # Obtener los identificadores de los tipos de lote
        cursor.execute("SELECT id_tipo_lote FROM tipo_lote;")
        tipos_lote = cursor.fetchall()

        # Obtener los identificadores de las actividades diarias ordenadas por fecha de actividad
        cursor.execute("SELECT id_actividad, fecha_actividad FROM actividad_diaria ORDER BY fecha_actividad;")
        actividades_diarias = cursor.fetchall()

        for i in range(len(actividades_diarias)):
            # Obtener los identificadores de las dimensiones de la orden de producción asociada
            cursor.execute("SELECT id_dim_corte, id_dim_confeccion, id_dim_prenda FROM orden_producción WHERE id_orden_producción = %s;", (i + 1,))
            dimensiones_orden_produccion = cursor.fetchone()
            dim_corte, dim_confeccion, dim_prenda = dimensiones_orden_produccion

            cantidad = random.randint(100, 1000)
            id_estado = random.choice(estado_ids)
            id_tipo_lote = random.choice(tipos_lote)[0]
            id_actividad = actividades_diarias[i][0]
            fecha_creacion = actividades_diarias[i][1]

            # Insertar el lote
            cursor.execute("""
                INSERT INTO lote (cantidad, id_estado, id_tipo_lote, id_dim_corte, id_dim_confeccion, id_dim_prenda, id_actividad, fecha_creacion)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """, (cantidad, id_estado, id_tipo_lote, dim_corte, dim_confeccion, dim_prenda, id_actividad, fecha_creacion))

            print("Inserted lote")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar lotes: {e}")

def insert_empleado_actividad(cursor):
    try:
        # Obtener los identificadores de las actividades diarias
        cursor.execute("SELECT id_actividad FROM actividad_diaria;")
        actividades = cursor.fetchall()
        actividades_ids = [actividad[0] for actividad in actividades]

        # Obtener los identificadores de los empleados
        cursor.execute("SELECT id_empleado FROM empleado;")
        empleados = cursor.fetchall()
        empleados_ids = [empleado[0] for empleado in empleados]

        for _ in range(100):
            id_actividad = random.choice(actividades_ids)
            id_empleado = random.choice(empleados_ids)
            cantidad_hecha = random.randint(10, 20)

            cursor.execute("""
                INSERT INTO empleado_actividad (id_actividad, id_empleado, cantidad_hecha)
                VALUES (%s, %s, %s);
            """, (id_actividad, id_empleado, cantidad_hecha))

            print("Inserted empleado_actividad")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar empleado_actividad: {e}")

def insert_maquina_actividad(cursor):
    try:
        # Obtener los identificadores de las actividades diarias
        cursor.execute("SELECT id_actividad FROM actividad_diaria;")
        actividades = cursor.fetchall()
        actividades_ids = [actividad[0] for actividad in actividades]

        # Obtener los identificadores de las máquinas
        cursor.execute("SELECT id_maquina FROM maquina;")
        maquinas = cursor.fetchall()
        maquinas_ids = [maquina[0] for maquina in maquinas]

        for _ in range(100):
            id_actividad = random.choice(actividades_ids)
            id_maquina = random.choice(maquinas_ids)
            cantidad_hecha = random.randint(1,5) * 100

            cursor.execute("""
                INSERT INTO maquina_actividad (id_actividad, id_maquina, cantidad_hecha)
                VALUES (%s, %s, %s);
            """, (id_actividad, id_maquina, cantidad_hecha))

            print("Inserted maquina_actividad")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar maquina_actividad: {e}")

def insert_caja_prenda(cursor):
    caja_prenda_estado_relations = {
        'Caja_prenda': ('En proceso', 'Entregado', 'Obsoleto'),
    }
    
    try:
        # Obtener todos los id_estado relacionados con 'orden_produccion'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(caja_prenda_estado_relations['Caja_prenda']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]
        
        # Obtener los identificadores de las dimensiones de prenda
        cursor.execute("SELECT id_dim_prenda FROM dimension_prenda;")
        dimensiones_prenda = cursor.fetchall()
        dimensiones_prenda_ids = [dim[0] for dim in dimensiones_prenda]

        # Obtener los identificadores de las actividades diarias
        cursor.execute("SELECT id_actividad FROM actividad_diaria;")
        actividades = cursor.fetchall()
        actividades_ids = [actividad[0] for actividad in actividades]

        for _ in range(200):
            cantidad = random.randint(2, 5) * 10
            fecha_creacion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            id_estado = random.choice(estado_ids)  # Supongamos que hay 3 estados
            id_dim_prenda = random.choice(dimensiones_prenda_ids)
            id_actividad = random.choice(actividades_ids)

            cursor.execute("""
                INSERT INTO caja_prenda (cantidad, fecha_creacion, id_estado, id_dim_prenda, id_actividad)
                VALUES (%s, %s, %s, %s, %s);
            """, (cantidad, fecha_creacion, id_estado, id_dim_prenda, id_actividad))

            print("Inserted caja_prenda")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar caja_prenda: {e}")

def insert_espacios(cursor): # Inserta espacios
    espacio_estado_relations = {
        'Espacio': ('Disponible', 'Ocupado', 'En mantenimiento'),
    }
    
    try:
        # Obtener los identificadores de las estanterías
        cursor.execute("SELECT id_estanteria FROM estanteria;")
        estanterias = cursor.fetchall()

        # Obtener todos los id_estado relacionados con 'espacio'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(espacio_estado_relations['Espacio']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        if not estado_ids:
            raise ValueError("No se encontraron estados en la tabla estado")

        for estanteria in estanterias:
            id_estanteria = estanteria[0]

            for _ in range(10):  # Insertar 10 espacios por estantería
                # Generar dimensiones aleatorias para el espacio
                ancho = round(random.uniform(0.5, 2.0), 2)
                largo = round(random.uniform(0.5, 2.0), 2)
                alto = round(random.uniform(1.0, 2.5), 2)

                # Generar el ID de la estantería (usando un contador para cada pasillo)
                cursor.execute("SELECT MAX(CAST(SUBSTRING(id_espacio, 8) AS INTEGER)) FROM espacio WHERE id_estanteria = %s;", (id_estanteria,))
                last_shelf_number = cursor.fetchone()[0]

                if last_shelf_number is None:
                    last_shelf_number = 0

                next_shelf_number = last_shelf_number + 1
                id_espacio = f"{id_estanteria}{next_shelf_number:02d}"

                # Seleccionar un estado aleatorio
                id_estado = random.choice(estado_ids)

                # Insertar el espacio en la base de datos
                cursor.execute("INSERT INTO espacio (id_espacio, ancho, largo, alto, estado, id_estanteria) VALUES (%s, %s, %s, %s, %s) RETURNING id_espacio;", (id_espacio, ancho, largo, alto, id_estado, id_estanteria))
                inserted_id_espacio = cursor.fetchone()[0]  # Se añade índice para obtener el valor directamente
                if inserted_id_espacio:
                    print(f"Inserted espacio: {inserted_id_espacio}, id_estanteria: {id_estanteria}")

    except (psycopg2.Error, ValueError) as e:
        messagebox.showerror("Error", f"Error al insertar espacios: {e}")

def insert_materia_prima(cursor):
    try:
        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        # Obtener los identificadores de las dimensiones de materia prima
        cursor.execute("SELECT id_dim_materia_prima FROM dimension_materia_prima;")
        dimensiones_materia_prima = cursor.fetchall()
        dimensiones_materia_prima_ids = [dim[0] for dim in dimensiones_materia_prima]

        # Obtener los identificadores de los proveedores
        cursor.execute("SELECT id_proveedor FROM proveedor;")
        proveedores = cursor.fetchall()
        proveedores_ids = [proveedor[0] for proveedor in proveedores]

        for _ in range(10000):
            id_lote = random.choice(lotes_ids)
            id_dim_materia_prima = random.choice(dimensiones_materia_prima_ids)
            id_proveedor = random.choice(proveedores_ids)

            cursor.execute("""
                INSERT INTO materia_prima (id_lote, id_dim_materia_prima, id_proveedor)
                VALUES (%s, %s, %s);
            """, (id_lote, id_dim_materia_prima, id_proveedor))

            print("Inserted materia_prima")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar materia_prima: {e}")

def insert_corte(cursor):
    try:
        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        # Obtener los identificadores de las dimensiones de corte
        cursor.execute("SELECT id_dim_corte FROM dimension_corte;")
        dimensiones_corte = cursor.fetchall()
        dimensiones_corte_ids = [dim[0] for dim in dimensiones_corte]

        # Obtener los identificadores de las máquinas de corte
        cursor.execute("SELECT id_maquina FROM maquina;")
        maquinas = cursor.fetchall()
        maquinas_ids = [maquina[0] for maquina in maquinas]

        for _ in range(10000):
            id_lote = random.choice(lotes_ids)
            id_dim_corte = random.choice(dimensiones_corte_ids)
            id_maquina = random.choice(maquinas_ids)

            cursor.execute("""
                INSERT INTO corte (id_lote, id_dim_corte, id_maquina)
                VALUES (%s, %s, %s);
            """, (id_lote, id_dim_corte, id_maquina))

            print("Inserted corte")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar corte: {e}")

def insert_registro_uso_lote(cursor):
    try:
        # Obtener los identificadores de las actividades diarias
        cursor.execute("SELECT id_actividad FROM actividad_diaria;")
        actividades = cursor.fetchall()
        actividades_ids = [actividad[0] for actividad in actividades]

        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        for _ in range(400):
            id_actividad = random.choice(actividades_ids)
            id_lote = random.choice(lotes_ids)
            cantidad_usada = random.randint(1, 100)

            cursor.execute("""
                INSERT INTO registro_uso_lote (id_actividad, id_lote, cantidad_usada)
                VALUES (%s, %s, %s);
            """, (id_actividad, id_lote, cantidad_usada))

            print("Inserted registro_uso_lote")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar registro_uso_lote: {e}")

def insert_caja_lote(cursor):
    caja_lote_estado_relations = {
        'Caja_lote': ('Disponible', 'Usado', 'Obsoleto'),
    }

    try:
        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        # Obtener todos los id_estado relacionados con 'orden_produccion'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(caja_lote_estado_relations['Caja_lote']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        for _ in range(200):
            cantidad = random.randint(1, 1000)
            id_lote = random.choice(lotes_ids)
            id_estado = random.choice(estado_ids)

            cursor.execute("""
                INSERT INTO caja_lote (cantidad, id_lote, id_estado)
                VALUES (%s, %s, %s);
            """, (cantidad, id_lote, id_estado))

            print("Inserted caja_lote")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar caja_lote: {e}")

def insert_prenda(cursor):
    try:
        # Obtener los identificadores de las dimensiones de prenda
        cursor.execute("SELECT id_dim_prenda FROM dimension_prenda;")
        dimensiones_prenda = cursor.fetchall()
        dimensiones_prenda_ids = [dim_prenda[0] for dim_prenda in dimensiones_prenda]

        # Obtener los identificadores de los empleados
        cursor.execute("SELECT id_empleado FROM empleado;")
        empleados = cursor.fetchall()
        empleados_ids = [empleado[0] for empleado in empleados]

        # Obtener los identificadores de las cajas de prenda
        cursor.execute("SELECT id_caja FROM caja_prenda;")
        cajas_prenda = cursor.fetchall()
        cajas_prenda_ids = [caja[0] for caja in cajas_prenda]

        for _ in range(10000):
            id_dim_prenda = random.choice(dimensiones_prenda_ids)
            id_empleado = random.choice(empleados_ids)
            id_caja = random.choice(cajas_prenda_ids)

            cursor.execute("""
                INSERT INTO prenda (id_dim_prenda, id_empleado, id_caja)
                VALUES (%s, %s, %s);
            """, (id_dim_prenda, id_empleado, id_caja))

            print("Inserted prenda")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar prenda: {e}")

def insert_lote_salida(cursor):
    try:
        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        # Obtener los identificadores de las áreas de envío
        cursor.execute("SELECT id_area FROM area;")
        areas = cursor.fetchall()
        areas_ids = [area[0] for area in areas]

        for _ in range(50):
            fecha_salida = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            id_lote = random.choice(lotes_ids)
            area_envio = random.choice(areas_ids)

            cursor.execute("""
                INSERT INTO lote_salida (fecha_salida, id_lote, area_envio)
                VALUES (%s, %s, %s);
            """, (fecha_salida, id_lote, area_envio))

            print("Inserted lote salida")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar lote salida: {e}")

def insert_inspeccion_calidad(cursor):
    try:
        # Obtener los identificadores de los estados
        cursor.execute("SELECT id_estado FROM estado;")
        estados = cursor.fetchall()
        estados_ids = [estado[0] for estado in estados]

        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        # Obtener los identificadores de los rangos de AQL
        cursor.execute("SELECT id_aql_lote_rango, id_aql_nivel FROM aql_muestra;")
        aql_muestras = cursor.fetchall()

        # Obtener los identificadores de los códigos de AQL
        cursor.execute("SELECT id_aql_codigo, id_aql_significancia FROM aql_resultado_rango;")
        aql_resultados = cursor.fetchall()

        # Obtener los identificadores de las descripciones de inspección
        cursor.execute("SELECT id_descripcion FROM inspeccion_descripcion;")
        descripciones = cursor.fetchall()
        descripciones_ids = [descripcion[0] for descripcion in descripciones]

        # Obtener los identificadores de los resultados
        cursor.execute("SELECT id_resultado FROM resultado;")
        resultados = cursor.fetchall()
        resultados_ids = [resultado[0] for resultado in resultados]

        for _ in range(200):
            fecha_inspeccion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            id_estado = random.choice(estados_ids)
            cantidad_defectuosos = random.randint(0, 10)
            id_lote = random.choice(lotes_ids)
            id_aql_lote_rango, id_aql_nivel = random.choice(aql_muestras)
            id_aql_codigo, id_aql_significancia = random.choice(aql_resultados)
            id_descripcion = random.choice(descripciones_ids)
            id_resultado = random.choice(resultados_ids)

            cursor.execute("""
                INSERT INTO inspeccion_calidad (fecha_inspeccion, id_estado, cantidad_defectuosos, id_lote, 
                                                id_aql_lote_rango, id_aql_nivel, id_aql_codigo, id_aql_significancia, 
                                                id_descripcion, id_resultado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (fecha_inspeccion, id_estado, cantidad_defectuosos, id_lote, id_aql_lote_rango, id_aql_nivel,
                  id_aql_codigo, id_aql_significancia, id_descripcion, id_resultado))

            print("Inserted inspeccion calidad")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar inspeccion calidad: {e}")

def insert_confeccion(cursor):
    try:
        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        # Obtener los identificadores de las dimensiones de confección
        cursor.execute("SELECT id_dim_confeccion FROM dimension_confeccion;")
        dimensiones_confeccion = cursor.fetchall()
        dimensiones_confeccion_ids = [dimension[0] for dimension in dimensiones_confeccion]

        # Obtener los identificadores de los empleados
        cursor.execute("SELECT id_empleado FROM empleado;")
        empleados = cursor.fetchall()
        empleados_ids = [empleado[0] for empleado in empleados]

        # Obtener los identificadores de las cajas de lote
        cursor.execute("SELECT id_caja FROM caja_lote;")
        cajas_lote = cursor.fetchall()
        cajas_lote_ids = [caja[0] for caja in cajas_lote]

        for _ in range(10000):
            id_lote = random.choice(lotes_ids)
            id_dim_confeccion = random.choice(dimensiones_confeccion_ids)
            id_empleado = random.choice(empleados_ids)
            id_caja = random.choice(cajas_lote_ids) if random.random() < 0.5 else None

            cursor.execute("""
                INSERT INTO confeccion (id_lote, id_dim_confeccion, id_empleado, id_caja)
                VALUES (%s, %s, %s, %s);
            """, (id_lote, id_dim_confeccion, id_empleado, id_caja))

            print("Inserted confeccion")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar confeccion: {e}")

def insert_registro_lote_caja(cursor):
    try:
        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        # Obtener los identificadores de las cajas de lote
        cursor.execute("SELECT id_caja FROM caja_lote;")
        cajas_lote = cursor.fetchall()
        cajas_lote_ids = [caja[0] for caja in cajas_lote]

        for _ in range(50):
            id_lote = random.choice(lotes_ids)
            id_caja = random.choice(cajas_lote_ids)
            fecha_transicion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)

            cursor.execute("""
                INSERT INTO registro_lote_caja (id_lote, id_caja, fecha_transicion)
                VALUES (%s, %s, %s);
            """, (id_lote, id_caja, fecha_transicion))

            print("Inserted registro_lote_caja")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar registro_lote_caja: {e}")

def insert_registro_transformacion_caja(cursor):
    try:
        # Obtener los identificadores de las actividades diarias
        cursor.execute("SELECT id_actividad FROM actividad_diaria;")
        actividades = cursor.fetchall()
        actividades_ids = [actividad[0] for actividad in actividades]

        # Obtener los identificadores de las cajas de lote
        cursor.execute("SELECT id_caja FROM caja_lote;")
        cajas_lote = cursor.fetchall()
        cajas_lote_ids = [caja[0] for caja in cajas_lote]

        for _ in range(50):
            id_actividad = random.choice(actividades_ids)
            id_caja = random.choice(cajas_lote_ids)

            cursor.execute("""
                INSERT INTO registro_transformacion_caja (id_actividad, id_caja)
                VALUES (%s, %s);
            """, (id_actividad, id_caja))

            print("Inserted registro_transformacion_caja")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar registro_transformacion_caja: {e}")

def insert_caja_salida(cursor):
    try:
        # Obtener los identificadores de las cajas de lote
        cursor.execute("SELECT id_caja FROM caja_lote;")
        cajas_lote = cursor.fetchall()
        cajas_lote_ids = [caja[0] for caja in cajas_lote]

        # Obtener los identificadores de las áreas
        cursor.execute("SELECT id_area FROM area;")
        areas = cursor.fetchall()
        areas_ids = [area[0] for area in areas]

        for _ in range(200):
            fecha_salida = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            id_caja = random.choice(cajas_lote_ids)
            id_area = random.choice(areas_ids)

            cursor.execute("""
                INSERT INTO caja_salida (fecha_salida, id_caja, id_area)
                VALUES (%s, %s, %s);
            """, (fecha_salida, id_caja, id_area))

            print("Inserted caja_salida")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar caja_salida: {e}")

def insert_lote_entrada(cursor):
    try:
        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        # Obtener los identificadores de los espacios
        cursor.execute("SELECT id_espacio FROM espacio;")
        espacios = cursor.fetchall()
        espacios_ids = [espacio[0] for espacio in espacios]

        for _ in range(200):
            fecha_entrada = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            id_lote = random.choice(lotes_ids)
            id_espacio = random.choice(espacios_ids)

            cursor.execute("""
                INSERT INTO Lote_entrada (fecha_entrada, id_lote, id_espacio)
                VALUES (%s, %s, %s);
            """, (fecha_entrada, id_lote, id_espacio))

            print("Inserted Lote_entrada")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al insertar Lote_entrada: {e}")

def insert_data(connection): #Insertar todos los datos en la base de datos
    cursor = connection.cursor()

    # Valores de las tablas
    cargos = ('Almacenero', 'Operario', 'Costurero', 'Inspector', 'Planificador', 'Jefe')
    estados = ('Cancelado', 'En mantenimiento', 'No disponible', 'Atrasado', 'Obsoleto', 'No iniciado', 'Completado', 'Usado', 'En proceso', 'Entregado', 'Ocupado', 'Disponible')
    tipos_mp = ('Franela','French Terry', 'Full Lycra', 'Jersey', 'Polialgodón', 'Poliéster', 'Piqué', 'Rib')
    colores = ('Negro', 'Blanco', 'Gris', 'Azul', 'Rojo', 'Verde', 'Amarillo', 'Naranja', 'Morado', 'Rosa', 'Marrón', 'Beige', 'Turquesa', 'Borgoña', 'Celeste')
    tipos_partes_prenda = ('Manga', 'Falda trasera', 'Pretina', 'Sisa', 'Pierna delantera', 'entrepierna', 'Falda delantera', 'Yugo', 'Bolsillo', 'Pierna trasera', 'Cuerpo delantero', 'Cintura', 'Bajo', 'Puño', 'Entrepierna', 'Cuello', 'Cuerpo trasero')
    tipos_cortes = ('Largo de la manga', 'Ancho de la manga', 'Largo delantero', 'Ancho delantero', 'Largo trasero', 'Ancho trasero', 'Forma del cuello', 'Largo del cuello', 'Ancho del puño', 'Largo del puño', 'Ancho de la pretina', 'Largo de la pretina', 'Tamaño del bolsillo', 'Posición del bolsillo', 'Largo del yugo', 'Ancho del yugo', 'Forma de la sisa', 'Profundidad de la sisa', 'Largo de la pierna', 'Ancho de la pierna', 'Ancho de la cintura', 'Largo de la cintura', 'Largo de la entrepierna', 'Ancho del bajo', 'Largo del bajo')
    tipos_lotes = ('Materia prima', 'Corte', 'Confección', 'Prenda')
    tipos_prendas = ('Camisa', 'Polo', 'Blusa', 'Pantalón', 'Short', 'Falda')
    estilos_prendas = ('Deportivo', 'Casual', 'Formal')
    tallas = ('XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL')
    generos = ('Masculino', 'Femenino')
    acabados = ('Etiquetado','Hangteado', 'Embolsado', 'Embalaje', 'Encaje')
    areas = ('Almacén Central', 'Corte', 'Confección', 'Almacén de tránsito', 'Acabado', 'Calidad', 'Planeamiento')
    aql_niveles = ('G1', 'G2', 'G3', 'S1', 'S2', 'S3', 'S4')
    aql_lote_rangos = ((2, 8), (9, 15), (16, 25), (26, 50), (51, 90), (91, 150), (151, 280), (281, 500), (501, 1200), (1201, 3200), (3201, 10000), (10001, 35000), (35001, 150000), (150001, 500000), (500001, 1000000))
    aql_codigos = (('A', 2), ('B', 3), ('C', 5), ('D', 8), ('E', 13), ('F', 20), ('G', 32), ('H', 50), ('J', 80), ('K', 125), ('L', 200), ('M', 315), ('N', 500), ('P', 800), ('Q', 1250), ('R', 2000))
    aql_significancias = (0.065, 0.10, 0.15, 0.25, 0.40, 0.65, 1.0, 1.5, 2.5, 4.0, 6.5)
    resultados = ('Conforme', 'No conforme')
    zonas = ('Materia prima', 'Corte', 'Confección', 'Producto terminado', 'Tránsito')

    insert_cargos(cursor, cargos)
    insert_estados(cursor, estados)
    insert_tipos_mp(cursor, tipos_mp)
    insert_colores(cursor, colores)
    insert_tipos_partes_prenda(cursor, tipos_partes_prenda)
    insert_tipos_cortes(cursor, tipos_cortes)
    insert_tipos_lotes(cursor, tipos_lotes)
    insert_tipos_prendas(cursor, tipos_prendas)
    insert_estilos_prendas(cursor, estilos_prendas)
    insert_tallas(cursor, tallas)
    insert_generos(cursor, generos)
    insert_acabados(cursor, acabados)
    insert_areas(cursor, areas)
    insert_aql_niveles(cursor, aql_niveles)
    insert_aql_lote_rangos(cursor, aql_lote_rangos)
    insert_aql_codigos(cursor, aql_codigos)
    insert_aql_significancias(cursor, aql_significancias)
    insert_resultados(cursor, resultados)
    insert_proveedor(cursor)
    insert_empleados(cursor)
    insert_maquinas(cursor)
    insert_dimension_materia_prima(cursor)
    insert_dimension_parte_prenda(cursor)
    insert_dimension_confeccion(cursor)
    insert_orden_pedido(cursor)
    insert_plan_produccion(cursor)
    insert_zonas(cursor)
    insert_aql_muestra(cursor)
    insert_aql_resultado_rango(cursor)
    insert_dimension_corte(cursor)
    insert_parte_corte_detalle(cursor)
    insert_dimension_prenda(cursor)
    insert_orden_trabajo(cursor)
    insert_pasillo(cursor)
    insert_dim_confeccion_detalle(cursor)
    insert_dim_prenda_detalle(cursor)
    insert_pedido_detalle(cursor)
    insert_estanterias(cursor)
    insert_ordenes_produccion(cursor)
    insert_actividades_diarias(cursor)
    insert_lotes(cursor)
    insert_empleado_actividad(cursor)
    insert_maquina_actividad(cursor)
    insert_caja_prenda(cursor)
    insert_espacios(cursor)
    insert_materia_prima(cursor)
    insert_corte(cursor)
    insert_registro_uso_lote(cursor)
    insert_caja_lote(cursor)
    insert_prenda(cursor)
    insert_lote_salida(cursor)
    insert_inspeccion_calidad(cursor)
    insert_confeccion(cursor)
    insert_registro_lote_caja(cursor)
    insert_registro_transformacion_caja(cursor)
    insert_caja_salida(cursor)
    insert_lote_entrada(cursor)
    
    
    connection.commit()
    messagebox.showinfo("Éxito", "Registros generados exitosamente")
    cursor.close()

def main(): #Función principal
    # Crear la ventana principal
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Solicitar datos al usuario
    host = simpledialog.askstring('Host', 'Ingrese el host de la base de datos (default localhost):', initialvalue='localhost')
    port = simpledialog.askstring('Puerto', 'Ingrese el puerto de la base de datos (default 5432):', initialvalue='5432')
    database = simpledialog.askstring('Base de Datos', 'Ingrese el nombre de la base de datos:')
    user = simpledialog.askstring('Usuario', 'Ingrese su usuario (default postgres):', initialvalue='postgres')
    password = simpledialog.askstring('Contraseña', 'Ingrese su contraseña:', show='*')

    if host and port and database and user and password:
        connection = connect_to_database(host, port, database, user, password)
        if connection:
            insert_data(connection)
    else:
        messagebox.showwarning('Advertencia', 'Todos los campos son obligatorios')

if __name__ == '__main__':
    main()
