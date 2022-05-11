from django.urls import path
from .views import home, discografia, galeria,formulario_registro,inicio_sesion 
urlpatterns = [
    path('', home,name="home"),
    path('discografia', discografia, name="discografia"),
    path('galeria',galeria,name="galeria"),
    path('formulario_registro',formulario_registro,name="formulario"),
    path('inicio_sesion',inicio_sesion,name="inicio"),
]