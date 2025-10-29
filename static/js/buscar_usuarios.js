document.addEventListener("DOMContentLoaded", () => {
  const campoBusca = document.getElementById("campo-busca");
  const resultados = document.getElementById("resultados");

  campoBusca.addEventListener("input", async () => {
    const termo = campoBusca.value.trim();

    try {
      const response = await fetch(`?q=${encodeURIComponent(termo)}`, {
        headers: { "X-Requested-With": "XMLHttpRequest" }
      });

      const html = await response.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, "text/html");
      const novosResultados = doc.querySelector("#resultados").innerHTML;

      resultados.innerHTML = novosResultados;
    } catch (error) {
      console.error("Erro ao buscar usuários:", error);
    }
  });
});