from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('paises/', get_paises, name='get_paises'),
    path('ciudades/<int:pais_id>', get_ciudades, name='get_ciudades'),
]