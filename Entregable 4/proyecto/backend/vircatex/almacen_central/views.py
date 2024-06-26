from django.http import JsonResponse
from django.db import connection
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser


class LoteListView(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        estado = data.get('estado', None)
        tipo_materia_prima = data.get('tipo_materia_prima', None)
        query = """
            SELECT    
                l.id_lote, 
                p.denominacion_social,
                e.id_espacio,
                le.fecha_entrada,
                tmp.nombre as tipo_materia_prima
            FROM lote l
            JOIN materia_prima mp ON l.id_lote = mp.id_lote
            JOIN proveedor p on mp.id_proveedor = p.id_proveedor
            JOIN espacio e on l.id_lote = e.id_lote
            JOIN lote_entrada le on l.id_lote = le.id_lote
            join estado e2 on l.id_estado = e2.id_estado
            join dimension_materia_prima dmp on mp.id_dim_materia_prima = dmp.id_dim_materia_prima
            join tipo_materia_prima tmp ON dmp.id_tipo_materia_prima =tmp.id_tipo_materia_prima 
            WHERE e2.nombre = %s
        """
        params = [estado]
        if tipo_materia_prima is not None:
            query += " AND tmp.nombre = %s"
            params.append(tipo_materia_prima)
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            result = []
            for row in rows:
                result.append({
                    'id_lote': row[0],
                    'denominacion_social': row[1],
                    'id_espacio': row[2],
                    'fecha_entrada': row[3],
                    'tipo_materia_prima': row[4],
                })
        return JsonResponse(result, safe=False)

class LotesEntreFechasView(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin', None)
        with connection.cursor() as cursor:
            cursor.callproc('get_lotes_entre_fechas', [fecha_inicio, fecha_fin])
            rows = cursor.fetchall()
            result = []
            for row in rows:
                result.append({
                    'fecha_entrada': row[0],
                    'id_lote': row[1],
                    'id_estanteria': row[2],
                    'id_espacio': row[3],
                    'denominacion_social': row[4],
                    'id_materia_prima': row[5],
                })
        return JsonResponse(result, safe=False)

class ProveedorMateriaPrimaView(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        denominacion_social = data.get('denominacion_social', None)
        nombre = data.get('nombre', None)
        query = """
            SELECT 
                tmp.nombre AS materia_prima,
                p.denominacion_social AS proveedor,
                COUNT(*) AS cantidad_lotes
            FROM 
                proveedor p
            JOIN materia_prima mp ON p.id_proveedor = mp.id_proveedor
            join lote l ON mp.id_lote = l.id_lote
            JOIN dimension_materia_prima dmp on mp.id_dim_materia_prima = dmp.id_dim_materia_prima
            JOIN tipo_materia_prima tmp ON dmp.id_tipo_materia_prima =tmp.id_tipo_materia_prima
            WHERE 
                l.id_estado = 12
        """
        params = []
        if denominacion_social is not None:
            query += " AND p.denominacion_social = %s"
            params.append(denominacion_social)
        if nombre is not None:
            query += " AND tmp.nombre = %s"
            params.append(nombre)
        query += """
            GROUP BY 
                tmp.nombre, 
                p.denominacion_social;
        """
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            result = []
            for row in rows:
                result.append({
                    'materia_prima': row[0],
                    'proveedor': row[1],
                    'cantidad_lotes': row[2],
                })
        return JsonResponse(result, safe=False)

class LotesEntradaView(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        fecha_entrada = data.get('fecha_entrada')
        nombre_material = data.get('nombre_material', None)
        nombre_proveedor = data.get('nombre_proveedor', None)
        query = """
            SELECT 
                le.fecha_entrada, 
                l.id_lote, 
                tmp.nombre AS nombre_material, 
                p.denominacion_social AS nombre_proveedor, 
                l.cantidad 
            FROM lote_entrada le 
            JOIN lote l ON le.id_lote = l.id_lote 
            JOIN materia_prima mp ON l.id_lote = mp.id_lote 
            JOIN dimension_materia_prima dmp ON mp.id_dim_materia_prima = dmp.id_dim_materia_prima 
            JOIN tipo_materia_prima tmp ON dmp.id_tipo_materia_prima = tmp.id_tipo_materia_prima 
            JOIN proveedor p ON mp.id_proveedor = p.id_proveedor 
            WHERE DATE(le.fecha_entrada) = DATE(%s)
        """
        params = [fecha_entrada]
        if nombre_material is not None:
            query += " AND tmp.nombre = %s"
            params.append(nombre_material)
        if nombre_proveedor is not None:
            query += " AND p.denominacion_social = %s"
            params.append(nombre_proveedor)
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            result = []
            for row in rows:
                result.append({
                    'fecha_entrada': row[0],
                    'id_lote': row[1],
                    'nombre_material': row[2],
                    'nombre_proveedor': row[3],
                    'cantidad': row[4],
                })
        return JsonResponse(result, safe=False)

class LotesSalidaView(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        fecha_salida = data.get('fecha_salida')
        nombre_material = data.get('nombre_material', None)
        nombre_proveedor = data.get('nombre_proveedor', None)
        query = """
            SELECT
                ls.fecha_salida,
                l.id_lote,
                tmp.nombre AS nombre_material,
                p.denominacion_social AS nombre_proveedor,
                l.cantidad,
                a.nombre AS nombre_area
            FROM lote_salida ls
            JOIN lote l ON ls.id_lote = l.id_lote
            JOIN materia_prima mp ON l.id_lote = mp.id_lote
            JOIN dimension_materia_prima dmp ON mp.id_dim_materia_prima = dmp.id_dim_materia_prima
            JOIN tipo_materia_prima tmp ON dmp.id_tipo_materia_prima = tmp.id_tipo_materia_prima
            JOIN proveedor p ON mp.id_proveedor = p.id_proveedor
            JOIN area a ON ls.area_envio = a.id_area
            WHERE DATE(ls.fecha_salida) = DATE(%s)
        """
        params = [fecha_salida]
        if nombre_material is not None:
            query += " AND tmp.nombre = %s"
            params.append(nombre_material)
        if nombre_proveedor is not None:
            query += " AND p.denominacion_social = %s"
            params.append(nombre_proveedor)
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            result = []
            for row in rows:
                result.append({
                    'fecha_salida': row[0],
                    'id_lote': row[1],
                    'nombre_material': row[2],
                    'nombre_proveedor': row[3],
                    'cantidad': row[4],
                    'nombre_area': row[5],
                })
        return JsonResponse(result, safe=False)

class CrearProveedorView(APIView):
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        _descripcion_direccion = data.get('_descripcion_direccion')
        _direccion_correo = data.get('_direccion_correo')
        _numero_telefono = data.get('_numero_telefono')
        _ruc = data.get('_ruc')
        _denominacion_social = data.get('_denominacion_social')
        with connection.cursor() as cursor:
            cursor.execute("CALL crear_proveedor(%s, %s, %s, %s, %s)", [_descripcion_direccion, _direccion_correo, _numero_telefono, _ruc, _denominacion_social])
        return JsonResponse({"message": "Proveedor creado exitosamente"}, status=201)
