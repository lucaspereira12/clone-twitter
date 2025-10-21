from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from app.views.utils import realizar_logout

@login_required
def logoff_view(request):
    realizar_logout(request)
    return redirect("home")