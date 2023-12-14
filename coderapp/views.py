from django.http import HttpResponse
from django.shortcuts import render
from coderapp.models import Profesor

def leer_profesor(request):
    profe = Profesor(nombre="John", apellido="Cena", email="JhonCena@test.com")
    profe.save()
    return HttpResponse("Profesor creado exitosamente")

def leer_alumnos(request):
    contexto = {
        "nombre": "juan",
        "edad" : "20",
        "lenguaje" : "python",
        "cursos" : ["coder","dalto"],
    }

    return render(request, 'plantilla.html', contexto)

