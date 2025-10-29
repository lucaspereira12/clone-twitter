from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse

@login_required
def excluir_conta_view(request):
    if request.method == "POST":
        senha = request.POST.get("senha_confirmacao", "")
        user = request.user

        if not senha:
            return JsonResponse({"status": "erro", "mensagem": "Digite sua senha."})

        if not user.check_password(senha):
            return JsonResponse({"status": "erro", "mensagem": "Senha incorreta."})

        user.delete()
        logout(request)
        request.session.flush()
        return JsonResponse({"status": "sucesso", "redirect": "/"})

    return JsonResponse({"status": "erro", "mensagem": "Requisição inválida."})