from django.http import JsonResponse
from django.shortcuts import render
from .models import Pais, Ciudad

# Create your views here.

def index(request):
    return render(request, 'index.html')


def get_paises(request):
    # Obtenemos los valores de la tabla paises
    paises = list(Pais.objects.values())
    
    # verificamos que exitan valores 
    if(len(paises)>0):
        data = {'message':'Success', 'paises':paises}
    else:
        data = {'message':'Not Found'}

    # devolvemos estos valores en una respuesta JSON
    return JsonResponse(data)


def get_ciudades(request, pais_id):
    # obtenemos las paises vinculadas al id del pais
    ciudades = list(Ciudad.objects.filter(pais_id=pais_id).values())

    # verificamos que exitan valores 
    if(len(ciudades)>0):
        data = {'message':'Success', 'ciudades':ciudades}
    else:
        data = {'message':'Not Found'}

    # devolvemos estos valores en una respuesta JSON
    return JsonResponse(data)