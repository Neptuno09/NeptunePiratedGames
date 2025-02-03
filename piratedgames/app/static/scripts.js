function toggleParrafo(event) {
    event.preventDefault();  // Evitar que el botón haga submit o recargue la página
  
    const parrafo = document.getElementById("parrafo");
    const boton = document.querySelector(".boton-collapse");
  
    // Alternar la clase para expandir o colapsar el párrafo
    if (parrafo.classList.contains("expandido")) {
      parrafo.classList.remove("expandido");
      boton.innerHTML = "⬇️"; // Cambiar el ícono de la flecha
    } else {
      parrafo.classList.add("expandido");
      boton.innerHTML = "⬆️"; // Cambiar el ícono de la flecha
    }
  }