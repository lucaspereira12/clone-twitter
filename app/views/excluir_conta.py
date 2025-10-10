from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def excluir_conta_view(request):
    request.user.delete()
    return redirect("home")