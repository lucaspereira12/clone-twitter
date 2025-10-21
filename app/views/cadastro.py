from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from app.forms import CustomUserCreationForm

class CadastroView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "cadastro.html"
    success_url = reverse_lazy("home")