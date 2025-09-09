from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Aluno
import json


class AlunoModelTest(TestCase):
    def setUp(self):
        self.aluno = Aluno.objects.create(
            nome="João Silva",
            serie="3º Ano",
            sexo="M"
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.aluno), "João Silva")
    
    def test_tem_imagem_false(self):
        self.assertFalse(self.aluno.tem_imagem())


class AlunoAPITest(APITestCase):
    def setUp(self):
        self.aluno = Aluno.objects.create(
            nome="Maria Santos",
            serie="2º Ano",
            sexo="F"
        )
    
    def test_listar_alunos(self):
        url = reverse('students:listar')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_buscar_aluno(self):
        url = reverse('students:buscar', kwargs={'pk': self.aluno.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "Maria Santos")
    
    def test_excluir_aluno(self):
        url = reverse('students:excluir', kwargs={'pk': self.aluno.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Aluno.objects.filter(pk=self.aluno.pk).exists())