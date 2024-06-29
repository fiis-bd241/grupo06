from django.http import JsonResponse
from django.views import View
from django.db import connection
from core.models import *

from django.views.decorators.csrf import csrf_exempt
import json


#para la primera y segunda pantalla, donde es la orden de produccion y luego de apretar asignar
class OrdenesListView(View):
    def get(self, request):
        with connection.cursor() as cursor:
            query = """
            SELECT
                o.id_orden_producción,
                o.fecha_inicio,
                o.fecha_fin,
                o.cantidad,
                e.nombre AS estado_orden,
                a.nombre AS area,
                tc.nombre AS tipo_corte,
                tmp.nombre AS tipo_materia_prima,
                o.id_orden_trabajo,
                o.fecha_creacion
            FROM
                orden_producción o
            JOIN
                estado e ON o.id_estado = e.id_estado
            JOIN
                area a ON o.id_area = a.id_area
            JOIN
                dimension_corte dc ON o.id_dim_corte = dc.id_dim_corte
            JOIN
                parte_corte_detalle pcd ON dc.id_dim_parte_prenda = pcd.id_dim_parte_prenda
            JOIN
                tipo_corte tc ON pcd.id_tipo_corte = tc.id_tipo_corte
            JOIN
                actividad_diaria ad ON o.id_orden_producción = ad.id_orden_producción
            JOIN
                registro_uso_lote rul ON ad.id_actividad = rul.id_actividad
            JOIN
                lote l ON rul.id_lote = l.id_lote
            JOIN
                dimension_materia_prima dmp ON l.id_dim_materia_prima = dmp.id_dim_materia_prima
            JOIN
                tipo_materia_prima tmp ON dmp.id_tipo_materia_prima = tmp.id_tipo_materia_prima
            WHERE
                a.nombre = 'Corte'
            GROUP BY
                o.id_orden_producción, o.fecha_inicio, o.fecha_fin, o.cantidad, e.nombre, a.nombre, tc.nombre, tmp.nombre,
                o.id_orden_trabajo, o.fecha_creacion
            ORDER BY
                o.fecha_inicio DESC;
            """
            cursor.execute(query)
            rows = cursor.fetchall()

        data = [
            {
                'id_orden_produccion': row[0],
                'fecha_inicio': row[1],
                'fecha_fin': row[2],
                'cantidad': row[3],
                'estado_orden': row[4],
                'area': row[5],
                'tipo_corte': row[6],
                'tipo_materia_prima': row[7],
                'id_orden_trabajo': row[8],
                'fecha_creacion': row[9]
            }
            for row in rows
        ]
        return JsonResponse(data, safe=False)

class AsignarView(View):
    def post(self, request, id_orden_produccion):
        body = json.loads(request.body)
        id_maquina = body['id_maquina']
        cantidad_hecha = body['cantidad_hecha']

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO actividad_diaria (fecha_actividad, id_orden_producción) VALUES (NOW(), %s) RETURNING id_actividad;",
                [id_orden_produccion]
            )
            id_actividad = cursor.fetchone()[0]

            cursor.execute(
                "INSERT INTO maquina_actividad (id_actividad, id_maquina, cantidad_hecha) VALUES (%s, %s, %s);",
                [id_actividad, id_maquina, cantidad_hecha]
            )

        return JsonResponse({'status': 'success'})
    

#para la tercera pantalla actividades que debe realizar cada maquina al dia (operario)

def actividad_diaria(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                a.fecha_actividad,
                o.id_orden_producción,
                o.cantidad AS cantidad_orden,
                m.id_maquina,
                ma.cantidad_hecha AS cantidad_realizar,
                tc.nombre AS tipo_corte
            FROM actividad_diaria a
            JOIN maquina_actividad ma ON a.id_actividad = ma.id_actividad
            JOIN maquina m ON ma.id_maquina = m.id_maquina
            JOIN orden_producción o ON a.id_orden_producción = o.id_orden_producción
            JOIN corte c ON c.id_lote = o.id_dim_corte
            JOIN dimension_corte dc ON c.id_dim_corte = dc.id_dim_corte
            JOIN parte_corte_detalle pcd ON dc.id_dim_parte_prenda = pcd.id_dim_parte_prenda
            JOIN tipo_corte tc ON pcd.id_tipo_corte = tc.id_tipo_corte
            ORDER BY a.fecha_actividad DESC;
        """)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]
    
    return JsonResponse(results, safe=False)

#para la cuarta pantalla, inserta datos de la cantidad de corte realizado y la cantidad de lote usado (operario)
@csrf_exempt
def insertar_datos(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        id_tipo_lote = 2  # el valor constante como especificaste
        cantidad = data.get('cantidad')
        id_dim_corte = data.get('id_dim_corte')
        id_estado = data.get('id_estado')
        id_actividad = data.get('id_actividad')
        fecha_creacion = data.get('fecha_creacion')
        cantidad_usada = data.get('cantidad_usada')
        
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                INSERT INTO lote (id_tipo_lote, cantidad, id_dim_corte, id_estado, id_dim_confeccion, id_dim_materia_prima, id_actividad, fecha_creacion)
                VALUES (%s, %s, %s, %s, NULL, NULL, %s, %s) RETURNING id;
                ''',
                [id_tipo_lote, cantidad, id_dim_corte, id_estado, id_actividad, fecha_creacion]
            )
            id_lote = cursor.fetchone()[0]
            
            cursor.execute(
                '''
                INSERT INTO Registro_uso_lote (id_actividad, id_lote, cantidad_usada)
                VALUES (%s, %s, %s);
                ''',
                [id_actividad, id_lote, cantidad_usada]
            )
        
        return JsonResponse({'success': True, 'id_lote': id_lote})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


#para la quinta (actividades diarias por maquina)y sexta pantalla depues de apretar ver actividad se muestra el detalle de la actividad

def actividades(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                ma.id_maquina,
                m.capacidad_total,
                COUNT(ad.id_actividad) AS cantidad_actividades,
                ad.fecha_actividad
            FROM 
                actividad_diaria ad
            JOIN 
                maquina_actividad ma ON ad.id_actividad = ma.id_actividad
            JOIN 
                maquina m ON ma.id_maquina = m.id_maquina
            WHERE 
                ad.fecha_actividad = '2024-06-03'
            GROUP BY 
                ma.id_maquina, m.capacidad_total, ad.fecha_actividad
            ORDER BY 
                cantidad_actividades DESC;
        """)
        rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            'id_maquina': row[0],
            'capacidad_total': row[1],
            'cantidad_actividades': row[2],
            'fecha_actividad': row[3],
        })

    return JsonResponse(data, safe=False)

def actividad_detalle(request, actividad_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                ad.id_actividad,
                ad.fecha_actividad,
                COUNT(c.id_corte) AS cantidad_cortes,
                op.cantidad AS cantidad_orden_preproduccion,
                (SUM(l.cantidad) / op.cantidad) * 100 AS progreso_preproduccion
            FROM actividad_diaria ad
            JOIN orden_producción op ON ad.id_orden_producción = op.id_orden_producción
            JOIN lote l ON ad.id_actividad = l.id_actividad
            JOIN corte c ON l.id_lote = c.id_lote
            WHERE ad.id_actividad = %s
            GROUP BY
                ad.id_actividad,
                ad.fecha_actividad,
                op.cantidad
            ORDER BY
                ad.fecha_actividad DESC;
        """, [actividad_id])
        row = cursor.fetchone()

    data = {
        'id_actividad': row[0],
        'fecha_actividad': row[1],
        'cantidad_cortes': row[2],
        'cantidad_orden_preproduccion': row[3],
        'progreso_preproduccion': row[4],
    }

    return JsonResponse(data)


#para la septima pantalla, numero de lotes por dia en el mes

class LotesView(View):
    def get(self, request):
        query = """
            SELECT 
                l.fecha_creacion::date AS dia,
                COUNT(l.id_lote) AS cantidad_lotes
            FROM 
                lote l
            JOIN 
                actividad_diaria ad ON l.id_actividad = ad.id_actividad
            JOIN 
                orden_producción op ON ad.id_orden_producción = op.id_orden_producción
            JOIN 
                area a ON op.id_area = a.id_area
            WHERE 
                a.nombre = 'Corte'
                AND DATE_TRUNC('month', l.fecha_creacion) = DATE_TRUNC('month', CURRENT_DATE)
            GROUP BY 
                l.fecha_creacion::date
            ORDER BY 
                dia DESC;
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        data = [{'dia': row[0], 'cantidad_lotes': row[1]} for row in rows]
        return JsonResponse(data, safe=False)
    
# para la octava pantalla, numero de cortes por el orden de produccion 
class ProductionOrderView(View):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    op.id_orden_producción,
                    op.cantidad,
                    l.id_lote,
                    l.cantidad AS cantidad_lote,
                    tc.nombre AS tipo_corte,
                    COUNT(c.id_corte) AS cantidad_cortes,
                    e.nombre AS estado_orden,
                    (SELECT
                        (SUM(l2.cantidad) / op.cantidad) * 100
                     FROM lote l2
                     INNER JOIN corte c2 ON l2.id_lote = c2.id_lote
                     INNER JOIN orden_producción op2 ON op2.id_dim_corte = c2.id_dim_corte
                     WHERE op2.id_orden_producción = op.id_orden_producción) AS progreso_produccion
                FROM orden_producción op
                INNER JOIN estado e ON op.id_estado = e.id_estado
                INNER JOIN dimension_corte dc ON op.id_dim_corte = dc.id_dim_corte
                INNER JOIN corte c ON dc.id_dim_corte = c.id_dim_corte
                INNER JOIN lote l ON c.id_lote = l.id_lote
                INNER JOIN parte_corte_detalle pcd ON dc.id_dim_parte_prenda = pcd.id_dim_parte_prenda
                INNER JOIN tipo_corte tc ON pcd.id_tipo_corte = tc.id_tipo_corte
                GROUP BY
                    op.id_orden_producción,
                    op.cantidad,
                    l.id_lote,
                    l.cantidad,
                    tc.nombre,
                    e.nombre
                ORDER BY
                    op.id_orden_producción,
                    tc.nombre,
                    cantidad_cortes DESC;
            """)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in rows]

        return JsonResponse(data, safe=False)
