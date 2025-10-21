from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from app.views.utils import autenticar_usuario

def login_view(request):
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        sucesso, form = autenticar_usuario(request)

        if sucesso:
            return redirect('feed')

    else:
        form = AuthenticationForm()

    return render(request, 'index.html', {'form': form})