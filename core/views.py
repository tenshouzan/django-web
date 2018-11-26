from django.shortcuts import render
from .models import Tipo,Auto
# Create your views here.
def Home(request):
    # se retorna la rederizacion de una pagina html
    return render(request,'vistas/home.html')
def Listado(request):
    listado= Auto.objects.all()
    return render(request,'vistas/listado.html',{'listado':listado})
def Formulario(request):
    lt= Tipo.objects.all()#select * from Tipos
    if request.POST:
        patente= request.POST["patente"]
        dueno=request.POST["nombre"]
        marca=request.POST["marca"]
        modelo=request.POST["modelo"]
        anio=request.POST["anio"]
        tipo=request.POST["tipo"]

        obj_tipo= Tipo.objects.get(id=tipo)

        auto= Auto(
            patente=patente,
            dueno=dueno,
            marca=marca,
            modelo=modelo,
            anio=int(anio),
            tipo=obj_tipo
        )
        auto.save()
        return render(request,'vistas/formulario_ingreso.html',
                              {'tipos':lt,'mensaje':'grabo'})

    return render(request,'vistas/formulario_ingreso.html',{'tipos':lt})    