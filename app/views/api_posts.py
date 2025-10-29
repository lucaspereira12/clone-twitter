from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.models import Post
from app.serializers import PostSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    Endpoint da API para listar e criar postagens.
    GET  → lista todas as postagens (mais recentes primeiro)
    POST → cria uma nova postagem (requer autenticação)
    """
    queryset = Post.objects.all().order_by('-data_criacao')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)