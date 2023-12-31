"""
URL configuration for ferreteriaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from ferreteriaWeb.views import menu, peliculas, peliculas_ant  
from ferreteriaWeb.views import peliculas, peliculas_ant, detalles_pelicula

urlpatterns = [
    path('peliculas/', peliculas),
    path('peliculas_ant/', peliculas_ant),
    path('detalles_pelicula/<str:pelicula_name>/',detalles_pelicula)
]
