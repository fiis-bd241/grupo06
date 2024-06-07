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

def insert_proveedor(cursor): #Inserta proveedores, direccion, telefono y email
    # Función para generar correos basados en la denominación social del proveedor
    def generate_email(denominacion_social):
        denominacion_social = denominacion_social.replace(' ', '_').lower()
        return f"comercial@{re.sub('[^0-9a-zA-Z_]', '', denominacion_social)}.com"
    
    try:
        print("Insertando proveedores en la base de datos...")

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

            cursor.execute("""
                INSERT INTO proveedor (ruc, denominacion_social, id_direccion, id_telefono, id_correo)
                VALUES (%s, %s, %s, %s, %s);
            """, (ruc, denominacion_social, id_direccion, id_telefono, id_correo))

        cursor.connection.commit()
        print("Proveedores insertados exitosamente.")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar proveedores: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_empleados(cursor):
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
        print("Insertando empleados en la base de datos...")

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

                cursor.execute("""
                    INSERT INTO empleado (dni, nombre, segundo_apellido, primer_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (dni, nombre, segundo_apellido, primer_apellido, id_area, id_direccion, id_telefono, id_correo, id_cargo))

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

        cursor.connection.commit()
        print("Empleados insertados exitosamente.")
        
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar empleados: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)
def insert_estados(cursor): # Inserta estados
    estados = ('Cancelado', 'En mantenimiento', 'No disponible', 'Atrasado', 'Obsoleto', 'No iniciado', 'Completado', 'Usado', 'En proceso', 'Entregado', 'Ocupado', 'Disponible')
    try:
        print("Insertando estados en la base de datos...")
        for estado in estados:
            cursor.execute("INSERT INTO estado (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_estado;", (estado,))
        cursor.connection.commit()
        print("Estados insertados exitosamente.")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar estados: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tipos_mp(cursor): #Inserta tipos de materia prima
    tipos_materia_prima = ('Franela','French Terry', 'Full Lycra', 'Jersey', 'Polialgodón', 'Poliéster', 'Piqué', 'Rib')
    try:
        for tipo_mp in tipos_materia_prima:
            cursor.execute("INSERT INTO tipo_materia_prima (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_tipo_materia_prima;", (tipo_mp,))
        cursor.connection.commit()
        print("Tipos de materia prima insertados exitosamente.")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tipos de materia prima: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_colores(cursor): #Inserta colores
    colores = ('Negro', 'Blanco', 'Gris', 'Azul', 'Rojo', 'Verde', 'Amarillo', 'Naranja', 'Morado', 'Rosa', 'Marrón', 'Beige', 'Turquesa', 'Borgoña', 'Celeste')
    try:
        for color in colores:
            cursor.execute("INSERT INTO color (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_color;", (color,))
        cursor.connection.commit()
        print("Colores insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar colores: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tipos_partes_prenda(cursor): #Inserta tipos de partes de prenda
    tipos_partes_prenda = ('Manga', 'Falda trasera', 'Pretina', 'Sisa', 'Pierna delantera', 'entrepierna', 'Falda delantera', 'Yugo', 'Bolsillo', 'Pierna trasera', 'Cuerpo delantero', 'Cintura', 'Bajo', 'Puño', 'Entrepierna', 'Cuello', 'Cuerpo trasero')
    try:
        for tipo_parte_prenda in tipos_partes_prenda:
            cursor.execute("INSERT INTO tipo_parte_prenda (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_tipo_parte_prenda;", (tipo_parte_prenda,))
        cursor.connection.commit()
        print("Tipos de partes de prenda insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tipos de partes de prenda: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tipos_cortes(cursor): #Inserta tipos de cortes
    tipos_cortes = ('Largo de la manga', 'Ancho de la manga', 'Largo delantero', 'Ancho delantero', 'Largo trasero', 'Ancho trasero', 'Forma del cuello', 'Largo del cuello', 'Ancho del puño', 'Largo del puño', 'Ancho de la pretina', 'Largo de la pretina', 'Tamaño del bolsillo', 'Posición del bolsillo', 'Largo del yugo', 'Ancho del yugo', 'Forma de la sisa', 'Profundidad de la sisa', 'Largo de la pierna', 'Ancho de la pierna', 'Ancho de la cintura', 'Largo de la cintura', 'Largo de la entrepierna', 'Ancho del bajo', 'Largo del bajo')
    try:
        for tipo_corte in tipos_cortes:
            cursor.execute("INSERT INTO tipo_corte (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_tipo_corte;", (tipo_corte,))
        cursor.connection.commit()
        print("Tipos de cortes insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tipos de cortes: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tipos_lotes(cursor): #Inserta tipos de lotes
    tipos_lotes = ('Materia prima', 'Corte', 'Confección', 'Prenda')
    try:
        for tipo_lote in tipos_lotes:
            cursor.execute("INSERT INTO tipo_lote (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_tipo_lote;", (tipo_lote,))
        cursor.connection.commit()
        print("Tipos de lotes insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tipos de lotes: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tipos_prendas(cursor): #Inserta tipos de prendas
    tipos_prendas = ('Camisa', 'Polo', 'Blusa', 'Pantalón', 'Short', 'Falda')
    try:
        for tipo_prenda in tipos_prendas:
            cursor.execute("INSERT INTO tipo_prenda (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_tipo_prenda;", (tipo_prenda,))
        cursor.connection.commit()
        print("Tipos de prendas insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tipos de prendas: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_estilos_prendas(cursor): #Inserta estilos de prendas
    estilos_prendas = ('Deportivo', 'Casual', 'Formal')
    try:
        for estilo_prenda in estilos_prendas:
            cursor.execute("INSERT INTO estilo_prenda (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_estilo_prenda;", (estilo_prenda,))
        cursor.connection.commit()
        print("Estilos de prendas insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar estilos de prendas: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tallas(cursor): #Inserta tallas
    tallas = ('XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL')
    try:
        for talla in tallas:
            cursor.execute("INSERT INTO talla (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_talla;", (talla,))
        cursor.connection.commit()
        print("Tallas insertadas correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tallas: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_generos(cursor): #Inserta géneros
    generos = ('Masculino', 'Femenino')
    try:
        for genero in generos:
            cursor.execute("INSERT INTO genero (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_genero;", (genero,))
        cursor.connection.commit()
        print("Géneros insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar géneros: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_acabados(cursor): #Inserta acabados
    acabados = ('Etiquetado','Hangteado', 'Embolsado', 'Embalaje', 'Encaje')
    try:
        for acabado in acabados:
            cursor.execute("INSERT INTO acabado (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_acabado;", (acabado,))
        cursor.connection.commit()
        print("Acabados insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar acabados: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_areas(cursor): #Inserta áreas
    areas = ('Almacén Central', 'Corte', 'Confección', 'Almacén de tránsito', 'Acabado', 'Calidad', 'Planeamiento')
    try:
        for area in areas:
            cursor.execute("INSERT INTO area (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_area;", (area,))
        cursor.connection.commit()
        print("Áreas insertadas correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar áreas: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_aql_niveles(cursor): #Inserta niveles AQL
    aql_niveles = ('G1', 'G2', 'G3', 'S1', 'S2', 'S3', 'S4')
    try:
        for aql_nivel in aql_niveles:
            cursor.execute("INSERT INTO aql_nivel (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_aql_nivel;", (aql_nivel,))
        cursor.connection.commit()
        print("Niveles AQL insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar niveles AQL: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_aql_lote_rangos(cursor): #Inserta rangos de lote AQL
    aql_lote_rangos = ((2, 8), (9, 15), (16, 25), (26, 50), (51, 90), (91, 150), (151, 280), (281, 500), (501, 1200), (1201, 3200), (3201, 10000), (10001, 35000), (35001, 150000), (150001, 500000), (500001, 1000000))
    try:
        for aql_lote_rango in aql_lote_rangos:
            cursor.execute("INSERT INTO aql_lote_rango (min_lote, max_lote) VALUES (%s, %s) RETURNING id_aql_lote_rango;", (aql_lote_rango[0],aql_lote_rango[1]))
        cursor.connection.commit()
        print("Rangos de lote AQL insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar rangos de lote AQL: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_aql_codigos(cursor): #Inserta códigos AQL
    aql_codigos = (('A', 2), ('B', 3), ('C', 5), ('D', 8), ('E', 13), ('F', 20), ('G', 32), ('H', 50), ('J', 80), ('K', 125), ('L', 200), ('M', 315), ('N', 500), ('P', 800), ('Q', 1250), ('R', 2000))
    try:
        for aql_codigo in aql_codigos:
            cursor.execute("INSERT INTO aql_codigo (id_aql_codigo, tamaño_muestra) VALUES (%s, %s) ON CONFLICT (tamaño_muestra) DO NOTHING RETURNING id_aql_codigo;", (aql_codigo[0], aql_codigo[1]))
        cursor.connection.commit()
        print("Códigos AQL insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar códigos AQL: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_aql_significancias(cursor): #Inserta significancias AQL
    aql_significancias = (0.065, 0.10, 0.15, 0.25, 0.40, 0.65, 1.0, 1.5, 2.5, 4.0, 6.5)
    try:
        for aql_significancia in aql_significancias:
            cursor.execute("INSERT INTO aql_significancia (nivel_significancia) VALUES (%s) ON CONFLICT (nivel_significancia) DO NOTHING RETURNING id_aql_significancia;", (aql_significancia,))
        cursor.connection.commit()
        print("Significancias AQL insertadas correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar significancias AQL: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_resultados(cursor): #Inserta tipos de resultados
    resultados = ('Conforme', 'No conforme')
    try:
        for resultado in resultados:
            cursor.execute("INSERT INTO resultado (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING RETURNING id_resultado;", (resultado,))
        cursor.connection.commit()
        print("Resultados insertados correctamente")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar resultados: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def inserts1(cursor):
    insert_proveedor(cursor)
    insert_estados(cursor)
    insert_tipos_mp(cursor)
    insert_colores(cursor)
    insert_tipos_partes_prenda(cursor)
    insert_tipos_cortes(cursor)
    insert_tipos_lotes(cursor)
    insert_tipos_prendas(cursor)
    insert_estilos_prendas(cursor)
    insert_tallas(cursor)
    insert_generos(cursor)
    insert_acabados(cursor)
    insert_areas(cursor)
    insert_aql_niveles(cursor)
    insert_aql_lote_rangos(cursor)
    insert_aql_codigos(cursor)
    insert_aql_significancias(cursor)
    insert_resultados(cursor)

def main(): #Función prueba
    """Función principal para la ejecución del script."""

    host, port, database, user, password = conectorBD.get_db_credentials()

    if all([host, port, database, user, password]):
        print("Conectando a la base de datos...")
        connection = conectorBD.connect_to_database(host, port, database, user, password)
        cursor.connection.autocommit = False
        cursor = connection.cursor()
        inserts1(cursor)
        insert_proveedor(cursor)
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
