from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import Post, Relacionamento

@login_required
def perfil_view(request, username):
    usuario_perfil = get_object_or_404(User, username=username)

    postagens = Post.objects.filter(autor=usuario_perfil).order_by('-data_criacao')

    seguidores = Relacionamento.objects.filter(seguindo=usuario_perfil)
    seguindo = Relacionamento.objects.filter(seguidor=usuario_perfil)

    seguindo_usuario_logado = Relacionamento.objects.filter(
        seguidor=request.user,
        seguindo=usuario_perfil
    ).exists()

    context = {
        'usuario_perfil': usuario_perfil,
        'postagens': postagens,
        'seguidores': seguidores,
        'seguindo': seguindo,
        'seguindo_usuario_logado': seguindo_usuario_logado,
    }
    return render(request, 'perfil.html', context)