import psycopg2
from tkinter import messagebox
from faker import Faker
import sys
import conectorBD

fake = Faker('es_ES')

def insert_cargos(cursor): # Inserta cargos
    cargos = ('Almacenero', 'Operario', 'Costurero', 'Inspector', 'Planificador', 'Jefe')
    try:
        print("Insertando cargos en la base de datos...")
        for cargo in cargos:
            cursor.execute("INSERT INTO cargo (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (cargo,))
        
        cursor.connection.commit()
        print("Cargos insertados exitosamente.")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar cargos: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_estados(cursor): # Inserta estados
    estados = ('Cancelado', 'En mantenimiento', 'No disponible', 'Atrasado', 'Obsoleto', 'No iniciado', 'Completado', 'Usado', 'En proceso', 'Entregado', 'Ocupado', 'Disponible')
    try:
        print("Insertando estados en la base de datos...")
        for estado in estados:
            cursor.execute("INSERT INTO estado (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (estado,))
        
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
        print("Insertando tipos de materia prima en la base de datos...")
        for tipo_mp in tipos_materia_prima:
            cursor.execute("INSERT INTO tipo_materia_prima (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (tipo_mp,))
        
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
        print("Insertando colores en la base de datos...")
        for color in colores:
            cursor.execute("INSERT INTO color (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (color,))
        
        cursor.connection.commit()
        print("Colores insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar colores: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tipos_partes_prenda(cursor): #Inserta tipos de partes de prenda
    tipos_partes_prenda = ('Manga', 'Falda trasera', 'Pretina', 'Sisa', 'Pierna delantera', 'Falda delantera', 'Yugo', 'Bolsillo', 'Pierna trasera', 'Cuerpo delantero', 'Cintura', 'Bajo', 'Puño', 'Entrepierna', 'Cuello', 'Cuerpo trasero')
    try:
        print("Insertando tipos de partes de prenda en la base de datos...")
        for tipo_parte_prenda in tipos_partes_prenda:
            cursor.execute("INSERT INTO tipo_parte_prenda (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (tipo_parte_prenda,))
        
        cursor.connection.commit()
        print("Tipos de partes de prenda insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tipos de partes de prenda: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tipos_cortes(cursor): #Inserta tipos de cortes
    tipos_cortes = ('Largo de la manga', 'Ancho de la manga', 'Largo delantero', 'Ancho delantero', 'Largo trasero', 'Ancho trasero', 'Forma del cuello', 'Largo del cuello', 'Ancho del puño', 'Largo del puño', 'Ancho de la pretina', 'Largo de la pretina', 'Tamaño del bolsillo', 'Posición del bolsillo', 'Largo del yugo', 'Ancho del yugo', 'Forma de la sisa', 'Profundidad de la sisa', 'Largo de la pierna', 'Ancho de la pierna', 'Ancho de la cintura', 'Largo de la cintura', 'Largo de la entrepierna', 'Ancho del bajo', 'Largo del bajo', 'Largo de la falda', 'Ancho de la falda')
    try:
        print("Insertando tipos de cortes en la base de datos...")
        for tipo_corte in tipos_cortes:
            cursor.execute("INSERT INTO tipo_corte (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (tipo_corte,))
        
        cursor.connection.commit()
        print("Tipos de cortes insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tipos de cortes: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tipos_lotes(cursor): #Inserta tipos de lotes
    tipos_lotes = ('Materia prima', 'Corte', 'Confección')
    try:
        print("Insertando tipos de lotes en la base de datos...")
        for tipo_lote in tipos_lotes:
            cursor.execute("INSERT INTO tipo_lote (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (tipo_lote,))
        
        cursor.connection.commit()
        print("Tipos de lotes insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tipos de lotes: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tipos_prendas(cursor): #Inserta tipos de prendas
    tipos_prendas = ('Camisa', 'Polo', 'Blusa', 'Pantalón', 'Short', 'Falda')
    try:
        print("Insertando tipos de prendas en la base de datos...")
        for tipo_prenda in tipos_prendas:
            cursor.execute("INSERT INTO tipo_prenda (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (tipo_prenda,))
        
        cursor.connection.commit()
        print("Tipos de prendas insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tipos de prendas: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_estilos_prendas(cursor): #Inserta estilos de prendas
    estilos_prendas = ('Deportivo', 'Casual', 'Formal')
    try:
        print("Insertando estilos de prendas en la base de datos...")
        for estilo_prenda in estilos_prendas:
            cursor.execute("INSERT INTO estilo_prenda (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (estilo_prenda,))
        
        cursor.connection.commit()
        print("Estilos de prendas insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar estilos de prendas: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_tallas(cursor): #Inserta tallas
    tallas = ('XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL')
    try:
        print("Insertando tallas en la base de datos...")
        for talla in tallas:
            cursor.execute("INSERT INTO talla (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (talla,))
        
        cursor.connection.commit()
        print("Tallas insertadas exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar tallas: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_generos(cursor): #Inserta géneros
    generos = ('Masculino', 'Femenino')
    try:
        print("Insertando géneros en la base de datos...")
        for genero in generos:
            cursor.execute("INSERT INTO genero (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (genero,))
        
        cursor.connection.commit()
        print("Géneros insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar géneros: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_acabados(cursor): #Inserta acabados
    acabados = ('Hangteado', 'Vaporizado', 'Doblado', 'Embolsado', 'Encajado')
    try:
        print("Insertando acabados en la base de datos...")
        for acabado in acabados:
            cursor.execute("INSERT INTO acabado (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (acabado,))
        
        cursor.connection.commit()
        print("Acabados insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar acabados: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_areas(cursor): #Inserta áreas
    areas = ('Almacén Central', 'Corte', 'Confección', 'Almacén de tránsito', 'Acabado', 'Calidad', 'Planeamiento')
    try:
        print("Insertando áreas en la base de datos...")
        for area in areas:
            cursor.execute("INSERT INTO area (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (area,))
        
        cursor.connection.commit()
        print("Áreas insertadas exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar áreas: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_aql_niveles(cursor): #Inserta niveles AQL
    aql_niveles = ('G1', 'G2', 'G3', 'S1', 'S2', 'S3', 'S4')
    try:
        print("Insertando niveles AQL en la base de datos...")
        for aql_nivel in aql_niveles:
            cursor.execute("INSERT INTO aql_nivel (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (aql_nivel,))
        
        cursor.connection.commit()
        print("Niveles AQL insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar niveles AQL: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_aql_lote_rangos(cursor): #Inserta rangos de lote AQL
    aql_lote_rangos = ((2, 8), (9, 15), (16, 25), (26, 50), (51, 90), (91, 150), (151, 280), (281, 500), (501, 1200), (1201, 3200), (3201, 10000), (10001, 35000), (35001, 150000), (150001, 500000), (500001, 1000000))
    try:
        print("Insertando rangos de lote AQL en la base de datos...")
        for aql_lote_rango in aql_lote_rangos:
            cursor.execute("INSERT INTO aql_lote_rango (min_lote, max_lote) VALUES (%s, %s);", (aql_lote_rango[0],aql_lote_rango[1]))
        
        cursor.connection.commit()
        print("Rangos de lote AQL insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar rangos de lote AQL: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_aql_codigos(cursor): #Inserta códigos AQL
    aql_codigos = (('A', 2), ('B', 3), ('C', 5), ('D', 8), ('E', 13), ('F', 20), ('G', 32), ('H', 50), ('J', 80), ('K', 125), ('L', 200), ('M', 315), ('N', 500), ('P', 800), ('Q', 1250), ('R', 2000))
    try:
        print("Insertando códigos AQL en la base de datos...")
        for aql_codigo in aql_codigos:
            cursor.execute("INSERT INTO aql_codigo (id_aql_codigo, tamaño_muestra) VALUES (%s, %s) ON CONFLICT (tamaño_muestra) DO NOTHING;", (aql_codigo[0], aql_codigo[1]))
        
        cursor.connection.commit()
        print("Códigos AQL insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar códigos AQL: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_aql_significancias(cursor): #Inserta significancias AQL
    aql_significancias = (0.065, 0.10, 0.15, 0.25, 0.40, 0.65, 1.0, 1.5, 2.5, 4.0, 6.5)
    try:
        print("Insertando significancias AQL en la base de datos...")
        for aql_significancia in aql_significancias:
            cursor.execute("INSERT INTO aql_significancia (nivel_significancia) VALUES (%s) ON CONFLICT (nivel_significancia) DO NOTHING;", (aql_significancia,))
        
        cursor.connection.commit()
        print("Significancias AQL insertadas exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar significancias AQL: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)

def insert_resultados(cursor): #Inserta tipos de resultados
    resultados = ('Conforme', 'No conforme')
    try:
        print("Insertando resultados en la base de datos...")
        for resultado in resultados:
            cursor.execute("INSERT INTO resultado (nombre) VALUES (%s) ON CONFLICT (nombre) DO NOTHING;", (resultado,))
        
        cursor.connection.commit()
        print("Resultados insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar resultados: {e}"
        print(error)
        messagebox.showerror('Error', error)
        sys.exit(1)


def inserts1(cursor):
    insert_cargos(cursor)
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
        connection.autocommit = False
        cursor = connection.cursor()
        inserts1(cursor)
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
