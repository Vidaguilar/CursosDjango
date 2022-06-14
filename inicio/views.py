from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

menu="""<a href="/">home</a>
<a href="/formulario">Formulario</a>
<a href="/contacto">Contacto</a>"""

def principal(request):
    contenido="<h1>Hola Django</h1>"
    return HttpResponse(menu + contenido)

def contacto(request):
    contenido="""<h2>Contacto</h2>
     <p>Nombre:<input type="text" name="nombre"></p>
     <p>MeNsaje:</p><p><textarea  cols="50" rows="10"></textarea></p>
     <p><input type="button" name="enviar" value="Enviar"></p>"""
    return HttpResponse(menu + contenido)

def formulario(request):
    contenido="""<h2>Registrar</h2>
    <p>Matricula:<input type="text"></p>
    <p>Nombre:<input type="text"></p>
    <p>Carrera:
        <select name="Carrera" >
        <option >ING. DGS</option>
        <option>ING. EVND</option>
    </select>
    </p>
    <input type="radio" name="Turno" id="">MAtutino
    <input type="radio" name="Turno" id="">Vespertino
    <p><input type="button"  name="enviar" value="Enviar"></p>"""
    return HttpResponse(contenido)
