from rest_framework import serializers
from app.models import Comentario, Post

class ComentarioSerializer(serializers.ModelSerializer):
    autor_username = serializers.CharField(source='autor.username', read_only=True)
    autor_nome = serializers.CharField(source='autor.first_name', read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'autor_username', 'autor_nome', 'texto', 'data_criacao']

class PostSerializer(serializers.ModelSerializer):
    autor_username = serializers.CharField(source='autor.username', read_only=True)
    autor_nome = serializers.CharField(source='autor.first_name', read_only=True)
    comentarios = ComentarioSerializer(source='comentario_set', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'autor', 'autor_username', 'autor_nome', 'conteudo', 'data_criacao', 'comentarios']