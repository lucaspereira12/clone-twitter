from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from app.forms import ComentarioForm
from app.models import Post

@login_required
def comentar_view(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)

        if form.is_valid():
            post_id = request.POST.get("post_id")

            try:
                post = Post.objects.get(id=post_id)
                comentario = form.save(commit=False)
                comentario.autor = request.user
                comentario.post = post
                comentario.save()

            except Post.DoesNotExist:
                pass

    return redirect("feed")