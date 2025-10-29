from rest_framework import serializers
from app.models import Post, Curtida, Comentario

class PostSerializer(serializers.ModelSerializer):
    autor_username = serializers.CharField(source='autor.username', read_only=True)
    autor_nome = serializers.CharField(source='autor.first_name', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'autor_username', 'autor_nome', 'conteudo', 'data_criacao']

class CurtidaSerializer(serializers.ModelSerializer):
    total_curtidas = serializers.SerializerMethodField()
    curtido_por_usuario = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'conteudo', 'total_curtidas', 'curtido_por_usuario']

    def get_total_curtidas(self, obj):
        return obj.curtida_set.count()

    def get_curtido_por_usuario(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.curtida_set.filter(usuario=user).exists()
        return False

class ComentarioSerializer(serializers.ModelSerializer):
    autor_username = serializers.CharField(source='autor.username', read_only=True)
    autor_nome = serializers.CharField(source='autor.first_name', read_only=True)
    data_criacao = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'autor_username', 'autor_nome', 'texto', 'data_criacao']