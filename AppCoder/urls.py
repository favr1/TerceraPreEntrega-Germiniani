from django.urls import path
from AppCoder import views 
from AppCoder.views import *

urlpatterns = [
    path('',views.inicio, name="Inicio"), #Esta era nuestra primera vista
    path('AutosView/',views.view_auto, name="autosView"),
    path('MecanicosView/',views.view_mecanicos, name="mecanicosView"),
    path('PiezasView/',views.view_piezas, name="piezasView"),
    path('nosotros/',views.nosotros, name="Nosotros"),
    path('Registro-De-Mecanico/', views.registrar_mecanico, name="mecanicoRegistro"),
    path('Registro-De-Auto/', views.registrar_auto, name="autoRegistro"),
    path('Registro-De-Pieza/', views.registrar_pieza, name="piezaRegistro"),
    path('autos/', views.autos_disponibles, name="autos"),
    path('mecanicos/', views.mecanicos_disponibles, name="mecanicos"),
    path('piezas/', views.piezas_disponibles, name="piezas"),
    path('Buscar-Autos/', views.auto_buscar, name="autoBuscar"),
    path('Buscar-Mecanicos/', views.mecanico_buscar, name="mecanicoBuscar"),
    path('Buscar-Piezas/', views.pieza_buscar, name="piezaBuscar"),
]