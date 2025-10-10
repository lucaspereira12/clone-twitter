from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def cadastro_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "cadastro.html", {"error": "As senhas não coincidem."})

        if User.objects.filter(username=username).exists():
            return render(request, "cadastro.html", {"error": "Nome de usuário já existe."})

        user = User.objects.create_user(username=username, password=password)
        return redirect("home")

    return render(request, "cadastro.html")