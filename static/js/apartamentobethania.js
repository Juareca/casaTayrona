function cambiarImagen(id) {
    // Ocultar todas las imágenes
    var imagenes = document.querySelectorAll('.itemCarrousel');
    imagenes.forEach(function(img) {
        img.style.display = 'none';
    });

    // Mostrar la imagen correspondiente al ID proporcionado
    var imagenMostrar = document.getElementById(id);
    if (imagenMostrar) {
        imagenMostrar.style.display = 'block';
    }
}
