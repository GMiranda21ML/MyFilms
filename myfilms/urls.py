from django.urls import path
from myfilms.views import index, buscar, adicionar_filme, listar_filmes, filme_detalhes
urlpatterns = [
    path('', index, name = 'index'),
    path('buscar/', buscar, name = 'buscar'),
    path('adicionar_filme/', adicionar_filme, name='adicionar_filme'),
    path('minha-lista/', listar_filmes, name='minhaLista'),
    path('filme/<int:filme_id>/', filme_detalhes, name='filmeDetalhe'),
]
