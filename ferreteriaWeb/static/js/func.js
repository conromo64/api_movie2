
function peliculasSig(){
    window.location.href = "http://localhost:8000/peliculas/";
}

function peliculasAnt() {
    window.location.href = "http://localhost:8000/peliculas_ant/";
}

// func.js

function mostrarDetallesPelicula(index) {
    // Puedes acceder a la película correspondiente usando el índice
    var auxpelicula = pelicula[index];

    // Aquí puedes realizar cualquier acción con la película, por ejemplo, mostrar detalles
    console.log('Detalles de la película:', auxpeliculapelicula);
}


// func.js

document.addEventListener('DOMContentLoaded', function() {
    var titulos = document.querySelectorAll('.titulo');
    console.log('Número de elementos .titulo:', titulos.length);
    titulos.forEach(function(titulo, index) {
        titulo.addEventListener('click', function() {
            mostrarDetallesPelicula(index);
        });
    });

    function mostrarDetallesPelicula(index) {
        // Puedes acceder a la película correspondiente usando el índice
        //var pelicula = peliculas[index];

        // Aquí puedes realizar cualquier acción con la película, por ejemplo, mostrar detalles
        //console.log('Detalles de la película:', pelicula);
        console.log("entre")
    }
});

