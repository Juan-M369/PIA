from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('Agentes/',views.Agentes,name="Agentes"),
    path('Mapas/',views.Mapas,name="Mapas"),
    path('Arsenal/',views.Arsenal,name="Arsenal"),
    path('Equiposcom/',views.Equiposcom,name="Equiposcom")
]