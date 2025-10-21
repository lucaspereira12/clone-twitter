from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.forms import PostForm, ComentarioForm
from app.views.utils import gerar_info_postagens

@login_required
def feed_view(request):
    return render(request, "feed.html", {
        "form": PostForm(),
        "comentario_form": ComentarioForm(),
        "postagens_info": gerar_info_postagens(request.user),
        "username": request.user.username,
    })