from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def excluir_conta_view(request):
    if request.method == "POST":
        request.user.delete()
        request.session.flush()
        return redirect("home")
    return redirect("perfil")