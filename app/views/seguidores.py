from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Relacionamento

@login_required
def seguidores_view(request):
    user = request.user
    seguidores = User.objects.filter(seguindo__seguindo=user)
    seguindo = User.objects.filter(seguidores__seguidor=user)

    return render(request, 'seguidores.html', {
        'seguidores': seguidores,
        'seguindo': seguindo,
    })