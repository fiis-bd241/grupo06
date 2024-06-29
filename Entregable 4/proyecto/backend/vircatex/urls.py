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
from django.urls import path, include
from acabados.views import *
from almacen_central.views import *
from almacen_transito.views import *
from calidad.views import *
from confeccion.views import *
from corte.views import *
from pcp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # acabados
    path('acabados/', include([
        path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
        path('datosa/', DatosListAView.as_view(), name='datos_list_a'),
        path('reporte/', ReporteAcabadosView.as_view(), name='reporte_acabados'),
        path('acabados/', AcabadoListView.as_view(), name='acabados-list'),
        path('lote-entrada-vista/', LoteEntradaVista.as_view(), name='lote-entrada-vista'),
    ])),

    # almacen central
    path('almacen_central/', include([
        path('almacen_central/lotes/', LoteListView.as_view(), name='lote-list'),
        path('almacen_central/lotes_entre_fechas/', LotesEntreFechasView.as_view()),
        path('almacen_central/proveedor_materia_prima/', ProveedorMateriaPrimaView.as_view()),
        path('almacen_central/lote_entrada/', LotesEntradaView.as_view()),
        path('almacen_central/lote_salida/', LotesSalidaView.as_view()),
        path('almacen_central/proveedor/crear_o_modificar/', CrearProveedorView.as_view()),
        path('almacen_central/proveedor/eliminar/<str:ruc>/', EliminarProveedorView.as_view()),
        path('almacen_central/lote/crear/', CrearLoteView.as_view()),
        path('almacen_central/lote_entrada/crear/', CrearLoteEntradaView.as_view()),
        path('almacen_central/lote_salida/mover/', MoverLoteSalidaView.as_view()),
    ])),

    # almacen de tránsito
    path('almacen_transito/', include([

    ])),

    # calidad
    path('calidad/', include([

    ])),
    
    # confección
    path('confeccion/', include([
        path('ordenes-produccion/', OrdProdConfView.as_view(), name='ord-prod-conf'),
        path('descripcion/<int:id_orden_produccion>/', DescConfView.as_view(), name='desc-conf'),
        path('empleados/', EmpConfView.as_view(), name='empleados-confeccion'),
        path('asignar-empleado/', AsigEmpConfView.as_view(), name='asignar-emp-conf'),
        path('ordenes-asignadas/<int:id_empleado>/', OrdConfAsigdasEmplView.as_view(), name='ord-conf-asigdas-empl'),
        path('empleados-ordenes-asignadas/', EmpConfRegView.as_view(), name='emp-ord-asigdas'),
        path('ordenes-empleado/<int:id_empleado>/', OrdConfEmpView.as_view(), name='ord-conf-emp'),
        path('actualizar-cantidad/', ActCantView.as_view(), name='act-cant'),
        path('lotes-corte-empleado/<int:id_empleado>/', LtsCteEmpView.as_view(), name='lts-cte-emp'),
        path('insertar-consumo-lote-corte/', InsConsLteCteView.as_view(), name='ins-cons-lte-cte'),
    ])),

    # corte
    path('corte/', include([

    ])),

    # pcp
    path('pcp/', include([

    ])),
    
]
