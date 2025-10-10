from django.urls import path
from app.views.login import login_view
from app.views.cadastro import cadastro_view
from app.views.feed import feed_view
from app.views.logoff import logoff_view
from app.views.excluir_conta import excluir_conta_view

urlpatterns = [
    path('', login_view, name='home'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('feed/', feed_view, name='feed'),
    path('logoff/', logoff_view, name='logoff'),
    path('remover_conta/', excluir_conta_view, name='remover_conta'),
]