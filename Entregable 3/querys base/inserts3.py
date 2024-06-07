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
        print("Dimensiones de corte insertadas exitosamente.")
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
        print("Parte de corte detalle insertada exitosamente.")
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
        print("Dimensiones de prenda insertadas exitosamente.")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar dimensiones de prenda: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_orden_trabajo(cursor):
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
     
        for _ in range(100):
            fecha_creacion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            fecha_inicio = fake.date_time_between_dates(datetime_start=fecha_creacion, datetime_end=fecha_creacion + timedelta(days=5), tzinfo=None)
            fecha_fin = fake.date_time_between_dates(datetime_start=fecha_inicio, datetime_end=fecha_inicio + timedelta(days=10), tzinfo=None)
            prioridad = random.randint(1, 5)
            id_plan = random.choice(plan_ids)
            id_orden_pedido = random.choice(orden_pedido_ids)
            id_estado = random.choice(estado_ids)  # Escoger un estado aleatorio

            cursor.execute("INSERT INTO orden_trabajo (fecha_inicio, fecha_fin, prioridad, id_estado, id_plan, id_orden_pedido,fecha_creacion) VALUES (%s, %s, %s, %s, %s, %s, %s);", (fecha_inicio, fecha_fin, prioridad, id_estado, id_plan, id_orden_pedido, fecha_creacion))
        
        cursor.connection.commit()
        print("Órdenes de trabajo insertadas exitosamente.")
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
                ancho_pasillo = round(random.uniform(1.5, 2.0), 2)
                largo_pasillo = round(random.uniform(1.5, 2.0), 2)

                # Obtener el último número de pasillo para este id_zona
                cursor.execute("SELECT MAX(id_pasillo) FROM pasillo WHERE id_zona = %s;", (id_zona,))

                last_hall_number = cursor.fetchone()[0]

                if last_hall_number is None:
                    last_hall_number = id_zona * 100

                next_hall_number = last_hall_number + 1

                cursor.execute("INSERT INTO pasillo (id_pasillo, ancho_pasillo, largo_pasillo, id_zona) VALUES (%s, %s, %s, %s);", (next_hall_number, ancho_pasillo, largo_pasillo, id_zona))
        
        cursor.connection.commit()
        print("Pasillos insertados exitosamente.")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar pasillos: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)




def inserts3(cursor):
    insert_dimension_corte(cursor)
    insert_parte_corte_detalle(cursor)
    insert_dimension_prenda(cursor)
    insert_orden_trabajo(cursor)
    insert_pasillo(cursor)

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
