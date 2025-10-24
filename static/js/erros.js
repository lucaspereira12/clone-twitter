// Esconde mensagens de erro quando o usuário começa a digitar novamente
document.addEventListener("DOMContentLoaded", function () {
  const inputs = document.querySelectorAll("input, textarea");
  const mensagensErro = document.querySelectorAll(".mensagem-erro");

  inputs.forEach(input => {
    input.addEventListener("input", () => {
      mensagensErro.forEach(msg => {
        msg.style.display = "none";
      });
    });
  });
});