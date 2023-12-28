from django.http import HttpResponse
from django.http import JsonResponse
import requests
import datetime
import json
from django.template import Template, Context
pagina = 0


def peliculas(request):
    try:
        global pagina 
        pagina = pagina+1  # incrementa la pagina 
        api_key = 'd78cfb8acb70922ed2c45fc903e9bcea'
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en&page={pagina}'
        # Realizar la llamada a la API
        respuesta = requests.get(url)
        resultados = respuesta.json()
        #print(resultados)
        peliculas = resultados['results']
        #print(peliculas)
        #print(resultados)
        plantilla = open('C:/martin/cursos/django/pictures-master/ferreteriaWeb/templates/articulo.html')
        plt=Template(plantilla.read())
        plantilla.close()
        ctx=Context({"peliculas":peliculas})
        documento=plt.render(ctx)
        return HttpResponse(documento)
    except Exception as e:
        # Manejar errores según tus necesidades
        print('Error en la solicitud. Código de estado: {peliculas.status_code}')



def peliculas_ant(request):
    try:
        global pagina 
        if (pagina>1):
            pagina = pagina-1  # va a la pagina anterior
        api_key = 'd78cfb8acb70922ed2c45fc903e9bcea'
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en&page={pagina}'
        # Realizar la llamada a la API
        respuesta = requests.get(url)
        resultados = respuesta.json()
        #print(resultados)
        peliculas = resultados['results']
        #print(peliculas)
        plantilla = open('C:/martin/cursos/django/pictures-master/ferreteriaWeb/templates/articulo.html')

        plt=Template(plantilla.read())
        plantilla.close()
        ctx=Context({"peliculas":peliculas})
        documento=plt.render(ctx)
        return HttpResponse(documento)
    except Exception as e:
        # Manejar errores según tus necesidades
        print('Error en la solicitud. Código de estado: {peliculas.status_code}')


def detalles_pelicula(request,pelicula_name):
    try: 
        global pagina 
        api_key = 'd78cfb8acb70922ed2c45fc903e9bcea'
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en&query={pelicula_name}'
        # Realizar la llamada a la API
        respuesta = requests.get(url)
        resultados = respuesta.json()
        peliculas = resultados['results']
        print(peliculas)
        plantilla = open('C:/martin/cursos/django/pictures-master/ferreteriaWeb/templates/detalle.html')
        plt=Template(plantilla.read())
        plantilla.close()
        ctx=Context({"peliculas":peliculas})
        documento=plt.render(ctx)
        print('----------- id',pelicula_name)
        return HttpResponse(documento)

    except Exception as e:
        # Manejar errores según tus necesidades
        print('Error en la solicitud')    