import psycopg2
from tkinter import messagebox
import random
from faker import Faker
from datetime import timedelta
import sys
import conectorBD
from inserts1 import inserts1
from inserts2 import inserts2

fake = Faker('es_ES')

def insert_dimension_corte(cursor): #Inserta dimensiones de corte
    try:
        print("Insertando dimensiones de corte en la base de datos...")
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

            cursor.execute("INSERT INTO dimension_corte (id_dim_materia_prima, id_dim_parte_prenda) VALUES (%s, %s);", (id_dim_materia_prima, id_dim_parte_prenda))
        
        cursor.connection.commit()
        print("Dimensiones de corte insertadas exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar dimensiones de corte: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_parte_corte_detalle(cursor): # Inserta parte de corte detalle    
    cortes_por_parte_prenda = {
        'Manga': ['Largo de la manga', 'Ancho de la manga'],
        'Cuerpo delantero': ['Largo delantero', 'Ancho delantero'],
        'Cuerpo trasero': ['Largo trasero', 'Ancho trasero'],
        'Cuello': ['Forma del cuello', 'Largo del cuello'],
        'Puño': ['Ancho del puño', 'Largo del puño'],
        'Pretina': ['Ancho de la pretina', 'Largo de la pretina'],
        'Bolsillo': ['Tamaño del bolsillo', 'Posición del bolsillo'],
        'Yugo': ['Largo del yugo', 'Ancho del yugo'],
        'Sisa': ['Forma de la sisa', 'Profundidad de la sisa'],
        'Pierna delantera': ['Largo de la pierna', 'Ancho de la pierna'],
        'Pierna trasera': ['Largo de la pierna', 'Ancho de la pierna'],
        'Cintura': ['Ancho de la cintura', 'Largo de la cintura'],
        'Entrepierna': ['Largo de la entrepierna'],
        'Bajo': ['Ancho del bajo', 'Largo del bajo'],
        'Falda delantera': ['Largo de la falda', 'Ancho de la falda'],
        'Falda trasera': ['Largo de la falda', 'Ancho de la falda']
    }    

    try:
        print("Insertando parte de corte detalle en la base de datos...")
        # Obtener todos los id_dim_parte_prenda y id_tipo_parte_prenda
        cursor.execute("SELECT dpp.id_dim_parte_prenda, tpp.nombre FROM dimension_parte_prenda dpp INNER JOIN tipo_parte_prenda tpp ON dpp.id_tipo_parte_prenda = tpp.id_tipo_parte_prenda;")

        dimensiones_parte_prenda = cursor.fetchall()
        dim_parte_prenda_dict = {dim[0]: dim[1] for dim in dimensiones_parte_prenda}
        ids_dim_parte_prenda = [dim[0] for dim in dimensiones_parte_prenda]

        # Obtener todos los id_tipo_corte con sus nombres
        cursor.execute("SELECT id_tipo_corte, nombre FROM tipo_corte;")
        tipos_corte = cursor.fetchall()
        tipo_corte_dict = {tipo[1]: tipo[0] for tipo in tipos_corte}

        if not dim_parte_prenda_dict:
            raise ValueError("No se encontraron dimensiones de parte de prenda en la tabla dimension_parte_prenda")
        if not tipo_corte_dict:
            raise ValueError("No se encontraron tipos de corte en la tabla tipo_corte")

        # Insertar datos en la tabla parte_corte_detalle
        for id_dim_parte_prenda in ids_dim_parte_prenda:
            cortes_parte_prenda = cortes_por_parte_prenda.get(dim_parte_prenda_dict.get(id_dim_parte_prenda))
            
            for corte in cortes_parte_prenda:
                id_tipo_corte = tipo_corte_dict.get(corte)
                medida = round(random.uniform(10, 40), 2)

                cursor.execute("INSERT INTO parte_corte_detalle (id_dim_parte_prenda, id_tipo_corte, medida) VALUES (%s, %s, %s);", (id_dim_parte_prenda, id_tipo_corte, medida))

        cursor.connection.commit()  # Confirmar todas las inserciones exitosas
        print("Parte de corte detalle insertada exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar parte de corte detalle: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_dimension_prenda(cursor): #Inserta dimensiones de prenda
    try:
        print("Insertando dimensiones de prenda en la base de datos...")
        # Obtener todos los id_dim_confeccion
        cursor.execute("SELECT id_dim_confeccion FROM dimension_confeccion;")
        dimensiones_confeccion = cursor.fetchall()
        dim_confeccion_ids = [dim[0] for dim in dimensiones_confeccion]

        if not dim_confeccion_ids:
            raise ValueError("No se encontraron dimensiones de confección en la tabla dimension_confeccion")

        for _ in range(100):
            id_dim_confeccion = random.choice(dim_confeccion_ids)

            cursor.execute("INSERT INTO dimension_prenda (id_dim_confeccion) VALUES (%s);", (id_dim_confeccion,))
        
        cursor.connection.commit()
        print("Dimensiones de prenda insertadas exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar dimensiones de prenda: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_orden_trabajo(cursor): # Inserta órdenes de trabajo
    entidad_estado_relations = ('No iniciado', 'En proceso', 'Completado', 'Atrasado', 'Cancelado')
    try:
        print("Insertando órdenes de trabajo en la base de datos...")
        # Obtener todos los id_estado relacionados con 'Orden_pedido'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (entidad_estado_relations,))
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
     
        for _ in range(50):
            fecha_creacion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            fecha_inicio = fake.date_time_between_dates(datetime_start=fecha_creacion, datetime_end=fecha_creacion + timedelta(days=5), tzinfo=None)
            fecha_fin = fake.date_time_between_dates(datetime_start=fecha_inicio, datetime_end=fecha_inicio + timedelta(days=30), tzinfo=None)
            prioridad = random.randint(1, 5)
            id_plan = random.choice(plan_ids)
            id_orden_pedido = random.choice(orden_pedido_ids)
            id_estado = random.choice(estado_ids)  # Escoger un estado aleatorio

            cursor.execute("INSERT INTO orden_trabajo (fecha_inicio, fecha_fin, prioridad, id_estado, id_plan, id_orden_pedido,fecha_creacion) VALUES (%s, %s, %s, %s, %s, %s, %s);", (fecha_inicio, fecha_fin, prioridad, id_estado, id_plan, id_orden_pedido, fecha_creacion))
        
        cursor.connection.commit()
        print("Órdenes de trabajo insertadas exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar órdenes de trabajo: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_pasillo(cursor): # Inserta pasillos
    try:
        print("Insertando pasillos en la base de datos...")
        cursor.execute("SELECT id_zona FROM zona;")
        zonas = cursor.fetchall()

        for zona in zonas:
            id_zona = zona[0]
            for _ in range(10):
                ancho_pasillo = round(random.uniform(2.0, 4.0), 1)
                largo_pasillo = round(random.uniform(10.0, 15.0), 1)

                # Obtener el último número de pasillo para este id_zona
                cursor.execute("SELECT MAX(id_pasillo) FROM pasillo WHERE id_zona = %s;", (id_zona,))

                last_hall_number = cursor.fetchone()[0]

                if last_hall_number is None:
                    last_hall_number = id_zona * 100

                next_hall_number = last_hall_number + 1

                cursor.execute("INSERT INTO pasillo (id_pasillo, ancho_pasillo, largo_pasillo, id_zona) VALUES (%s, %s, %s, %s);", (next_hall_number, ancho_pasillo, largo_pasillo, id_zona))
        
        cursor.connection.commit()
        print("Pasillos insertados exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar pasillos: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)


def insert_dim_confeccion_detalle(cursor): # Inserta dim_confeccion_detalle
    partes_por_prenda = {
        'Camisa': ['Manga', 'Cuerpo delantero', 'Cuerpo trasero', 'Cuello', 'Puño', 'Pretina', 'Bolsillo', 'Yugo', 'Sisa'],
        'Polo': ['Manga', 'Cuerpo delantero', 'Cuerpo trasero', 'Cuello', 'Puño', 'Pretina', 'Yugo', 'Sisa'],
        'Blusa': ['Manga', 'Cuerpo delantero', 'Cuerpo trasero', 'Cuello', 'Puño', 'Pretina', 'Bolsillo', 'Yugo', 'Sisa'],
        'Pantalón': ['Pierna delantera', 'Pierna trasera', 'Cintura', 'Entrepierna', 'Bajo'],
        'Short': ['Pierna delantera', 'Pierna trasera', 'Cintura', 'Entrepierna', 'Bajo'],
        'Falda': ['Falda delantera', 'Falda trasera', 'Pretina', 'Cintura', 'Bajo']
    }

    try:
        print("Insertando dim_confeccion_detalle en la base de datos...")

        # Obtener todos los id_dim_confeccion y el tipo de prenda correspondiente
        cursor.execute("""
            SELECT dc.id_dim_confeccion, tp.nombre
            FROM dimension_confeccion dc
            INNER JOIN tipo_prenda tp ON dc.id_tipo_prenda = tp.id_tipo_prenda;
        """)
        dim_confeccion_data = cursor.fetchall()
        dim_confeccion_dict = {dim[0]: dim[1] for dim in dim_confeccion_data}
        ids_dim_confeccion = [dim[0] for dim in dim_confeccion_data]

        # Obtener todos los id_dim_corte con sus nombres
        cursor.execute("""
            SELECT dc.id_dim_corte, tpp.nombre
            FROM dimension_corte dc
            INNER JOIN dimension_parte_prenda dpp ON dc.id_dim_parte_prenda = dpp.id_dim_parte_prenda
            INNER JOIN tipo_parte_prenda tpp ON dpp.id_tipo_parte_prenda = tpp.id_tipo_parte_prenda;
        """)
        dim_corte_data = cursor.fetchall()
        dim_corte_dict = {dim[1]: [] for dim in dim_corte_data}
        for dim in dim_corte_data:
            dim_corte_dict[dim[1]].append(dim[0])

        if not dim_confeccion_dict:
            raise ValueError("No se encontraron registros en la tabla dimension_confeccion")
        if not dim_corte_dict:
            raise ValueError("No se encontraron registros en la tabla dimension_corte")

        # Insertar datos en la tabla dim_confeccion_detalle
        for id_dim_confeccion in ids_dim_confeccion:
            partes_prenda = partes_por_prenda.get(dim_confeccion_dict.get(id_dim_confeccion))

            for parte in partes_prenda:
                if parte not in dim_corte_dict:
                    continue
                id_dim_corte = random.choice(dim_corte_dict.get(parte, []))
                cursor.execute("INSERT INTO dim_confeccion_detalle (id_dim_confeccion, id_dim_corte) VALUES (%s, %s);", (id_dim_confeccion, id_dim_corte))

        cursor.connection.commit()
        print("Dim_confeccion_detalle insertada exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar en la tabla dim_confeccion_detalle: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_dim_prenda_detalle(cursor): # Inserta dim_prenda_detalle
    try:
        print("Insertando detalles de prenda en la base de datos...")

        # Obtener todos los id_dim_prenda y nombres de prenda de la tabla dimension_prenda
        cursor.execute("SELECT id_dim_prenda FROM dimension_prenda;")
        dim_prenda_data = cursor.fetchall()
        dim_prenda_ids = [dim[0] for dim in dim_prenda_data]

        # Obtener todos los id_acabado y sus nombres
        cursor.execute("SELECT id_acabado FROM acabado;")
        acabado_data = cursor.fetchall()
        acabado_ids = [acabado[0] for acabado in acabado_data]

        if not dim_prenda_ids:
            raise ValueError("No se encontraron registros en la tabla dimension_prenda")
        if not acabado_ids:
            raise ValueError("No se encontraron registros en la tabla acabado")

        # Insertar datos en la tabla dim_prenda_detalle
        for id_dim_prenda in dim_prenda_ids:
            # Seleccionar una cantidad aleatoria de acabados para cada prenda, asegurando al menos uno
            num_acabados = random.randint(1, len(acabado_ids))
            acabados_seleccionados = random.sample(acabado_ids, num_acabados)

            for id_acabado in acabados_seleccionados:
                cursor.execute("INSERT INTO dim_prenda_detalle (id_dim_prenda, id_acabado) VALUES (%s, %s);", (id_dim_prenda, id_acabado))

        cursor.connection.commit()
        print("Detalles de prenda insertados exitosamente\n")
    
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar detalles de prenda: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_pedido_detalle(cursor): # Inserta pedido_detalle
    try:
        print("Insertando pedido_detalle en la base de datos...")

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

        for id_orden_pedido in orden_pedido_ids:
            # Seleccionar una cantidad aleatoria de dimensiones prenda para cada pedido, asegurando al menos una
            num_dim_prenda = random.randint(1, 5)
            dim_prenda_seleccionadas = random.sample(dim_prenda_ids, num_dim_prenda)

            for id_dim_prenda in dim_prenda_seleccionadas:
                cursor.execute("INSERT INTO pedido_detalle (id_orden_pedido, id_dim_prenda) VALUES (%s, %s);", (id_orden_pedido, id_dim_prenda))

        cursor.connection.commit()
        print("Pedido_detalle insertado exitosamente\n")

    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar pedido_detalle: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_estanterias(cursor): # Inserta estanterias
    try:
        print("Insertando estanterías en la base de datos...")
        
        # Obtener los identificadores de los pasillos
        cursor.execute("SELECT id_pasillo, largo_pasillo, ancho_pasillo FROM pasillo;")
        pasillos = cursor.fetchall()

        for pasillo in pasillos:
            id_pasillo = pasillo[0]
            for _ in range(5):  # Insertar 5 estanterías por pasillo
                # Generar dimensiones aleatorias para la estantería
                ancho = round(pasillo[1] / 5, 2)
                largo = round(random.choice([i * 0.1 for i in range(20, 31)]), 2)
                alto = 8.50

                # Obtener el último número de estanteria para este id_pasillo
                cursor.execute("SELECT MAX(id_estanteria) FROM estanteria WHERE id_pasillo = %s;", (id_pasillo,))
                
                last_shelf_number = cursor.fetchone()[0]

                if last_shelf_number is None:
                    last_shelf_number = id_pasillo * 100

                next_shelf_number = last_shelf_number + 1

                # Insertar la estantería en la base de datos
                cursor.execute("INSERT INTO estanteria (id_estanteria, ancho_estanteria, largo_estanteria, alto_estanteria, id_pasillo) VALUES (%s, %s, %s, %s, %s);", (next_shelf_number, ancho, largo, alto, id_pasillo))
                
        cursor.connection.commit()
        print("Estanterías insertadas exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar estanterías: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)


def inserts3(cursor):
    insert_dimension_corte(cursor)
    insert_parte_corte_detalle(cursor)
    insert_dimension_prenda(cursor)
    insert_orden_trabajo(cursor)
    insert_pasillo(cursor)

def inserts4(cursor):
    insert_dim_confeccion_detalle(cursor)
    insert_dim_prenda_detalle(cursor)
    insert_pedido_detalle(cursor)
    insert_estanterias(cursor)


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
