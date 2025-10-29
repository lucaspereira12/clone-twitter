// Exibe/oculta o menu dropdown
document.addEventListener("DOMContentLoaded", function() {
  const toggle = document.getElementById("menu-toggle");
  const menu = document.getElementById("menu-list");
  const container = toggle?.closest(".menu-container");

  if (toggle && menu && container) {
    toggle.addEventListener("click", (e) => {
      e.stopPropagation();
      container.classList.toggle("active");
    });

    // Fecha o menu se clicar fora
    document.addEventListener("click", (e) => {
      if (!container.contains(e.target)) {
        container.classList.remove("active");
      }
    });
  }
});

// Visibilidade da navbar
document.addEventListener("DOMContentLoaded", function() {
  const navbar = document.querySelector(".navbar");
  let lastScrollTop = 0;

  // Navbar visível no início
  navbar.style.transform = "translateY(0)";
  navbar.style.transition = "transform 0.3s ease";

  window.addEventListener("scroll", function() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop === 0) {
      // No topo → mostrar navbar
      navbar.style.transform = "translateY(0)";
    } else if (scrollTop > lastScrollTop) {
      // Rolando para baixo → esconder
      navbar.style.transform = "translateY(-100%)";
    } else {
      // Rolando para cima → mostrar
      navbar.style.transform = "translateY(0)";
    }

    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
  });
});