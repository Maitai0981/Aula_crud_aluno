from rest_framework import serializers
from .models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    imagemBase64 = serializers.SerializerMethodField()
    
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'serie', 'sexo', 'data', 'imagem', 'imagemBase64']
        extra_kwargs = {
            'imagem': {'write_only': True}
        }
    
    def get_imagemBase64(self, obj):
        """Retorna a imagem em base64 para o frontend"""
        return obj.get_imagem_base64()
    
    def validate_nome(self, value):
        """Valida se o nome não está vazio"""
        if not value or not value.strip():
            raise serializers.ValidationError("O nome é obrigatório.")
        return value.strip()


class AlunoCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'serie', 'sexo', 'data', 'imagem']
    
    def validate_nome(self, value):
        """Valida se o nome não está vazio"""
        if not value or not value.strip():
            raise serializers.ValidationError("O nome é obrigatório.")
        return value.strip()