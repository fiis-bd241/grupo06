"""
URL configuration for vircatex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from acabados.views import *
from almacen_central.views import *
from almacen_transito.views import *
from calidad.views import *
from confeccion.views import *
from corte.views import *
from pcp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("acabado/", acabado_list, name="acabado_list"),
    path('ordenes-produccion-confeccion/', OrdenesProduccionConfView.as_view(), name='ordenes-produccion-confeccion'),
    path('descripcion-confeccion/<int:id_orden_produccion>/', DescripcionConfeccionView.as_view(), name='descripcion-confeccion'),
    path('empleados-confeccion/', EmpleadosConfView.as_view(), name='empleados-confeccion'),
    path('asignar-empleado-confeccion/', AsignarEmpleadoConfView.as_view(), name='asignar-empleado-confeccion'),
    path('ordenes-confeccion-asignadas-hoy/', OrdenesConfAsignadasEmplView.as_view(), name='ordenes-confeccion-asignadas-hoy'),
    path('lista-empleados-confeccion/', EmpleadosConfRegistroView.as_view(), name='ordenes-asignadas-hoy'),
    path('ordenes-confeccion-empleado/', OrdenesConfEmplView.as_view(), name='ordenes-confeccion-empleado'),
    path('actualizar-cantidad/', ActualizarCantidadView.as_view(), name='actualizar-cantidad'),
    path('lotes-corte-empleado/', LotesCorteEmPView.as_view(), name='lotes-corte-empleado'),
    path('insertar-consumo-lote-corte/', InsertarConsumoLoteCutView.as_view(), name='insertar-consumo-lote-corte'),

]
