from django.http import HttpResponse
from django.shortcuts import render

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


def Saludar(request):
    return HttpResponse("Hola")

def Index(request):
    amigo=Persona("Andrea Lucero", "25")
    lista=["Perro", "Gato", "Tortuga"]
    datos={"Nombre": "Felipe Durán Espinoza", "Animales":lista, "amigo":amigo }
    return render(request, 'Index.html', datos)