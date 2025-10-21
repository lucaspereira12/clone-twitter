from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from app.models import Relacionamento

@login_required
def seguir_usuario(request, usuario_id):
    usuario_para_seguir = get_object_or_404(User, id=usuario_id)

    # Evitar que usuário siga ele mesmo
    if usuario_para_seguir != request.user:
        # Cria o relacionamento se não existir
        Relacionamento.objects.get_or_create(seguidor=request.user, seguindo=usuario_para_seguir)

    return redirect('perfil', username=usuario_para_seguir.username)

@login_required
def deixar_de_seguir_usuario(request, usuario_id):
    usuario_para_deixar = get_object_or_404(User, id=usuario_id)

    # Remove o relacionamento se existir
    Relacionamento.objects.filter(seguidor=request.user, seguindo=usuario_para_deixar).delete()

    return redirect('perfil', username=usuario_para_deixar.username)