import psycopg2
from tkinter import messagebox
import random
from faker import Faker
from datetime import timedelta
import sys
import conectorBD
from inserts1 import inserts1
from inserts2 import inserts2
from inserts3_4 import inserts3, inserts4

fake = Faker('es_ES')

def insert_ordenes_produccion(cursor): # Inserta órdenes de producción
    orden_produccion_estado_relations = {
        'Orden_produccion': ('No iniciado', 'En proceso', 'Completado', 'Atrasado', 'Cancelado'),
    }
    orden_produccion_areas = ('Corte', 'Confección', 'Acabado')
    areas_dimension = {
        'Corte': 'id_dim_corte',
        'Confección': 'id_dim_confeccion',
        'Acabado': 'id_dim_prenda'
    }
    
    try:
        print("Insertando órdenes de producción en la base de datos...")
        # Obtener los identificadores de áreas
        cursor.execute("SELECT id_area, nombre FROM area WHERE nombre IN %s;", (orden_produccion_areas,))
        areas = cursor.fetchall()
        areas_dict = {area[1]: area[0] for area in areas}

        # Obtener todos los id_estado relacionados con 'orden_produccion'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(orden_produccion_estado_relations['Orden_produccion']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        # Obtener los identificadores de las órdenes de trabajo
        cursor.execute("SELECT id_orden_trabajo, fecha_creacion, fecha_inicio FROM orden_trabajo;")
        ordenes_trabajo = cursor.fetchall()
        ids_orden_trabajo = [orden_trabajo[0] for orden_trabajo in ordenes_trabajo]
        fechas_dict = {orden_trabajo[0]: (orden_trabajo[1], orden_trabajo[2]) for orden_trabajo in ordenes_trabajo}

        cursor.execute("""
            SELECT ot.id_orden_trabajo, dp.id_dim_prenda, dc.id_dim_confeccion, dct.id_dim_corte
            FROM orden_trabajo ot
            INNER JOIN orden_pedido op ON op.id_orden_pedido = ot.id_orden_pedido
            INNER JOIN pedido_detalle pd ON pd.id_orden_pedido = op.id_orden_pedido
            INNER JOIN dimension_prenda dp ON dp.id_dim_prenda = pd.id_dim_prenda
            INNER JOIN dimension_confeccion dc ON dc.id_dim_confeccion = dp.id_dim_confeccion
            INNER JOIN dim_confeccion_detalle dcd ON dcd.id_dim_confeccion = dc.id_dim_confeccion
            INNER JOIN dimension_corte dct ON dct.id_dim_corte = dcd.id_dim_corte;
        """)
        dimensiones_data = cursor.fetchall()

        # Inicializar los diccionarios
        orden_trabajo_prenda_dict = {}
        orden_trabajo_confeccion_dict = {}
        orden_trabajo_corte_dict = {}

        # Procesar los resultados y llenar los diccionarios
        for row in dimensiones_data:
            id_orden_trabajo, id_dim_prenda, id_dim_confeccion, id_dim_corte = row
            
            if id_orden_trabajo not in orden_trabajo_prenda_dict:
                orden_trabajo_prenda_dict[id_orden_trabajo] = []
            orden_trabajo_prenda_dict[id_orden_trabajo].append(id_dim_prenda)
            
            if id_orden_trabajo not in orden_trabajo_confeccion_dict:
                orden_trabajo_confeccion_dict[id_orden_trabajo] = []
            orden_trabajo_confeccion_dict[id_orden_trabajo].append(id_dim_confeccion)
            
            if id_orden_trabajo not in orden_trabajo_corte_dict:
                orden_trabajo_corte_dict[id_orden_trabajo] = []
            orden_trabajo_corte_dict[id_orden_trabajo].append(id_dim_corte)


        for id_orden_trabajo in ids_orden_trabajo:  # Insertar órdenes de producción a cada orden de trabajo
            fecha_creacion_ot = fechas_dict[id_orden_trabajo][0]
            fecha_inicio_ot = fechas_dict[id_orden_trabajo][1]
            fecha_actual_inicio = fecha_inicio_ot            

            for area in orden_produccion_areas: # Insertar ordenes de produccion para cada area
                id_area = areas_dict[area]
                fecha_creacion = fake.date_time_between(start_date=fecha_creacion_ot, end_date=fecha_creacion_ot + timedelta(minutes=120), tzinfo=None)
                
                fecha_fin = fecha_actual_inicio + timedelta(days=random.randint(5, 9))
                cantidad = random.randint(500, 1000)
                id_estado = random.choice(estado_ids)

                # Determinar qué dimensiones se van a llenar
                dim_a_llenar = areas_dimension.get(areas_dict.get(id_area))

                if area == 'Corte':
                    dim_id = random.choice(orden_trabajo_corte_dict[id_orden_trabajo])
                elif area == 'Confección':
                    dim_id = random.choice(orden_trabajo_confeccion_dict[id_orden_trabajo])
                elif area == 'Acabado':
                    dim_id = random.choice(orden_trabajo_prenda_dict[id_orden_trabajo])

                # Insertar la orden de producción
                cursor.execute(f"""
                    INSERT INTO orden_producción (fecha_inicio, fecha_fin, cantidad, id_estado, id_area, {areas_dimension[area]}, id_orden_trabajo, fecha_creacion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """, (fecha_actual_inicio, fecha_fin, cantidad, id_estado, id_area, dim_id, id_orden_trabajo, fecha_creacion))

                fecha_actual_inicio = fecha_fin + timedelta(days=1)
        
        cursor.connection.commit()
        print("Órdenes de producción insertadas exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar órdenes de producción: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_actividades_diarias(cursor): # Inserta actividades diarias
    try:
        print("Insertando actividades diarias en la base de datos...")
        # Obtener los identificadores de las órdenes de producción
        cursor.execute("SELECT id_orden_producción, fecha_inicio, fecha_fin FROM orden_producción;")
        ordenes_produccion_data = cursor.fetchall()
        ordenes_produccion = [(orden_produccion[0], orden_produccion[1], orden_produccion[2]) for orden_produccion in ordenes_produccion_data]

        # Insertar actividades diarias para cada orden de producción
        for id_orden_produccion, fecha_inicio_op, fecha_fin_op in ordenes_produccion: 
            for _ in range(random.randint(6,10)):  # Insertar 100 actividades diarias
                fecha_actividad = fake.date_between(start_date=fecha_inicio_op, end_date=fecha_fin_op)

                # Insertar la actividad diaria
                cursor.execute("""
                    INSERT INTO actividad_diaria (fecha_actividad, id_orden_producción)
                    VALUES (%s, %s);
                """, (fecha_actividad, id_orden_produccion))

        cursor.connection.commit()
        print("Actividades diarias insertadas exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar actividades diarias: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_lotes(cursor): # Inserta lotes
    lote_estado_relations = {
        'Lote': ('Disponible', 'En proceso', 'Usado', 'Obsoleto'),
    }
    
    try:
        print("Insertando lotes en la base de datos...")
        # Obtener todos los id_estado relacionados con 'lote'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(lote_estado_relations['Lote']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        # Obtener los identificadores de los tipos de lote
        cursor.execute("SELECT id_tipo_lote, nombre FROM tipo_lote;")
        tipos_lote_data = cursor.fetchall()
        tipos_lote_dict = {tipo[1]: tipo[0] for tipo in tipos_lote_data}

        # Obtener los identificadores de las actividades diarias ordenadas por fecha de actividad
        cursor.execute("""
            SELECT ad.id_actividad, ad.fecha_actividad
            FROM actividad_diaria ad
            INNER JOIN orden_producción op ON op.id_orden_producción = ad.id_orden_producción
            ORDER BY ad.fecha_actividad;
        """)
        actividades_diarias_data = cursor.fetchall()
        actividades_diarias = [(actividad_diaria[0], actividad_diaria[1]) for actividad_diaria in actividades_diarias_data]

        # Obtener los identificadores de las dimensiones de materia prima
        cursor.execute("SELECT id_dim_materia_prima FROM dimension_materia_prima;")
        dimensiones_materia_prima = cursor.fetchall()
        dim_materia_prima_ids = [dim_materia_prima[0] for dim_materia_prima in dimensiones_materia_prima]

        for id_actividad_diaria, fecha_actividad in actividades_diarias:
            # Obtener los identificadores de las dimensiones de la orden de producción asociada
            cursor.execute("""
                SELECT op.id_dim_confeccion, op.id_dim_corte
                FROM actividad_diaria ad
                INNER JOIN orden_producción op ON op.id_orden_producción = ad.id_orden_producción
                WHERE ad.id_actividad = %s;
            """, (id_actividad_diaria,))
            dimensiones_orden_produccion = cursor.fetchone()
            
            # Verificar y manejar los valores nulos
            if dimensiones_orden_produccion:
                id_dim_confeccion = dimensiones_orden_produccion[0]
                id_dim_corte = dimensiones_orden_produccion[1]
                id_dim_materia_prima = None

                if id_dim_confeccion is None and id_dim_corte is None:
                    id_tipo_lote = tipos_lote_dict['Materia prima']
                    id_dim_materia_prima = random.choice(dim_materia_prima_ids)
                    id_actividad_diaria = None
                elif id_dim_confeccion is None:
                    id_tipo_lote = tipos_lote_dict['Corte']
                elif id_dim_corte is None:
                    id_tipo_lote = tipos_lote_dict['Confección']
                else:
                    print("Error: hay dos dimensiones llenas.")
                    cursor.connection.rollback()
                    sys.exit(1)

            cantidad = random.randint(100, 1000)
            id_estado = random.choice(estado_ids)

            # Insertar el lote
            cursor.execute("""
                INSERT INTO lote (cantidad, id_estado, id_tipo_lote, id_dim_corte, id_dim_confeccion, id_dim_materia_prima, id_actividad, fecha_creacion)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """, (cantidad, id_estado, id_tipo_lote, id_dim_corte, id_dim_confeccion, id_dim_materia_prima, id_actividad_diaria, fecha_actividad))

        cursor.connection.commit()
        print("Lotes insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar lotes: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_empleado_actividad(cursor): # Inserta empleados_actividad
    try:
        print("Insertando empleados_actividad en la base de datos...")
        # Obtener los identificadores de las actividades diarias
        cursor.execute("""
            SELECT ad.id_actividad
            FROM actividad_diaria ad
            INNER JOIN orden_producción op ON op.id_orden_producción = ad.id_orden_producción
            INNER JOIN area a ON a.id_area = op.id_area
            WHERE a.nombre IN ('Confección','Acabado');
        """)
        actividades = cursor.fetchall()
        actividades_ids = [actividad[0] for actividad in actividades]

        # Obtener los identificadores de los empleados
        cursor.execute("SELECT id_empleado FROM empleado;")
        empleados = cursor.fetchall()
        empleados_ids = [empleado[0] for empleado in empleados]

        registros_insertados = 0
        pares_insertados = set()  # Conjunto para almacenar pares únicos insertados

        # Iterar sobre todas las actividades y asegurarse de que haya al menos un registro para cada una
        for id_actividad in actividades_ids:
            if registros_insertados >= 100:
                break  # Salir del bucle si ya se han insertado 100 registros

            # Verificar si ya hay un registro para esta actividad
            if id_actividad not in pares_insertados:
                id_empleado = random.choice(empleados_ids)
                cantidad_hecha = random.randint(10, 20)

                cursor.execute("""
                    INSERT INTO empleado_actividad (id_actividad, id_empleado, cantidad_hecha)
                    VALUES (%s, %s, %s);
                """, (id_actividad, id_empleado, cantidad_hecha))

                pares_insertados.add((id_actividad, id_empleado))  # Agregar la actividad al conjunto de pares insertados
                registros_insertados += 1

        # Generar el resto de registros hasta llegar a 100 (si es necesario)
        while registros_insertados < 300:
            id_actividad = random.choice(actividades_ids)
            id_empleado = random.choice(empleados_ids)

            # Verificar si el par ya ha sido insertado
            if (id_actividad, id_empleado) not in pares_insertados:
                cantidad_hecha = random.randint(10, 20)

                cursor.execute("""
                    INSERT INTO empleado_actividad (id_actividad, id_empleado, cantidad_hecha)
                    VALUES (%s, %s, %s);
                """, (id_actividad, id_empleado, cantidad_hecha))

                pares_insertados.add((id_actividad, id_empleado))  # Agregar el par al conjunto de pares insertados
                registros_insertados += 1

        cursor.connection.commit()
        print("Empleados_actividad insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar empleados_actividad: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_maquina_actividad(cursor): # Inserta maquina_actividad
    try:
        print("Insertando maquina_actividad en la base de datos...")
        # Obtener los identificadores de las actividades diarias
        cursor.execute("""
            SELECT ad.id_actividad
            FROM actividad_diaria ad
            INNER JOIN orden_producción op ON op.id_orden_producción = ad.id_orden_producción
            INNER JOIN area a ON a.id_area = op.id_area
            WHERE a.nombre IN ('Corte');
        """)
        actividades = cursor.fetchall()
        actividades_ids = [actividad[0] for actividad in actividades]

        # Obtener los identificadores de las máquinas
        cursor.execute("SELECT id_maquina FROM maquina;")
        maquinas = cursor.fetchall()
        maquinas_ids = [maquina[0] for maquina in maquinas]

        registros_insertados = 0
        pares_insertados = set()  # Conjunto para almacenar pares únicos insertados

        # Iterar sobre todas las actividades y asegurarse de que haya al menos un registro para cada una
        for id_actividad in actividades_ids:
            if registros_insertados >= 100:
                break  # Salir del bucle si ya se han insertado 100 registros

            # Verificar si ya hay un registro para esta actividad
            if id_actividad not in pares_insertados:
                id_maquina = random.choice(maquinas_ids)
                cantidad_hecha = random.randint(1, 5) * 100

                cursor.execute("""
                    INSERT INTO maquina_actividad (id_actividad, id_maquina, cantidad_hecha)
                    VALUES (%s, %s, %s);
                """, (id_actividad, id_maquina, cantidad_hecha))

                pares_insertados.add(id_actividad)  # Agregar la actividad al conjunto de pares insertados
                registros_insertados += 1

        # Generar el resto de registros hasta llegar a 100 (si es necesario)
        while registros_insertados < 100:
            id_actividad = random.choice(actividades_ids)
            id_maquina = random.choice(maquinas_ids)

            # Verificar si el par ya ha sido insertado
            if (id_actividad, id_maquina) not in pares_insertados:
                cantidad_hecha = random.randint(1, 5) * 100

                cursor.execute("""
                    INSERT INTO maquina_actividad (id_actividad, id_maquina, cantidad_hecha)
                    VALUES (%s, %s, %s);
                """, (id_actividad, id_maquina, cantidad_hecha))

                pares_insertados.add((id_actividad, id_maquina))  # Agregar el par al conjunto de pares insertados
                registros_insertados += 1

        cursor.connection.commit()
        print("Maquina_actividad insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar maquina_actividad: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)


def inserts5_6_7(cursor):
    insert_ordenes_produccion(cursor)
    insert_actividades_diarias(cursor)
    insert_lotes(cursor)
    insert_empleado_actividad(cursor)
    insert_maquina_actividad(cursor)


def main(): #Función prueba
    """Función principal para la ejecución del script."""

    host, port, database, user, password = conectorBD.get_db_credentials()

    if all([host, port, database, user, password]):
        print("Conectando a la base de datos...")
        connection = conectorBD.connect_to_database(host, port, database, user, password)
        connection.autocommit = False
        cursor = connection.cursor()
        inserts1(cursor)
        inserts2(cursor)
        inserts3(cursor)
        inserts4(cursor)
        inserts5_6_7(cursor)
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
