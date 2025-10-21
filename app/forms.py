from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comentario

# Formulário de postagem
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

# Formulário de comentário
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

# Formulário de cadastro personalizado
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nome de usuário'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Senha'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirmar senha'
        })