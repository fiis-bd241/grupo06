import psycopg2
import tkinter as tk
from tkinter import simpledialog, messagebox
import sys

def connect_to_database(host, port, database, user, password):
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        print(f"Conexión exitosa a la base de datos: {database}")
        messagebox.showinfo('Conexión exitosa', f'Conexión exitosa a la base de datos: {database}')
        return connection
    except psycopg2.Error as e:
        # Manejar la excepción (mostrar mensaje de error)
        error_message = f"Error al conectar a la base de datos: {e}"
        print(error_message)  # Imprimir el error en la consola
        messagebox.showerror("Error de conexión", error_message)  # Mostrar un mensaje de error
        # Detener la ejecución del programa con un código de salida 1 (indica un error)
        sys.exit(1)

def get_db_credentials():
    # Crear la ventana principal
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Solicitar datos al usuario
    host = simpledialog.askstring('Host', 'Ingrese el host de la base de datos (default localhost):', initialvalue='localhost')
    port = simpledialog.askstring('Puerto', 'Ingrese el puerto de la base de datos (default 5432):', initialvalue='5432')
    database = simpledialog.askstring('Base de Datos', 'Ingrese el nombre de la base de datos:')
    user = simpledialog.askstring('Usuario', 'Ingrese su usuario (default postgres):', initialvalue='postgres')
    password = simpledialog.askstring('Contraseña', 'Ingrese su contraseña:', show='*')

    return host, port, database, user, password


def main(): #Función principal
    
    # Solicitar datos al usuario
    host, port, database, user, password = get_db_credentials()

    if all([host, port, database, user, password]):
        connection = connect_to_database(host, port, database, user, password)
        if connection:
            connection.close()
            messagebox.showinfo('Cierre', 'Conexión cerrada')
    else:
        print("Todos los campos son obligatorios.")
        messagebox.showwarning('Advertencia', 'Todos los campos son obligatorios')

if __name__ == '__main__':
    main()
