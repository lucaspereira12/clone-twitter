from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField(max_length=280)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username}: {self.conteudo[:30]}"

class Curtida(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='curtidas')
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'post')

    def __str__(self):
        return f"{self.usuario.username} curtiu {self.post.id}"

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField(max_length=280)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username} comentou: {self.texto[:30]}"

class Relacionamento(models.Model):
    seguidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguindo')
    seguindo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguidores')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('seguidor', 'seguindo')

    def __str__(self):
        return f'{self.seguidor} segue {self.seguindo}'