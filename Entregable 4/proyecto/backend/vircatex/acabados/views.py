from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import *

@api_view(['GET'])
def acabado_list(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM acabado")
            results = cursor.fetchall()

            # Extraer los nombres de las columnas
            columns = [col[0] for col in cursor.description]

            # Convertir los resultados en una lista de diccionarios
            acabados = [dict(zip(columns, row)) for row in results]

        return Response(acabados)
    except Exception as e:
        return Response({"error": str(e)})  # Manejo básico de errores para devolver detalles del error