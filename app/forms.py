from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comentario, Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError

# =======================
# Formulário de Postagem
# =======================
class PostForm(forms.ModelForm):
    conteudo = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'O que está acontecendo?'
        }),
        label=''
    )

    class Meta:
        model = Post
        fields = ['conteudo']

# ========================
# Formulário de Comentário
# ========================
class ComentarioForm(forms.ModelForm):
    texto = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 1,
            'placeholder': 'Comente algo...',
            'class': 'form-control',
        }),
        label='',
        max_length=280
    )

    class Meta:
        model = Comentario
        fields = ['texto']

# ==========================
# Formulário de Cadastro
# ==========================
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome de usuário'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Senha'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirmar senha'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nome de usuário já está em uso.")

        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas não coincidem.")

        return password2

# =============================================
# Formulário unificado para edição de perfil
# =============================================
class EditarPerfilForm(forms.ModelForm):
    # Campos do modelo User
    first_name = forms.CharField(label='Nome', required=False)
    last_name = forms.CharField(label='Sobrenome', required=False)
    email = forms.EmailField(label='E-mail', required=False)

    class Meta:
        model = Profile
        fields = ['imagem']  # campo do Profile

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)

        # Guardar referência ao User (vindo de profile.user)
        if isinstance(user, Profile):
            self.profile_instance = user
            self.user_instance = user.user

        else:
            self.profile_instance = None
            self.user_instance = user

        # Preenche dados iniciais do usuário
        if self.user_instance:
            self.fields['first_name'].initial = self.user_instance.first_name
            self.fields['last_name'].initial = self.user_instance.last_name
            self.fields['email'].initial = self.user_instance.email

        # Garante que o campo imagem tenha o valor inicial (para mostrar o checkbox "Limpar")
        if self.profile_instance and self.profile_instance.imagem:
            self.fields['imagem'].initial = self.profile_instance.imagem

    def save(self, commit=True):
        profile = self.profile_instance
        user = self.user_instance

        # Atualiza dados do usuário
        if user:
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.email = self.cleaned_data.get('email')
            user.save()

        # Atualiza ou limpa a imagem
        imagem = self.cleaned_data.get('imagem')
        if imagem is False:  # checkbox “Limpar”
            profile.imagem.delete(save=False)
            profile.imagem = None

        elif imagem:
            profile.imagem = imagem

        if commit:
            profile.save()

        return profile