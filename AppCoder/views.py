from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return HttpResponse("Hola como estas")

def despedida(request):
    return HttpResponse("Hasta luego amigos")

def saludo_nombre(request, nombre):
    return HttpResponse(f'HOLA BUENOS DIAS {nombre}')

def anio_nacimiento(request, anio):
    return HttpResponse(f'NACISTE EN EL AÑO {anio}')

def primer_template(request):
    return render(request, "AppCoder/index.html")

def template_modificado(request):
    suma = 1 + 1
    return render(request, "AppCoder/index.html",
    {
        "nombre" : "Eduar",
        "apellido" : "Quintero",
        "suma" : suma
    })

def template_modificado2(request, nombre, apellido):
    return render(request, "AppCoder/index2.html",
    {
        "nombre" : nombre,
        "apellido" : apellido
    })

def template_modificado2(request):
    return render(request, "AppCoder/index2.html",
    {
        "notas" : [1, 2, 3, 4, 5, 6, 7, 8, 9]
    })