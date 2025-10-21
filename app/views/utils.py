from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from app.models import Post, Curtida, Relacionamento
from app.forms import ComentarioForm

def gerar_info_postagens(usuario):
    # Obtém a lista dos usuários que o usuário está seguindo
    seguindo_ids = list(Relacionamento.objects.filter(seguidor=usuario).values_list('seguindo_id', flat=True))
    
    # Inclui o próprio usuário para que as postagens dele também apareçam no feed
    seguindo_ids.append(usuario.id)
    
    # Busca as postagens desses usuários (seguindo + próprio usuário)
    postagens = Post.objects.filter(autor__id__in=seguindo_ids).order_by("-data_criacao")
    
    # IDs dos posts que o usuário curtiu
    curtidos_ids = set(Curtida.objects.filter(usuario=usuario).values_list("post_id", flat=True))

    return [
        {
            "post": post,
            "curtido": post.id in curtidos_ids,
            "total_curtidas": post.curtidas.count(),
        }

        for post in postagens
    ]

def processar_comentario(request):
    form = ComentarioForm(request.POST)

    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.autor = request.user
        comentario.post_id = request.POST.get('post_id')
        comentario.save()
        return True

    return False

def autenticar_usuario(request):
    form = AuthenticationForm(request=request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return True, form

    return False, form

def realizar_logout(request):
    logout(request)
    request.session.flush()  # Garante que toda a sessão seja limpa