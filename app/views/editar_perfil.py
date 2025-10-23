from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from app.forms import EditarPerfilForm
from app.models import Profile

@login_required
def editar_perfil_view(request):
    user = request.user
    profile, _ = Profile.objects.get_or_create(user=user)

    usuario_form = EditarPerfilForm(
        request.POST or None,
        request.FILES or None,
        instance=profile  # agora é o Profile
    )
    senha_form = PasswordChangeForm(user, request.POST or None)

    if request.method == "POST":
        # Alterar senha
        if 'old_password' in request.POST:
            if senha_form.is_valid():
                user = senha_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Senha alterada com sucesso!")
                return redirect('editar_perfil')
            else:
                messages.error(request, "Por favor, corrija os erros na senha.")
        # Atualizar perfil
        elif usuario_form.is_valid():
            usuario_form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('editar_perfil')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")

    return render(request, 'editar_perfil.html', {
        'usuario_form': usuario_form,
        'senha_form': senha_form,
        'profile': profile
    })