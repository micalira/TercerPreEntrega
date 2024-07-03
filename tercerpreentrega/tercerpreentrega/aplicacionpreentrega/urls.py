from django.urls import path,include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('tiendaMayoristas',tiendaMayoristas, name="tiendaMayoristas"),
    path('tiendaMinorista',tiendaMinorista, name="tiendaMinorista"),
]