from django.urls import path
from app.views.login import login_view
from app.views.cadastro import CadastroView
from app.views.feed import feed_view
from app.views.postagens.postar import postar_view
from app.views.postagens.curtir import curtir_view
from app.views.postagens.comentar import comentar_view
from app.views.logoff import logoff_view
from app.views import excluir_conta

from app.views import feed, perfil, seguir
from app.views.seguidores import seguidores_view

urlpatterns = [
    path('', login_view, name='home'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('feed/', feed_view, name='feed'),
    path('postar/', postar_view, name='postar'),
    path('curtir/<int:post_id>/', curtir_view, name='curtir'),
    path('comentar/', comentar_view, name='comentar'),
    path('logoff/', logoff_view, name='logoff'),
    path('excluir-conta/', excluir_conta.excluir_conta_view, name='excluir_conta'),

    path('seguir/<int:usuario_id>/', seguir.seguir_usuario, name='seguir_usuario'),
    path('deixar_de_seguir/<int:usuario_id>/', seguir.deixar_de_seguir_usuario, name='deixar_de_seguir_usuario'),
    path('perfil/<str:username>/', perfil.perfil_view, name='perfil'),
    path('rede/', seguidores_view, name='seguidores'),
]