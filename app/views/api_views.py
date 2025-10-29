from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.models import Post, Curtida, Comentario
from app.serializers import CurtidaSerializer
from app.serializers import ComentarioSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def curtir_post_api(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"erro": "Post não encontrado."}, status=404)

    curtida = Curtida.objects.filter(post=post, usuario=request.user).first()

    if curtida:
        curtida.delete()
        mensagem = "Curtida removida"
    else:
        Curtida.objects.create(post=post, usuario=request.user)
        mensagem = "Curtida adicionada"

    serializer = CurtidaSerializer(post, context={'request': request})
    return Response({"mensagem": mensagem, "post": serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comentar_post_api(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"erro": "Post não encontrado."}, status=404)

    texto = request.data.get('texto', '').strip()
    if not texto:
        return Response({"erro": "O texto do comentário não pode ser vazio."}, status=400)

    comentario = Comentario.objects.create(post=post, autor=request.user, texto=texto)
    serializer = ComentarioSerializer(comentario)
    return Response({"mensagem": "Comentário adicionado", "comentario": serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_comentarios_api(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"erro": "Post não encontrado."}, status=404)

    comentarios = Comentario.objects.filter(post=post).order_by('data_criacao')
    serializer = ComentarioSerializer(comentarios, many=True)
    return Response(serializer.data)