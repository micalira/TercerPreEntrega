from django.shortcuts import render
from .models import*

def home (request):
    return render(request, "aplicacionpreentrega/index.html")

def tiendaMayoristas (request):
    contexto = {"cursos": tiendaMayoristas.objects.all}
    return render(request, "aplicacionpreentrega/tiendaMayoristas.html", contexto)

def tiendaMinorista (request):
    return render(request, "aplicacionpreentrega/tiendaMinorista.html")