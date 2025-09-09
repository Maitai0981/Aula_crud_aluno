from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    # API endpoints
    path('cadastrar', views.cadastrar_aluno, name='cadastrar'),
    path('listar', views.listar_alunos, name='listar'),
    path('<int:pk>', views.buscar_aluno, name='buscar'),
    path('', views.atualizar_aluno, name='atualizar'),
    path('<int:pk>', views.excluir_aluno, name='excluir'),
    path('remover-imagem/<int:pk>', views.remover_imagem_aluno, name='remover_imagem'),
    
    # Frontend
    path('', views.serve_frontend, name='frontend'),
]