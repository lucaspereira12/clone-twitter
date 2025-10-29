document.addEventListener("DOMContentLoaded", function () {
  const textarea = document.getElementById("post-conteudo");
  const contador = document.getElementById("contador-caracteres");

  if (!textarea || !contador) return;

  textarea.addEventListener("input", function () {
    const max = 280;
    const length = textarea.value.length;
    contador.textContent = `${length} / ${max}`;
    contador.style.color = "gray";
  });
});

// Contadores de comentários
document.addEventListener("DOMContentLoaded", function () {
  const comentarios = document.querySelectorAll(".comentario-textarea");

  comentarios.forEach(function (textarea) {
    const contador = textarea.parentElement.querySelector(".contador-comentario");
    if (!contador) return;

    textarea.addEventListener("input", function () {
      const max = 280;
      const length = textarea.value.length;
      contador.textContent = `${length} / ${max}`;
      contador.style.color = "gray";
    });
  });
});

// Expansão automática de textareas
document.addEventListener("DOMContentLoaded", function () {
  const textareas = document.querySelectorAll("textarea");

  textareas.forEach((textarea) => {
    // Ajusta o tamanho inicial
    textarea.style.overflow = "hidden";
    textarea.style.resize = "none";
    autoResize(textarea);

    // Aumenta conforme digita
    textarea.addEventListener("input", () => autoResize(textarea));
  });

  function autoResize(element) {
    element.style.height = "auto"; // reseta antes de medir
    element.style.height = element.scrollHeight + "px"; // ajusta à altura do conteúdo
  }
});