from django.urls import path
from . import views
from .views import LotesEntreFechasView, ProveedorMateriaPrimaView, CrearProveedorView

urlpatterns = [
    path('lotes/', views.LoteListView.as_view(), name='lote-list'),
    path('lotes_entre_fechas/', LotesEntreFechasView.as_view()),
    path('proveedor_materia_prima/', ProveedorMateriaPrimaView.as_view()),
    path('lote_entrada/', views.LotesEntradaView.as_view()),
    path('lote_salida/', views.LotesSalidaView.as_view()),
    path('crear_proveedor/', CrearProveedorView.as_view()),
]
