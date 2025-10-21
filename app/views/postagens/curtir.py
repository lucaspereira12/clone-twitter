from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from app.models import Post, Curtida

@login_required
def curtir_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    curtida = Curtida.objects.filter(post=post, usuario=request.user).first()

    if curtida:
        curtida.delete()

    else:
        Curtida.objects.create(post=post, usuario=request.user)

    return redirect("feed")