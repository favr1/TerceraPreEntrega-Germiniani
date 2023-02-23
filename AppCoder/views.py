from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')
    #return HttpResponse('vista inicio')

def view_auto(request):
    return render(request, 'AppCoder/inicio_autos.html')

def view_mecanicos(request):
    return render(request, 'AppCoder/inicio_mecanicos.html')

def view_piezas(request):
    return render(request, 'AppCoder/inicio_piezas.html')

def nosotros(request):
    return render(request, 'AppCoder/nosotros.html')

def registrar_auto(request):
    form = auto_registro()
    if request.method == 'POST':
        form = auto_registro(request.POST)
        if form.is_valid():
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            reparacion = form.cleaned_data['reparacion']
            precio = form.cleaned_data['precio']
            auto_nuevo = Autos(marca=marca, modelo=modelo, reparacion=reparacion ,precio=precio)
            auto_nuevo.save()
            return render(request, "AppCoder/autos.html")
    return render(request, "AppCoder/autoRegistro.html", {'form': form, 'auto_registro': auto_registro})   

def registrar_mecanico(request):
    form = mecanico_registro()
    if request.method == 'POST':
        form = mecanico_registro(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            especializacion = form.cleaned_data['especializacion']
            mecanico_nuevo = Mecanicos(nombre=nombre, apellido=apellido, especializacion=especializacion)
            mecanico_nuevo.save()
            return render(request, "AppCoder/mecanicoRegistrado.html")
    return render(request, "AppCoder/mecanicoRegistro.html", {'form': form, 'mecanico_registro': mecanico_registro})   

def registrar_pieza(request):
    form = pieza_registro()
    if request.method == 'POST':
        form = pieza_registro(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            cantidad = form.cleaned_data['cantidad']
            pieza_nuevo = Piezas(nombre=nombre, precio=precio, cantidad=cantidad)
            pieza_nuevo.save()
            return render(request, "AppCoder/piezaRegistrada.html")
    return render(request, "AppCoder/piezaRegistro.html", {'form': form, 'pieza_registro': pieza_registro})   

"""
def autos_disponibles(request):
    autos_disp = Autos(marca,modelo,reparacion,precio)
    return render(request, 'AppCoder/autos.html', {'autos_disp': autos_disp})
"""
def autos_disponibles(request):
    autos_disp = Autos.objects.all()
    return render(request, 'AppCoder/autoLista.html', {'autos_disp': autos_disp})   

def mecanicos_disponibles(request):
    mecanicos_disp = Mecanicos.objects.all()
    return render(request, 'AppCoder/mecanicoLista.html', {'mecanicos_disp': mecanicos_disp})  

def piezas_disponibles(request):
    piezas_disp = Piezas.objects.all()
    return render(request, 'AppCoder/piezaLista.html', {'piezas_disp': piezas_disp})  

def autos(request):
    return (request, 'AppCoder/autos.html')

def auto_buscar(request):
    query = request.GET.get('nombre')
    if query is not None:
        resultados = Autos.objects.filter(marca__icontains=query)
    else:
        resultados = []
    return render(request, 'AppCoder/busquedaAuto.html', {'resultados': resultados})

def mecanico_buscar(request):
    query = request.GET.get('nombre')
    if query is not None:
        resultados = Mecanicos.objects.filter(nombre__icontains=query)
    else:
        resultados = []
    return render(request, 'AppCoder/busquedaMecanico.html', {'resultados': resultados})

def pieza_buscar(request):
    query = request.GET.get('nombre')
    if query is not None:
        resultados = Piezas.objects.filter(nombre__icontains=query)
    else:
        resultados = []
    return render(request, 'AppCoder/busquedaPieza.html', {'resultados': resultados})