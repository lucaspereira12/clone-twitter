from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Post
from app.api.serializers import PostSerializer

@api_view(['GET'])
def listar_posts_api(request):
    posts = Post.objects.all().order_by('-data_criacao')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)