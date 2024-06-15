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
from inserts3_4 import inserts3, inserts4
from inserts5_6_7 import inserts5_6_7
from inserts8_9 import inserts8, inserts9

fake = Faker('es_ES')  # Usamos es_ES para generar datos en español

def insert_data(cursor): #Insertar todos los datos en la base de datos
    """Función para insertar los datos en la base de datos."""
    inserts1(cursor)
    inserts2(cursor)
    inserts3(cursor)
    inserts4(cursor)
    inserts5_6_7(cursor)
    inserts8(cursor)
    inserts9(cursor)
    

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
