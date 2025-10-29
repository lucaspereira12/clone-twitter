from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from app.models import Post, Comentario
from app.api.serializers import ComentarioSerializer, PostSerializer

def home(request):
    return HttpResponse("Bem-vindo ao Clone Twitter!")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def criar_comentario_api(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"erro": "Post não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ComentarioSerializer(data=request.data)
    if serializer.is_valid():
        # Cria o comentário
        Comentario.objects.create(
            autor=request.user,
            post=post,
            texto=serializer.validated_data['texto']
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_posts_api(request):
    posts = Post.objects.all().order_by('-data_criacao')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)