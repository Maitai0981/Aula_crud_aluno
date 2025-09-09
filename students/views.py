from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json

from .models import Aluno
from .serializers import AlunoSerializer, AlunoCreateUpdateSerializer


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def cadastrar_aluno(request):
    """Cadastra um novo aluno"""
    try:
        # Parse dos dados do aluno do FormData
        aluno_data = json.loads(request.data.get('aluno', '{}'))
        
        # Adiciona a imagem se fornecida
        if 'imagem' in request.FILES:
            aluno_data['imagem'] = request.FILES['imagem']
        
        serializer = AlunoCreateUpdateSerializer(data=aluno_data)
        
        if serializer.is_valid():
            aluno = serializer.save()
            response_serializer = AlunoSerializer(aluno)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except json.JSONDecodeError:
        return Response(
            {'error': 'Dados do aluno inválidos'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def listar_alunos(request):
    """Lista todos os alunos"""
    try:
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def buscar_aluno(request, pk):
    """Busca um aluno por ID"""
    try:
        aluno = get_object_or_404(Aluno, pk=pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
def atualizar_aluno(request):
    """Atualiza um aluno existente"""
    try:
        # Parse dos dados do aluno do FormData
        aluno_data = json.loads(request.data.get('aluno', '{}'))
        
        if 'id' not in aluno_data:
            return Response(
                {'error': 'ID do aluno é obrigatório'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        aluno = get_object_or_404(Aluno, pk=aluno_data['id'])
        
        # Adiciona a imagem se fornecida
        if 'imagem' in request.FILES:
            aluno_data['imagem'] = request.FILES['imagem']
        
        serializer = AlunoCreateUpdateSerializer(aluno, data=aluno_data, partial=True)
        
        if serializer.is_valid():
            aluno_atualizado = serializer.save()
            response_serializer = AlunoSerializer(aluno_atualizado)
            return Response(response_serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except json.JSONDecodeError:
        return Response(
            {'error': 'Dados do aluno inválidos'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['DELETE'])
def excluir_aluno(request, pk):
    """Exclui um aluno"""
    try:
        aluno = get_object_or_404(Aluno, pk=pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['DELETE'])
def remover_imagem_aluno(request, pk):
    """Remove a imagem de um aluno"""
    try:
        aluno = get_object_or_404(Aluno, pk=pk)
        
        if aluno.imagem:
            aluno.imagem.delete(save=False)
            aluno.imagem = None
            aluno.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


def serve_frontend(request):
    """Serve o arquivo HTML do frontend"""
    from django.shortcuts import render
    return render(request, 'index.html')