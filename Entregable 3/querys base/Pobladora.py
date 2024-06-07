import psycopg2
from tkinter import messagebox
import random
from faker import Faker
import re
from datetime import timedelta
import pytz
import conectorBD
from inserts1 import inserts1
from inserts2 import inserts2

fake = Faker('es_ES')  # Usamos es_ES para generar datos en español

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

def insert_data(cursor): #Insertar todos los datos en la base de datos
    zonas = ('Materia prima', 'Corte', 'Confección', 'Producto terminado', 'Tránsito')

    inserts1(cursor)
    inserts2(cursor)
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

def main(): #Función principal

    """Función principal para la ejecución del script."""

    host, port, database, user, password = conectorBD.get_db_credentials()

    if all([host, port, database, user, password]):
        print("Conectando a la base de datos...")
        connection = conectorBD.connect_to_database(host, port, database, user, password)
        connection.autocommit = False
        cursor = connection.cursor()
        insert_data(cursor)
        cursor.close()
        print("Registros generados exitosamente.")
        messagebox.showinfo("Éxito", "Registros generados exitosamente")
        connection.close()
        print("Conexión cerrada.")
        messagebox.showinfo('Cierre', 'Conexión cerrada')
    else:
        print("Todos los campos son obligatorios.")
        messagebox.showwarning('Advertencia', 'Todos los campos son obligatorios')
if __name__ == '__main__':
    main()
