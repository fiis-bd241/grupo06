import psycopg2
from tkinter import messagebox
import random
from faker import Faker
import re
from datetime import timedelta
import pytz
import sys
import conectorBD
from inserts1 import inserts1

fake = Faker('es_ES')

def insert_proveedor(cursor): # Inserta proveedores, direccion, telefono y email
    # Función para generar correos basados en la denominación social del proveedor
    def generate_email(denominacion_social):
        denominacion_social = denominacion_social.replace(' ', '_').lower()
        return f"comercial@{re.sub('[^0-9a-zA-Z_]', '', denominacion_social)}.com"
    
    try:
        print("Insertando proveedores (proveedores, telefonos, direcciones, emails) en la base de datos...")
        for _ in range(20):# Generar registros para proveedor
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

            cursor.execute("INSERT INTO proveedor (ruc, denominacion_social, id_direccion, id_telefono, id_correo) VALUES (%s, %s, %s, %s, %s);", (ruc, denominacion_social, id_direccion, id_telefono, id_correo))

        cursor.connection.commit()
        print("Proveedores insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar proveedores: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_empleados(cursor): # Inserta empleados, telefonos, direcciones y emails
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

    try:
        print("Insertando empleados (empleados, telefonos, direcciones, emails) en la base de datos...")
        # Generar registros para empleados
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

                cursor.execute("INSERT INTO empleado (dni, nombre, segundo_apellido, primer_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", (dni, nombre, segundo_apellido, primer_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo))

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

                cursor.execute("INSERT INTO empleado (dni, nombre, segundo_apellido, primer_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", (dni, nombre, segundo_apellido, primer_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo))

        cursor.connection.commit()
        print("Empleados insertados exitosamente\n")
        
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar empleados: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_maquinas(cursor): # Inserta máquinas
    maquina_estado_relations = {
        'Maquina': ('Disponible', 'No disponible', 'En mantenimiento'),
    }

    try:
        print("Insertando máquinas en la base de datos...")
        # Obtener todos los id_estado relacionados con 'Orden_pedido'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(maquina_estado_relations['Maquina']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]
        
        if not estado_ids:
            raise ValueError("No se encontraron estados válidos en la tabla estado")

        for _ in range(30):
            capacidad_total = random.randint(2, 5) * 1000
            id_estado = random.choice(estado_ids)  # Seleccionar un estado aleatorio

            cursor.execute("INSERT INTO maquina (capacidad_total, id_estado) VALUES (%s, %s);", (capacidad_total, id_estado))
        
        cursor.connection.commit()
        print("Máquinas insertadas exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar máquinas: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_dimension_materia_prima(cursor): # Inserta dimensiones de materia prima
    try:
        print("Insertando dimensiones de materia prima en la base de datos...")
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

            cursor.execute("INSERT INTO dimension_materia_prima (id_tipo_materia_prima, id_color) VALUES (%s, %s);", (id_tipo_materia_prima, id_color))
        cursor.connection.commit()
        print("Dimensiones de materia prima insertadas exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar dimensiones de materia prima: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_dimension_parte_prenda(cursor): # Inserta dimensiones de parte de prenda
    try:
        print("Insertando dimensiones de parte de prenda en la base de datos...")
        # Obtener todos los id_tipo_parte_prenda
        cursor.execute("SELECT id_tipo_parte_prenda FROM tipo_parte_prenda;")
        tipos_parte_prenda = cursor.fetchall()
        tipo_parte_prenda_ids = [tipo[0] for tipo in tipos_parte_prenda]

        if not tipo_parte_prenda_ids:
            raise ValueError("No se encontraron tipos de parte de prenda en la tabla tipo_parte_prenda")

        for _ in range(100):
            id_tipo_parte_prenda = random.choice(tipo_parte_prenda_ids)

            cursor.execute("INSERT INTO dimension_parte_prenda (id_tipo_parte_prenda) VALUES (%s);", (id_tipo_parte_prenda,))
        cursor.connection.commit()
        print("Dimensiones de parte de prenda insertadas exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar dimensiones de parte de prenda: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_dimension_confeccion(cursor):
    medidas_por_prenda = {
        'Camisa': ['medida_longitud', 'medida_hombro', 'medida_pecho', 'medida_manga'],
        'Polo': ['medida_longitud', 'medida_hombro', 'medida_pecho', 'medida_manga'],
        'Blusa': ['medida_longitud', 'medida_hombro', 'medida_pecho', 'medida_manga', 'medida_cintura'],
        'Pantalón': ['medida_longitud', 'medida_cintura', 'medida_cadera', 'medida_muslo'],
        'Short': ['medida_longitud', 'medida_cintura', 'medida_cadera', 'medida_muslo'],
        'Falda': ['medida_longitud', 'medida_cintura', 'medida_cadera']
    }

    try:
        print("Insertando dimensiones de confección en la base de datos...")

        # Obtener todos los id_tipo_prenda
        cursor.execute("SELECT id_tipo_prenda, nombre FROM tipo_prenda;")
        tipos_prenda = cursor.fetchall()
        tipo_prenda_dict = {tipo[0]: tipo[1] for tipo in tipos_prenda}

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
        if not tipo_prenda_dict:
            raise ValueError("No se encontraron tipos de prenda en la tabla tipo_prenda")
        if not estilo_prenda_ids:
            raise ValueError("No se encontraron estilos de prenda en la tabla estilo_prenda")
        if not talla_ids:
            raise ValueError("No se encontraron tallas en la tabla talla")
        if not genero_ids:
            raise ValueError("No se encontraron géneros en la tabla genero")

        for _ in range(100):
            id_tipo_prenda = random.choice(list(tipo_prenda_dict.keys()))
            nombre_tipo_prenda = tipo_prenda_dict[id_tipo_prenda]
            id_estilo_prenda = random.choice(estilo_prenda_ids)
            id_talla = random.choice(talla_ids)
            id_genero = random.choice(genero_ids)

            # Generar medidas basadas en el tipo de prenda
            medidas = {}
            for medida in medidas_por_prenda[nombre_tipo_prenda]:
                if 'pecho' in medida:
                    medidas[medida] = round(random.uniform(70, 90), 2)
                elif 'cintura' in medida:
                    medidas[medida] = round(random.uniform(60, 90), 2)
                elif 'cadera' in medida:
                    medidas[medida] = round(random.uniform(80, 90), 2)
                elif 'hombro' in medida:
                    medidas[medida] = round(random.uniform(35, 60), 2)
                elif 'longitud' in medida:
                    medidas[medida] = round(random.uniform(50, 90), 2)
                elif 'manga' in medida:
                    medidas[medida] = round(random.uniform(50, 80), 2)
                elif 'muslo' in medida:
                    medidas[medida] = round(random.uniform(40, 70), 2)

            # Preparar y ejecutar la consulta de inserción para guia_confeccion
            columns = ', '.join(medidas.keys())
            placeholders = ', '.join(['%s'] * len(medidas))
            values = tuple(medidas.values())

            query = f"INSERT INTO guia_confeccion ({columns}) VALUES ({placeholders}) RETURNING id_guia_confeccion;"
            cursor.execute(query, values)
            id_guia_confeccion = cursor.fetchone()[0]

            # Insertar dimensión de confección
            cursor.execute("INSERT INTO dimension_confeccion (id_tipo_prenda, id_estilo_prenda, id_guia_confeccion, id_talla, id_genero) VALUES (%s, %s, %s, %s, %s);", (id_tipo_prenda, id_estilo_prenda, id_guia_confeccion, id_talla, id_genero))

        cursor.connection.commit()
        print("Dimensiones de confección insertadas exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar dimensiones de confección: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_orden_pedido(cursor): # Inserta órdenes de pedido    
    orden_pedido_estado_relations = ('No iniciado', 'En proceso', 'Completado', 'Atrasado', 'Cancelado')
    try:
        print("Insertando órdenes de pedido en la base de datos...")
        # Obtener todos los id_estado relacionados con 'Orden_pedido'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (orden_pedido_estado_relations,))
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
            fecha_entrega = fake.date_time_between_dates(datetime_start=fecha_creacion, datetime_end=fecha_creacion + timedelta(days=60), tzinfo=timezone)

            cursor.execute("INSERT INTO orden_pedido (fecha_entrega, cantidad, id_estado, fecha_creacion) VALUES (%s, %s, %s, %s);", (fecha_entrega, cantidad, id_estado, fecha_creacion))
        
        cursor.connection.commit()
        print("Órdenes de pedido insertadas exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar órdenes de pedido: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_plan_produccion(cursor): # Inserta órdenes de pedido
    plan_produccion_estado_relations = ('No iniciado', 'En proceso', 'Completado', 'Atrasado', 'Cancelado')
    try:
        print("Insertando planes de producción en la base de datos...")
        # Obtener todos los id_estado relacionados con 'Orden_pedido'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (plan_produccion_estado_relations,))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        if not estado_ids:
            raise ValueError("No se encontraron estados en la tabla estado")

        for _ in range(100):
            id_estado = random.choice(estado_ids)
            
            fecha_creacion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            fecha_inicio = fake.date_time_between_dates(datetime_start=fecha_creacion, datetime_end=fecha_creacion + timedelta(days=10), tzinfo=None)
            fecha_fin = fake.date_time_between_dates(datetime_start=fecha_inicio, datetime_end=fecha_inicio + timedelta(days=30), tzinfo=None)

            cursor.execute("INSERT INTO plan_produccion (fecha_inicio, fecha_fin, id_estado, fecha_creacion) VALUES (%s, %s, %s, %s);", (fecha_inicio, fecha_fin, id_estado, fecha_creacion))
        cursor.connection.commit()
        print("Planes de producción insertados exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar planes de producción: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_zonas(cursor): # Inserta zonas
    area_zona_relations = {
        'Almacén Central': ('Materia prima', 'Corte', 'Confección', 'Producto terminado'),
        'Almacén de tránsito': ('Tránsito',),
    }
    try:
        print("Insertando zonas en la base de datos...")

        for area, zona_list in area_zona_relations.items():
            # Obtener el id_area correspondiente
            cursor.execute("SELECT id_area FROM area WHERE nombre = %s;", (area,))
            id_area = cursor.fetchone()

            if not id_area:
                raise ValueError(f"No se encontró el área '{area}' en la tabla area")

            id_area = id_area[0]

            # Obtener el último número de zona para este id_area
            cursor.execute("SELECT MAX(id_zona) FROM zona WHERE id_area = %s;", (id_area,))
            
            last_zone_number = cursor.fetchone()[0]

            if last_zone_number is None:
                last_zone_number = id_area * 100

            for zona in zona_list:
                # Incrementar el número de zona
                next_zone_number = last_zone_number + 1
                last_zone_number = next_zone_number  # Update the last zone number for the next iteration

                cursor.execute("INSERT INTO zona (id_zona, nombre, id_area) VALUES (%s, %s, %s) ON CONFLICT (nombre) DO NOTHING;", (next_zone_number, zona, id_area))

        cursor.connection.commit()
        print("Zonas insertadas exitosamente\n")

    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar zonas: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_aql_muestra(cursor): #Inserta AQL muestra
    # Relaciones de aql_muestra
    aql_muestra_relations = {
        'G1': {(2, 8): 'A', (9, 15): 'A', (16, 25): 'B', (26, 50): 'C', (51, 90): 'C', (91, 150): 'D', (151, 280): 'E', (281, 500): 'F', (501, 1200): 'G', (1201, 3200): 'H', (3201, 10000): 'J', (10001, 35000): 'K', (35001, 150000): 'L', (150001, 500000): 'M', (500001, 1000000): 'N'},
        'G2': {(2, 8): 'A', (9, 15): 'B', (16, 25): 'C', (26, 50): 'D', (51, 90): 'E', (91, 150): 'F', (151, 280): 'G', (281, 500): 'H', (501, 1200): 'J', (1201, 3200): 'K', (3201, 10000): 'L', (10001, 35000): 'M', (35001, 150000): 'N', (150001, 500000): 'P', (500001, 1000000): 'Q'},
        'G3': {(2, 8): 'B', (9, 15): 'C', (16, 25): 'D', (26, 50): 'E', (51, 90): 'F', (91, 150): 'G', (151, 280): 'H', (281, 500): 'J', (501, 1200): 'K', (1201, 3200): 'L', (3201, 10000): 'M', (10001, 35000): 'N', (35001, 150000): 'P', (150001, 500000): 'Q', (500001, 1000000): 'R'},
        'S1': {(2, 8): 'A', (9, 15): 'A', (16, 25): 'A', (26, 50): 'A', (51, 90): 'B', (91, 150): 'B', (151, 280): 'B', (281, 500): 'B', (501, 1200): 'C', (1201, 3200): 'C', (3201, 10000): 'C', (10001, 35000): 'C', (35001, 150000): 'D', (150001, 500000): 'D', (500001, 1000000): 'D'},
        'S2': {(2, 8): 'A', (9, 15): 'A', (16, 25): 'A', (26, 50): 'B', (51, 90): 'B', (91, 150): 'B', (151, 280): 'C', (281, 500): 'C', (501, 1200): 'C', (1201, 3200): 'D', (3201, 10000): 'D', (10001, 35000): 'D', (35001, 150000): 'E', (150001, 500000): 'E', (500001, 1000000): 'E'},
        'S3': {(2, 8): 'A', (9, 15): 'A', (16, 25): 'B', (26, 50): 'B', (51, 90): 'C', (91, 150): 'C', (151, 280): 'D', (281, 500): 'D', (501, 1200): 'E', (1201, 3200): 'E', (3201, 10000): 'F', (10001, 35000): 'F', (35001, 150000): 'G', (150001, 500000): 'G', (500001, 1000000): 'H'},
        'S4': {(2, 8): 'A', (9, 15): 'A', (16, 25): 'B', (26, 50): 'C', (51, 90): 'C', (91, 150): 'D', (151, 280): 'E', (281, 500): 'E', (501, 1200): 'F', (1201, 3200): 'G', (3201, 10000): 'G', (10001, 35000): 'H', (35001, 150000): 'J', (150001, 500000): 'J', (500001, 1000000): 'K'}
    }
    
    try:
        print("Insertando AQL muestra en la base de datos...")
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

                cursor.execute("INSERT INTO aql_muestra (id_aql_nivel, id_aql_lote_rango, id_aql_codigo) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING;", (id_aql_nivel, id_aql_lote_rango, id_aql_codigo))
        
        cursor.connection.commit()
        print("AQL muestra insertada exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar AQL muestra: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_aql_resultado_rango(cursor): #Inserta AQL resultado rango
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
    try:
        print("Insertando AQL resultado rango en la base de datos...")

        # Obtener todos los niveles de significancia AQL
        cursor.execute("SELECT id_aql_significancia, nivel_significancia FROM aql_significancia;")
        significancias = cursor.fetchall()
        significancia_dict = {float(significancia[1]): significancia[0] for significancia in significancias}

        # Obtener todos los códigos AQL
        cursor.execute("SELECT id_aql_codigo FROM aql_codigo;")
        codigos = cursor.fetchall()
        codigo_dict = {codigo[0]: codigo[0] for codigo in codigos}

        for nivel_significancia, rango_codigos in aql_resultado_rango_relations.items():
            id_aql_significancia = significancia_dict.get(nivel_significancia)
            if not id_aql_significancia:
                raise ValueError(f"No se encontró la significancia '{nivel_significancia}' en la tabla aql_significancia")

            for codigo, rango in rango_codigos.items():
                id_aql_codigo = codigo_dict.get(codigo)
                if not id_aql_codigo:
                    raise ValueError(f"No se encontró el código AQL '{codigo}' en la tabla aql_codigo")

                max_aceptacion, min_rechazo = rango
                cursor.execute("INSERT INTO aql_resultado_rango (id_aql_codigo, id_aql_significancia, max_aceptacion, min_rechazo) VALUES (%s, %s, %s, %s);", (id_aql_codigo, id_aql_significancia, max_aceptacion, min_rechazo))
        
        cursor.connection.commit()
        print("AQL resultado rango insertado exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar AQL resultado rango: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)


def inserts2(cursor):
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


def main(): # Función prueba
    """Función principal para la ejecución del script."""

    host, port, database, user, password = conectorBD.get_db_credentials()

    if all([host, port, database, user, password]):
        print("Conectando a la base de datos...")
        connection = conectorBD.connect_to_database(host, port, database, user, password)
        connection.autocommit = False
        cursor = connection.cursor()
        inserts1(cursor)
        inserts2(cursor)
        cursor.close()
        print("Registros generados exitosamente.")
        messagebox.showinfo("Éxito", "Registros generados exitosamente")
        connection.close()
        print("Conexión cerrada.")
        messagebox.showinfo('Cierre', 'Conexión cerrada')
    else:
        print("Todos los campos son obligatorios.")
        messagebox.showwarning('Advertencia', 'Todos los campos son obligatorios')

if __name__ == "__main__":
    main()
