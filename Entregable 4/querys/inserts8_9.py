import psycopg2
from tkinter import messagebox
import random
from faker import Faker
import sys
import conectorBD
from inserts1 import inserts1
from inserts2 import inserts2
from inserts3_4 import inserts3, inserts4
from inserts5_6_7 import inserts5_6_7

fake = Faker('es_ES')

def insert_materia_prima(cursor): # Inserta materia prima
    try:
        print("Insertando materia_prima en la base de datos...")
        # Obtener los identificadores de los lotes y dimensiones de materia prima correspondientes
        cursor.execute("SELECT id_lote, id_dim_materia_prima FROM lote WHERE id_dim_materia_prima is not null;")
        lotes = cursor.fetchall()
        lotes_data = [(lote[0], lote[1]) for lote in lotes]

        # Obtener los identificadores de los proveedores
        cursor.execute("SELECT id_proveedor FROM proveedor;")
        proveedores = cursor.fetchall()
        proveedores_ids = [proveedor[0] for proveedor in proveedores]

        for id_lote, id_dim_materia_prima in lotes_data: # Insertar materia prima para cada lote
            id_proveedor = random.choice(proveedores_ids)
            for _ in range(100): # Insertar 100 registros de materia prima
                cursor.execute("""
                    INSERT INTO materia_prima (id_lote, id_dim_materia_prima, id_proveedor)
                    VALUES (%s, %s, %s);
                """, (id_lote, id_dim_materia_prima, id_proveedor))
            cursor.connection.commit()
       
        print("Materia_prima insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar materia_prima: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_corte(cursor): # Inserta corte
    try:
        print("Insertando corte en la base de datos...")
        # Obtener los identificadores de los lotes y dimensiones de corte correspondientes
        cursor.execute("SELECT id_lote, id_dim_corte FROM lote WHERE id_dim_corte is not null;")
        lotes = cursor.fetchall()
        lotes_data = [(lote[0], lote[1]) for lote in lotes]

        # Obtener los identificadores de las máquinas de corte
        cursor.execute("SELECT id_maquina FROM maquina;")
        maquinas = cursor.fetchall()
        maquinas_ids = [maquina[0] for maquina in maquinas]

        for id_lote, id_dim_corte in lotes_data: # Insertar corte para cada lote
            for id_maquina in random.sample(maquinas_ids,5): # Insertar corte de cada máquina
                for _ in range(random.randint(50, 100)): # Insertar de 50 a 100 registros de corte
                    cursor.execute("""
                        INSERT INTO corte (id_lote, id_dim_corte, id_maquina)
                        VALUES (%s, %s, %s);
                    """, (id_lote, id_dim_corte, id_maquina))
                cursor.connection.commit()

        print("Corte insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar corte: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_registro_uso_lote(cursor): # Inserta registro de uso de lote
    try:
        print("Insertando registro_uso_lote en la base de datos...")
        # Obtener los identificadores de las actividades diarias
        cursor.execute("SELECT id_actividad FROM actividad_diaria;")
        actividades = cursor.fetchall()
        actividades_ids = [actividad[0] for actividad in actividades]

        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        registros_insertados = 0

        while registros_insertados < 400:
            id_actividad = random.choice(actividades_ids)
            id_lote = random.choice(lotes_ids)
            cantidad_usada = random.randint(100, 1000)

            # Verificar si el registro ya existe
            cursor.execute("""
                SELECT COUNT(*) FROM registro_uso_lote
                WHERE id_actividad = %s AND id_lote = %s;
            """, (id_actividad, id_lote))

            existe = cursor.fetchone()[0]

            if not existe:
                cursor.execute("""
                    INSERT INTO registro_uso_lote (id_actividad, id_lote, cantidad_usada)
                    VALUES (%s, %s, %s);
                """, (id_actividad, id_lote, cantidad_usada))
                registros_insertados += 1

        cursor.connection.commit()
        print("Registro_uso_lote insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar registro_uso_lote: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_caja_prenda(cursor): # Inserta caja de prenda
    caja_prenda_estado_relations = {
        'Caja_prenda': ('En proceso', 'Entregado', 'Obsoleto'),
    }
    
    try:
        print("Insertando caja_prenda en la base de datos...")
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
            id_estado = random.choice(estado_ids)
            id_dim_prenda = random.choice(dimensiones_prenda_ids)
            id_actividad = random.choice(actividades_ids)

            cursor.execute("""
                INSERT INTO caja_prenda (cantidad, fecha_creacion, id_estado, id_dim_prenda, id_actividad)
                VALUES (%s, %s, %s, %s, %s);
            """, (cantidad, fecha_creacion, id_estado, id_dim_prenda, id_actividad))

        cursor.connection.commit()
        print("Caja_prenda insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar caja_prenda: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_espacios(cursor): # Inserta espacios
    espacio_estado_relations = {
        'Espacio': ('Disponible', 'Ocupado', 'En mantenimiento'),
    }
    
    try:
        print("Insertando espacios en la base de datos...")

        # Obtener los identificadores de las estanterías
        cursor.execute("SELECT id_estanteria, ancho_estanteria, largo_estanteria, alto_estanteria FROM estanteria;")
        estanterias = cursor.fetchall()

        # Obtener todos los id_estado relacionados con 'espacio'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN (%s, %s);", ('Disponible', 'En mantenimiento'))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        if not estado_ids:
            raise ValueError("No se encontraron estados en la tabla estado")

        for estanteria in estanterias:
            id_estanteria = estanteria[0]
            for _ in range(40):  # Insertar 40 espacios por estantería
                # Generar dimensiones aleatorias para el espacio
                ancho = round(estanteria[1]/4, 2)
                largo = round(estanteria[2], 2)
                alto = round(estanteria[3]/10, 2)

                # Obtener el último número de estanteria para este id_pasillo
                cursor.execute("SELECT MAX(id_espacio) FROM espacio WHERE id_estanteria = %s;", (id_estanteria,))

                last_shelf_number = cursor.fetchone()[0]

                if last_shelf_number is None:
                    last_shelf_number = id_estanteria * 100

                next_shelf_number = last_shelf_number + 1

                # Seleccionar un estado aleatorio
                id_estado = random.choice(estado_ids)

                # Insertar el espacio en la base de datos
                cursor.execute("INSERT INTO espacio (id_espacio, ancho, largo, alto, id_estado, id_estanteria) VALUES (%s, %s, %s, %s, %s, %s);", (next_shelf_number, ancho, largo, alto, id_estado, id_estanteria))
            
        cursor.connection.commit()
        print("Espacios insertados exitosamente\n")
    except (psycopg2.Error, ValueError) as e:
        cursor.connection.rollback()
        error = f"Error al insertar espacios: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_inspeccion_calidad(cursor): # Inserta inspección de calidad
    calidad_estado_relations = {
        'Inspeccion_calidad': ('No iniciado', 'Completado'),
    }
    try:
        print("Insertando inspección calidad en la base de datos...")
        # Obtener todos los id_estado relacionados con 'inspeccion_calidad'
        cursor.execute("SELECT id_estado, nombre FROM estado WHERE nombre IN %s;", (tuple(calidad_estado_relations['Inspeccion_calidad']),))
        estados = cursor.fetchall()
        estados_dict = {estado[0]: estado[1] for estado in estados}

        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote, cantidad FROM lote;")
        lotes = cursor.fetchall()
        lotes_data = [(lote[0], lote[1]) for lote in lotes]

        # Obtener los identificadores de los rangos de AQL
        cursor.execute("SELECT id_aql_nivel FROM aql_nivel;")
        aql_niveles = cursor.fetchall()
        ids_aql_niveles = [nivel[0] for nivel in aql_niveles]

        cursor.execute("SELECT id_aql_significancia FROM aql_significancia;")
        aql_significancias = cursor.fetchall()
        ids_aql_significancias = [significancia[0] for significancia in aql_significancias]

        # Obtener los identificadores de los resultados
        cursor.execute("SELECT id_resultado, nombre FROM resultado;")
        resultados = cursor.fetchall()
        resultados_dict = {resultado[1]: resultado[0] for resultado in resultados}

        for id_lote, cantidad_lote in random.sample(lotes_data, 100):
            fecha_inspeccion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            id_aql_nivel = random.choice(ids_aql_niveles)

            cursor.execute("""
                SELECT am.id_aql_lote_rango, am.id_aql_codigo
                FROM aql_muestra am
                INNER JOIN aql_lote_rango alr ON alr.id_aql_lote_rango = am.id_aql_lote_rango
                WHERE alr.min_lote <= %s AND %s <= alr.max_lote AND am.id_aql_nivel = %s;               
            """, (cantidad_lote, cantidad_lote, id_aql_nivel))
            aql_muestras = cursor.fetchone()
            id_aql_lote_rango, id_aql_codigo = aql_muestras

            id_aql_significancia = random.choice(ids_aql_significancias)
            cursor.execute("""
                SELECT arr.min_rechazo
                FROM aql_resultado_rango arr
                INNER JOIN aql_significancia asig ON asig.id_aql_significancia = arr.id_aql_significancia
                WHERE arr.id_aql_codigo = %s AND asig.id_aql_significancia = %s;
            """, (id_aql_codigo, id_aql_significancia))
            aql_resultado_rango = cursor.fetchone()
            min_rechazo = aql_resultado_rango[0]

            id_estado = random.choice(list(estados_dict.keys()))
            if estados_dict[id_estado] == 'Completado':
                cantidad_defectuosos = random.randint(0, 10)
                if cantidad_defectuosos >= min_rechazo:
                    id_resultado = resultados_dict['No conforme']
                else:
                    id_resultado = resultados_dict['Conforme']
                
                # Generar una descripción e insertarla en la tabla inspeccion_descripcion
                descripcion = fake.text(max_nb_chars=200)  # Generar una descripción falsa
                cursor.execute("""
                    INSERT INTO inspeccion_descripcion (descripcion)
                    VALUES (%s)
                    RETURNING id_descripcion;
                """, (descripcion,))
                id_descripcion = cursor.fetchone()[0]

            else:
                cantidad_defectuosos = None
                id_resultado = None
                id_descripcion = None

            cursor.execute("""
                INSERT INTO inspeccion_calidad (fecha_inspeccion, id_estado, cantidad_defectuosos, id_lote, 
                                                id_aql_lote_rango, id_aql_nivel, id_aql_codigo, id_aql_significancia, 
                                                id_descripcion, id_resultado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (fecha_inspeccion, id_estado, cantidad_defectuosos, id_lote, id_aql_lote_rango, id_aql_nivel,
                  id_aql_codigo, id_aql_significancia, id_descripcion, id_resultado))

        cursor.connection.commit()
        print("Inspección calidad insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar inspección calidad: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)


def insert_confeccion(cursor): # Inserta confección
    try:
        print("Insertando confección en la base de datos...")
        # Obtener los identificadores de los lotes y dimensiones de corte correspondientes
        cursor.execute("SELECT id_lote, id_dim_confeccion FROM lote WHERE id_dim_confeccion is not null;")
        lotes = cursor.fetchall()
        lotes_data = [(lote[0], lote[1]) for lote in lotes]

        # Obtener los identificadores de los empleados
        cursor.execute("SELECT id_empleado FROM empleado;")
        empleados = cursor.fetchall()
        empleados_ids = [empleado[0] for empleado in empleados]

        for id_lote, id_dim_confeccion in lotes_data: # Insertar corte para cada lote
            for _ in range(10): # Insertar corte de cada empleado
                id_empleado = random.choice(empleados_ids)
                for _ in range(random.randint(50, 100)): # Insertar de 50 a 100 registros de cpnfección
                    cursor.execute("""
                        INSERT INTO confeccion (id_lote, id_dim_confeccion, id_empleado)
                        VALUES (%s, %s, %s);
                    """, (id_lote, id_dim_confeccion, id_empleado))

        cursor.connection.commit()
        print("Confección insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar confección: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_prenda(cursor): # Inserta prenda
    try:
        print("Insertando prenda en la base de datos...")

        # Obtener los identificadores de los empleados
        cursor.execute("SELECT id_empleado FROM empleado;")
        empleados = cursor.fetchall()
        empleados_ids = [empleado[0] for empleado in empleados]

        # Obtener datos de caja_prenda
        cursor.execute("SELECT id_caja, id_dim_prenda FROM caja_prenda;")
        cajas_prenda_data = cursor.fetchall()
        cajas_prenda = [(caja[0], caja[1]) for caja in cajas_prenda_data]

        for id_caja, id_dim_prenda in cajas_prenda:
            for _ in range(5):
                id_empleado = random.choice(empleados_ids)
                for _ in range(random.randint(5, 20)):
                    cursor.execute("""
                        INSERT INTO prenda (id_dim_prenda, id_empleado, id_caja)
                        VALUES (%s, %s, %s);
                    """, (id_dim_prenda, id_empleado, id_caja))

        cursor.connection.commit()
        print("Prenda insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar prenda: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_lote_entrada(cursor): # Inserta lote de entrada
    try:
        print("Insertando Lote_entrada en la base de datos...")
        # Obtener los identificadores de los lotes
        cursor.execute("""
            SELECT l.id_lote, lt.nombre
            FROM lote l
            INNER JOIN tipo_lote lt ON lt.id_tipo_lote = l.id_tipo_lote;
        """)
        lotes= cursor.fetchall()
        lotes_dict = {lote[0]: lote[1] for lote in lotes}

        if not lotes:
            raise ValueError("No se encontraron lotes en la tabla lote")

        # Obtener todos el id_estado de 'Ocupado'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre = %s;", ('Ocupado',))
        estado = cursor.fetchall()
        ocupado_id = estado[0][0]

        # Obtener la última fecha de entrada ya registrada para comenzar desde ahí
        cursor.execute("SELECT MAX(fecha_entrada) FROM lote_entrada;")
        ultima_fecha_entrada = cursor.fetchone()[0]

        if ultima_fecha_entrada is None:
            ultima_fecha_entrada = fake.date_time_between(start_date='-2y', end_date='-1y')

        lotes_entrantes = set()

        for _ in range(200):
            # Generar una nueva fecha de entrada posterior a la última registrada
            fecha_entrada = fake.date_time_between(start_date=ultima_fecha_entrada, end_date='now')
            ultima_fecha_entrada = fecha_entrada  # Actualizar la última fecha registrada
            
            # Seleccionar un lote que no se haya utilizado todavía
            id_lote = random.choice(list(set(lotes_dict.keys()) - lotes_entrantes))
            lotes_entrantes.add(id_lote)

            if lotes_dict[id_lote] == 'Confección':
                zona = random.choice(['Confección', 'Tránsito'])
                cursor.execute(f"""
                    SELECT e.id_espacio 
                    FROM espacio e
                    INNER JOIN estanteria est ON est.id_estanteria = e.id_estanteria
                    INNER JOIN pasillo pa ON pa.id_pasillo = est.id_pasillo
                    INNER JOIN zona z ON z.id_zona = pa.id_zona
                    WHERE z.nombre = '{zona}' AND e.id_lote IS NULL;
                """)
            else:
                cursor.execute(f"""
                    SELECT e.id_espacio 
                    FROM espacio e
                    INNER JOIN estanteria est ON est.id_estanteria = e.id_estanteria
                    INNER JOIN pasillo pa ON pa.id_pasillo = est.id_pasillo
                    INNER JOIN zona z ON z.id_zona = pa.id_zona
                    WHERE z.nombre = '{lotes_dict[id_lote]}' AND e.id_lote IS NULL;
                """)
            espacios = cursor.fetchall()
            espacios_ids = [espacio[0] for espacio in espacios]

            id_espacio = random.choice(espacios_ids)

            cursor.execute("""
                INSERT INTO lote_entrada (fecha_entrada, id_lote, id_espacio)
                VALUES (%s, %s, %s);
            """, (fecha_entrada, id_lote, id_espacio))

            # Modificar el estado del lote seleccionado
            cursor.execute("""
                UPDATE espacio
                SET id_estado = %s,
                    id_lote = %s
                WHERE id_espacio = %s;
            """, (ocupado_id, id_lote, id_espacio))

        cursor.connection.commit()
        print("Lote_entrada insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar Lote_entrada: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_lote_salida(cursor): # Inserta lote de salida
    zona_area_envio = {
        'Materia prima': 'Corte',
        'Corte': 'Confección',
        'Confección': 'Almacén de tránsito'
    }
    
    try:
        print("Insertando lote salida en la base de datos...")
        # Obtener los identificadores de los lotes
        cursor.execute("""
            SELECT e.id_espacio, l.id_lote, z.nombre
            FROM espacio e
            INNER JOIN lote l ON l.id_lote = e.id_lote
            INNER JOIN estanteria est ON est.id_estanteria = e.id_estanteria
            INNER JOIN pasillo pa ON pa.id_pasillo = est.id_pasillo
            INNER JOIN zona z ON z.id_zona = pa.id_zona
            WHERE z.nombre != 'Tránsito';
        """)
        lotes = cursor.fetchall()
        lotes_dict = {lote[1]: (lote[2], lote[0]) for lote in lotes}

        # Obtener los identificadores de las áreas
        cursor.execute("SELECT id_area, nombre FROM area;")
        areas = cursor.fetchall()
        areas_dict = {area[1]: area[0] for area in areas}

        for _ in range(200):
            fecha_salida = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            id_lote = random.choice(list(lotes_dict.keys()))
            
            zona = lotes_dict.get(id_lote)[0]
            id_area_envio = areas_dict.get(zona_area_envio.get(zona))         
            
            cursor.execute("""
                INSERT INTO lote_salida (fecha_salida, id_lote, area_envio)
                VALUES (%s, %s, %s);
            """, (fecha_salida, id_lote, id_area_envio))

        cursor.connection.commit()
        print("Lote salida insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar lote salida: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_caja_lote(cursor): # Inserta caja de lote
    caja_lote_estado_relations = {
        'Caja_lote': ('Disponible', 'Usado', 'Obsoleto'),
    }

    try:
        print("Insertando caja_lote en la base de datos...")

        # Obtener los identificadores de los lotes de confección en tránsito
        cursor.execute("""
            SELECT l.id_lote
            FROM lote l
            INNER JOIN espacio e ON e.id_lote = l.id_lote
            INNER JOIN estanteria est ON est.id_estanteria = e.id_estanteria
            INNER JOIN pasillo pa ON pa.id_pasillo = est.id_pasillo
            INNER JOIN zona z ON z.id_zona = pa.id_zona
            WHERE z.nombre = 'Tránsito';
        """)
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        # Obtener todos los id_estado relacionados con 'Caja_lote'
        cursor.execute("SELECT id_estado FROM estado WHERE nombre IN %s;", (tuple(caja_lote_estado_relations['Caja_lote']),))
        estados = cursor.fetchall()
        estado_ids = [estado[0] for estado in estados]

        # Mantener un conjunto de confecciones ya actualizadas
        updated_confeccion_ids = set()

        for _ in range(200):
            cantidad = random.randint(50, 100)
            id_lote = random.choice(lotes_ids)
            id_estado = random.choice(estado_ids)

            cursor.execute("""
                INSERT INTO caja_lote (cantidad, id_lote, id_estado)
                VALUES (%s, %s, %s)
                RETURNING id_caja;
            """, (cantidad, id_lote, id_estado))
            id_caja = cursor.fetchone()[0]

             # Seleccionar una muestra de 10 confecciones relacionadas al lote elegido
            if updated_confeccion_ids:
                cursor.execute("""
                    SELECT id_confeccion 
                    FROM confeccion 
                    WHERE id_lote = %s
                    AND id_confeccion NOT IN %s
                    LIMIT 10;
                """, (id_lote, tuple(updated_confeccion_ids)))
            else:
                cursor.execute("""
                    SELECT id_confeccion 
                    FROM confeccion 
                    WHERE id_lote = %s
                    LIMIT 10;
                """, (id_lote,))
            
            confecciones = cursor.fetchall()
            confeccion_ids = [confeccion[0] for confeccion in confecciones]

            if len(confeccion_ids) == 0:
                continue

            # Actualizar id_lote de las confecciones seleccionadas
            for id_confeccion in confeccion_ids:
                cursor.execute("""
                    UPDATE confeccion
                    SET id_caja = %s
                    WHERE id_confeccion = %s;
                """, (id_caja, id_confeccion))

            # Agregar las confecciones actualizadas al conjunto
            updated_confeccion_ids.update(confeccion_ids)

        cursor.connection.commit()
        print("Caja_lote insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar caja_lote: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_registro_lote_caja(cursor): # Inserta registro de lote caja
    try:
        print("Insertando registro_lote_caja en la base de datos...")
        # Obtener los identificadores de los lotes
        cursor.execute("SELECT id_lote FROM lote;")
        lotes = cursor.fetchall()
        lotes_ids = [lote[0] for lote in lotes]

        # Obtener los identificadores de las cajas de lote
        cursor.execute("SELECT id_caja FROM caja_lote;")
        cajas_lote = cursor.fetchall()
        cajas_lote_ids = [caja[0] for caja in cajas_lote]

        registros_insertados = 0

        while registros_insertados < 50:
            id_lote = random.choice(lotes_ids)
            id_caja = random.choice(cajas_lote_ids)
            fecha_transicion = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)

            # Verificar si el registro ya existe
            cursor.execute("""
                SELECT COUNT(*) FROM registro_lote_caja
                WHERE id_lote = %s AND id_caja = %s;
            """, (id_lote, id_caja))

            existe = cursor.fetchone()[0]

            if not existe:
                cursor.execute("""
                    INSERT INTO registro_lote_caja (id_lote, id_caja, fecha_transicion)
                    VALUES (%s, %s, %s);
                """, (id_lote, id_caja, fecha_transicion))
                registros_insertados += 1

        cursor.connection.commit()
        print("Registro_lote_caja insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar registro_lote_caja: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_caja_salida(cursor): # Inserta caja de salida
    try:
        print("Insertando caja_salida en la base de datos...")
        # Obtener los identificadores de las cajas de lote
        cursor.execute("SELECT id_caja FROM caja_lote;")
        cajas_lote = cursor.fetchall()
        cajas_lote_ids = [caja[0] for caja in cajas_lote]

        # Obtener los identificadores de las áreas
        cursor.execute("SELECT id_area FROM area WHERE nombre = 'Acabado';")
        id_area = cursor.fetchone()

        cajas_entrantes = set()

        for _ in range(100):
            fecha_salida = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            id_caja = random.choice(list(set(cajas_lote_ids) - cajas_entrantes))
            cajas_entrantes.add(id_caja)

            cursor.execute("""
                INSERT INTO caja_salida (fecha_salida, id_caja, id_area)
                VALUES (%s, %s, %s);
            """, (fecha_salida, id_caja, id_area))

        cursor.connection.commit()
        print("Caja_salida insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar caja_salida: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)

def insert_registro_transformacion_caja(cursor): # Inserta registro de transformación de caja
    try:
        print("Insertando registro_transformacion_caja en la base de datos...")
        # Obtener los identificadores de las actividades diarias
        cursor.execute("SELECT id_actividad FROM actividad_diaria;")
        actividades = cursor.fetchall()
        actividades_ids = [actividad[0] for actividad in actividades]

        # Obtener los identificadores de las cajas de lote
        cursor.execute("SELECT id_caja FROM caja_lote;")
        cajas_lote = cursor.fetchall()
        cajas_lote_ids = [caja[0] for caja in cajas_lote]

        registros_insertados = 0

        while registros_insertados < 50:
            id_actividad = random.choice(actividades_ids)
            id_caja = random.choice(cajas_lote_ids)

            # Verificar si el registro ya existe
            cursor.execute("""
                SELECT COUNT(*) FROM registro_transformacion_caja
                WHERE id_actividad = %s AND id_caja = %s;
            """, (id_actividad, id_caja))

            existe = cursor.fetchone()[0]

            if not existe:
                cursor.execute("""
                    INSERT INTO registro_transformacion_caja (id_actividad, id_caja)
                    VALUES (%s, %s);
                """, (id_actividad, id_caja))
                registros_insertados += 1

        cursor.connection.commit()
        print("Registro_transformacion_caja insertados exitosamente\n")
    except psycopg2.Error as e:
        cursor.connection.rollback()
        error = f"Error al insertar registro_transformacion_caja: {e}"
        print(error)
        messagebox.showerror("Error", error)
        sys.exit(1)


def inserts8(cursor):
    insert_materia_prima(cursor)
    insert_corte(cursor)
    insert_registro_uso_lote(cursor)
    insert_caja_prenda(cursor)
    insert_espacios(cursor)
    insert_inspeccion_calidad(cursor)

def inserts9(cursor):
    insert_confeccion(cursor)
    insert_prenda(cursor)
    insert_lote_entrada(cursor)
    insert_lote_salida(cursor)
    insert_caja_lote(cursor)
    insert_registro_lote_caja(cursor)
    insert_caja_salida(cursor)
    insert_registro_transformacion_caja(cursor)


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
        inserts8(cursor)
        inserts9(cursor)
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
