from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import *

from rest_framework.views import APIView
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from datetime import datetime

# Orden Confeccion 1
@method_decorator(csrf_exempt, name='dispatch')
class OrdenesProduccionConfView(APIView):
    def get(self, request):
        # Leer el cuerpo de la solicitud como JSON
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return Response({"error": "Cuerpo de solicitud no válido"}, status=400)
        
        estado = body.get('estado', None)
        fecha_inicio = body.get('fecha_inicio', None)
        fecha_fin = body.get('fecha_fin', None)
        
        # Validar el estado si se proporciona
        if estado and estado not in ['No iniciado', 'En proceso', 'Atrasado']:
            return Response({"error": "Estado no válido"}, status=400)
        
        # Validar y parsear fechas si se proporcionan
        if fecha_inicio:
            fecha_inicio = parse_date(fecha_inicio)
            if not fecha_inicio:
                return Response({"error": "Fecha de inicio no válida"}, status=400)
        
        if fecha_fin:
            fecha_fin = parse_date(fecha_fin)
            if not fecha_fin:
                return Response({"error": "Fecha de fin no válida"}, status=400)
        
        # Construir el query con filtros dinámicos
        query = "SELECT * FROM vista_op_confección WHERE 1=1"
        params = []
        
        if estado:
            query += " AND estado = %s"
            params.append(estado)
        
        if fecha_inicio:
            query += " AND fecha_inicio >= %s"
            params.append(fecha_inicio)
        
        if fecha_fin:
            query += " AND fecha_fin <= %s"
            params.append(fecha_fin)
        
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
        
        # Convert the rows into a list of dictionaries
        results = [dict(zip(columns, row)) for row in rows]
        return Response(results)

# Orden Confección 2, Ordenes asignadas 2 y Registro de progreso 3
@method_decorator(csrf_exempt, name='dispatch')
class DescripcionConfeccionView(APIView):
    def get(self, request, id_orden_produccion):
        query = "SELECT * FROM vista_op_conf_descripción WHERE id_orden_producción = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, [id_orden_produccion])
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
        
        # Convert the rows into a list of dictionaries
        results = [dict(zip(columns, row)) for row in rows]
        return Response(results)

# Orden Confección 3
@method_decorator(csrf_exempt, name='dispatch')
class EmpleadosConfView(APIView):
    def get(self, request):
        # Leer el cuerpo de la solicitud como JSON
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return Response({"error": "Cuerpo de solicitud no válido"}, status=400)

        nombre = body.get('nombre', None)
        primer_apellido = body.get('primer_apellido', None)
        segundo_apellido = body.get('segundo_apellido', None)

        # Construir el query con filtros dinámicos
        query = "SELECT * FROM vista_emp_confección WHERE 1=1"
        params = []

        if nombre:
            query += " AND nombre = %s"
            params.append(nombre)

        if primer_apellido:
            query += " AND primer_apellido = %s"
            params.append(primer_apellido)

        if segundo_apellido:
            query += " AND segundo_apellido = %s"
            params.append(segundo_apellido)

        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]

        # Convert the rows into a list of dictionaries
        results = [dict(zip(columns, row)) for row in rows]
        return Response(results)

# Orden Confección 3
@method_decorator(csrf_exempt, name='dispatch')
class AsignarEmpleadoConfView(APIView):
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return Response({"error": "Cuerpo de solicitud no válido"}, status=400)

        id_empleado = body.get('id_empleado', None)
        id_orden_produccion = body.get('id_orden_produccion', None)

        if not id_empleado or not id_orden_produccion:
            return Response({"error": "Faltan parámetros"}, status=400)

        fecha_actual = datetime.today().strftime('%Y-%m-%d')

        try:
            with connection.cursor() as cursor:
                # Insertar en actividad_diaria si es necesario
                cursor.execute("""
                    INSERT INTO actividad_diaria (fecha_actividad, id_orden_producción)
                    VALUES (%s, %s)
                    ON CONFLICT (fecha_actividad, id_orden_producción) DO NOTHING
                """, [fecha_actual, id_orden_produccion])
                
                # Obtener el id_actividad recién insertado o existente
                cursor.execute("""
                    SELECT id
                    FROM actividad_diaria
                    WHERE fecha_actividad = %s AND id_orden_producción = %s
                """, [fecha_actual, id_orden_produccion])
                id_actividad = cursor.fetchone()[0]
                
                # Insertar en empleado_actividad
                cursor.execute("""
                    INSERT INTO empleado_actividad (id_empleado, id_actividad, cantidad_hecha)
                    VALUES (%s, %s, %s)
                """, [id_empleado, id_actividad, 0])

            return Response({"success": "Empleado asignado correctamente"}, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

# Ordenes Asignadas 1
@method_decorator(csrf_exempt, name='dispatch')
class OrdenesConfAsignadasEmplView(APIView):
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return Response({"error": "Cuerpo de solicitud no válido"}, status=400)

        id_empleado = body.get('id_empleado', None)

        if not id_empleado:
            return Response({"error": "Faltan parámetros"}, status=400)

        #fecha_actual = datetime.today().strftime('%Y-%m-%d')
        fecha_actual = '19/04/2024'

        try:
            with connection.cursor() as cursor:
                query = """
                    SELECT id_orden_producción
                    FROM vista_op_emp_conf
                    WHERE id_empleado = %s AND fecha_actividad = %s
                """
                cursor.execute(query, [id_empleado, fecha_actual])
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]

            # Convert the rows into a list of dictionaries
            results = [dict(zip(columns, row)) for row in rows]
            return Response(results)

        except Exception as e:
            return Response({"error": str(e)}, status=500)

# Registro de progreso 1
@method_decorator(csrf_exempt, name='dispatch')
class EmpleadosConfRegistroView(APIView):
    def get(self, request):
        # Leer el cuerpo de la solicitud como JSON
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return Response({"error": "Cuerpo de solicitud no válido"}, status=400)

        nombre = body.get('nombre', None)
        primer_apellido = body.get('primer_apellido', None)
        segundo_apellido = body.get('segundo_apellido', None)

        # Obtener la fecha actual
        #fecha_actual = datetime.today().strftime('%Y-%m-%d')
        fecha_actual = '19/04/2024'
        
        # Construir el query con filtros dinámicos
        query = """
            SELECT id_empleado, nombre, primer_apellido, segundo_apellido,
                   COUNT(id_actividad) AS ordenes
            FROM vista_emp_ops_confección
            WHERE fecha_actividad = %s
            GROUP BY id_empleado, nombre, primer_apellido, segundo_apellido
        """
        having_clauses = []
        params = [fecha_actual]

        if nombre:
            having_clauses.append("nombre = %s")
            params.append(nombre)

        if primer_apellido:
            having_clauses.append("primer_apellido = %s")
            params.append(primer_apellido)

        if segundo_apellido:
            having_clauses.append("segundo_apellido = %s")
            params.append(segundo_apellido)

        if having_clauses:
            query += " HAVING " + " AND ".join(having_clauses)

        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]

        # Convertir las filas en una lista de diccionarios
        results = [dict(zip(columns, row)) for row in rows]
        return Response(results)

# Registro de progreso 2
@method_decorator(csrf_exempt, name='dispatch')
class OrdenesConfEmplView(APIView):
    def get(self, request):
        # Leer el cuerpo de la solicitud como JSON
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return Response({"error": "Cuerpo de solicitud no válido"}, status=400)

        id_empleado = body.get('id_empleado', None)

        if not id_empleado:
            return Response({"error": "ID de empleado es requerido"}, status=400)

        # Obtener la fecha actual
        #fecha_actual = datetime.today().strftime('%Y-%m-%d')
        fecha_actual = '19/04/2024'

        # Construir el query para obtener las órdenes de producción
        query = """
            SELECT id_orden_producción
            FROM vista_emp_ops_confección
            WHERE fecha_actividad = %s AND id_empleado = %s
        """
        params = [fecha_actual, id_empleado]

        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]

        # Convertir las filas en una lista de diccionarios
        results = [dict(zip(columns, row)) for row in rows]
        return Response(results)

# Registro de progreso 2
@method_decorator(csrf_exempt, name='dispatch')
class ActualizarCantidadView(APIView):
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return Response({"error": "Cuerpo de solicitud no válido"}, status=400)

        id_empleado = body.get('id_empleado')
        id_orden_producción = body.get('id_orden_producción')
        cantidad_hecha = body.get('cantidad_hecha')

        if not all([id_empleado, id_orden_producción, cantidad_hecha]):
            return Response({"error": "Datos incompletos"}, status=400)

        #fecha_actual = datetime.today().strftime('%Y-%m-%d')
        fecha_actual = '19/04/2024'

        query = """
            UPDATE empleado_actividad
            SET cantidad_hecha = %s
            WHERE id_empleado = %s 
                  AND id_actividad = (
                      SELECT id_actividad
                      FROM vista_emp_ops_confección
                      WHERE fecha_actividad = %s 
                        AND id_empleado = %s 
                        AND id_orden_producción = %s
                  )
        """
        params = [cantidad_hecha, id_empleado, fecha_actual, id_empleado, id_orden_producción]

        with connection.cursor() as cursor:
            cursor.execute(query, params)

        return Response({"status": "Cantidad actualizada correctamente"})

# Registro de progreso 4
@method_decorator(csrf_exempt, name='dispatch')
class LotesCorteEmPView(APIView):
    def get(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return Response({"error": "Cuerpo de solicitud no válido"}, status=400)

        id_empleado = body.get('id_empleado', None)

        if not id_empleado:
            return Response({"error": "ID de empleado es requerido"}, status=400)

        #fecha_actual = datetime.today().strftime('%Y-%m-%d')
        fecha_actual = '19/04/2024'

        query = """
            SELECT id_lote
            FROM vista_lote_corte_emp
            WHERE id_orden_producción IN (
                SELECT id_orden_producción
                FROM vista_emp_ops_confección
                WHERE fecha_actividad = %s AND id_empleado = %s
            )
        """
        params = [fecha_actual, id_empleado]

        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]

        results = [dict(zip(columns, row)) for row in rows]
        return Response(results)
    
@method_decorator(csrf_exempt, name='dispatch')
class InsertarConsumoLoteCutView(APIView):
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return Response({"error": "Cuerpo de solicitud no válido"}, status=400)

        id_empleado = body.get('id_empleado')
        id_orden_producción = body.get('id_orden_producción')
        id_lote = body.get('id_lote')
        cantidad_usada = body.get('cantidad_usada')

        if not all([id_empleado, id_orden_producción, id_lote, cantidad_usada]):
            return Response({"error": "Datos incompletos"}, status=400)

        fecha_actual = datetime.today().strftime('%Y-%m-%d')

        query = """
            INSERT INTO registro_uso_lote (id_actividad, id_lote, cantidad_usada)
            VALUES (
                (SELECT id_actividad
                 FROM vista_emp_ops_confección
                 WHERE fecha_actividad = %s 
                   AND id_empleado = %s 
                   AND id_orden_producción = %s),
                %s,
                %s
            )
        """
        params = [fecha_actual, id_empleado, id_orden_producción, id_lote, cantidad_usada]

        with connection.cursor() as cursor:
            cursor.execute(query, params)

        return Response({"status": "Consumo de lote registrado correctamente"})