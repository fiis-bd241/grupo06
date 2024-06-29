from django.http import JsonResponse
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class InspeccionesAPIView(APIView):

    def get(self, request, *args, **kwargs):
        id_orden_produccion = request.query_params.get('id_orden_produccion', None)
        query = """
            SELECT
                OP.ID_ORDEN_PRODUCCION,
                I.ID_INSPECCION,
                I.ID_LOTE,
                I.FECHA_INSPECCION,
                I.CANTIDAD_DEFECTUOSOS,
                I.ID_AQL_CODIGO,
                AN.NOMBRE,
                AS.NIVEL_SIGNIFICANCIA,
                E.NOMBRE,
                R.NOMBRE
            FROM INSPECCION_CALIDAD I
            JOIN LOTE LT ON I.ID_LOTE = LT.ID_LOTE
            JOIN ACTIVIDAD_DIARIA AD ON LT.ID_ACTIVIDAD = AD.ID_ACTIVIDAD
            JOIN ORDEN_PRODUCCION OP ON AD.ID_ORDEN_PRODUCCION = OP.ID_ORDEN_PRODUCCION
            JOIN AQL_NIVEL AN ON AN.ID_AQL_NIVEL = I.ID_AQL_NIVEL
            JOIN AQL_NIVEL_SIGNIFICANCIA AS ON AS.ID_NIVEL_SIGNIFICANCIA = I.ID_NIVEL_SIGNIFICANCIA
            JOIN ESTADO E ON E.ID_ESTADO = I.ID_ESTADO
            JOIN RESULTADO R ON R.ID_RESULTADO = I.ID_RESULTADO
            JOIN AQL_RESULTADO_RANGO ARS ON ARS.ID_AQL_CODIGO = I.ID_AQL_CODIGO
        """
        if id_orden_produccion is not None:
            query += " WHERE OP.ID_ORDEN_PRODUCCION = %s"
            query_params = [id_orden_produccion]
        else:
            query_params = []

        query += " ORDER BY OP.ID_ORDEN_PRODUCCION DESC"

        with connection.cursor() as cursor:
            cursor.execute(query, query_params)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in rows]

        return JsonResponse(results, safe=False)

    def post(self, request, *args, **kwargs):
        data = request.data
        id_inspeccion = data.get('id_inspeccion')
        cantidad_defectuosos = data.get('cantidad_defectuosos')

        if not id_inspeccion or cantidad_defectuosos is None:
            return Response({"error": "Datos incompletos"}, status=status.HTTP_400_BAD_REQUEST)

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT ARS.MAX_ACEPTACION
                FROM INSPECCION_CALIDAD I
                JOIN AQL_RESULTADO_RANGO ARS ON ARS.ID_AQL_CODIGO = I.ID_AQL_CODIGO
                WHERE I.ID_INSPECCION = %s
            """, [id_inspeccion])
            max_aceptacion = cursor.fetchone()[0]

            id_resultado = 0 if cantidad_defectuosos < max_aceptacion else 1

            cursor.execute("""
                UPDATE INSPECCION_CALIDAD
                SET CANTIDAD_DEFECTUOSOS = %s, ID_ESTADO = 1, ID_RESULTADO = %s
                WHERE ID_INSPECCION = %s
            """, [cantidad_defectuosos, id_resultado, id_inspeccion])

        return Response({"message": "Inspección actualizada correctamente"}, status=status.HTTP_200_OK)
