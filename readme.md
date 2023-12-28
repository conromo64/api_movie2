# Movies App with API — Harvard CS50 Web — Final Project

Youtube demo: https://www.youtube.com/watch?v=D_NdkMZV28w

# Distinctiveness and Complexity:
 This is a web application that allows you to browse popular movies using The Movie Database (TMDb) API. The application displays a grid of movie posters and titles, and allows you to navigate through pages of movie results using pagination buttons. 
 
 Using many of the tools and techniques covered in CS50W. By providing functionality by combining a public API the back-end using python-django and HTML5, CSS and javascript for the front-end.
 It is also mobile and multiple OS and browser responsive which helps to provide a good user experience in terms of the easy to use interface

# File Structure

## What's contained in each file:

-pictures-master
    -ferreteriaWeb
        -static
            -css
                estilos.css (defines the CSS for the front-end)
            -js
                func.js     (defines javaScript frunctions called in the front-end)
        asgi.py         (ASGI config for ferreteriaWeb project.)
        settings.py     (contains all the configuration of your Django installation)
        urls.py         (URL configuration for ferreteriaWeb project.)
        views.py        (defines functions for the backend called by the URL's)
        wsgi.py         (It exposes the WSGI callable as a module-level variable named  
                        "application".)
    -templates
        articulo.html   (code HTML for the front-end, shows movies catalog)
        deetall.html    (code HTML for the front-end, shows movie detail)
    manage.py           (main function)
    readme.md           (this file) 
    requirements.txt    (dependencies for the project to work, use pip install -r       requirements.txt) 


## Technologies Used

The following technologies were used to create this application:

- HTML
- CSS
- JavaScript
- The Movie Database (TMDb) API
- Python
- Django

## Setup

To run the application, you need to follow these steps:

1. Clone this repository to your local machine
2. Open a terminal or command prompt.
   Navigate to the directory where your requirements.txt file is located.
   Run the following command to install the dependencies: pip install -r requirements.txt
3. Obtain an API key from The Movie Database (TMDb) website https://www.themoviedb.org/
4. Replace YOUR_API_KEY in the following URL https://api.themoviedb.org/3/movie/popular?api_key=YOUR_API_KEY&language=en-US&page= with your own API key
5. Open the index.html file in your web browser
6. Run python3 manage.py runserver command or python if you are on windows

## Usage

The application displays a grid of movie posters and titles on the main page. You can use the pagination buttons at the bottom of the page to navigate through pages of movie results.
Also by clicking the link under each movie poster you will go to the movie page with details and related information about it as well as similar movies for your information if you are interested.
Make sure to do the setup listed above first.

