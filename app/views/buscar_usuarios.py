from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q

@login_required
def buscar_usuarios_view(request):
    termo = request.GET.get('q', '')

    if termo:
        usuarios = User.objects.filter(
            Q(username__icontains=termo) | Q(first_name__icontains=termo)
        ).exclude(id=request.user.id)

    else:
        usuarios = User.objects.exclude(id=request.user.id)

    return render(request, 'buscar_usuarios.html', {
        'usuarios': usuarios,
        'termo': termo,
    })