from django.db import models
from django.utils import timezone
import base64


class Aluno(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('OUTRO', 'Outro'),
    ]
    
    nome = models.CharField(max_length=200, verbose_name='Nome')
    serie = models.CharField(max_length=50, blank=True, null=True, verbose_name='Série')
    sexo = models.CharField(
        max_length=10, 
        choices=SEXO_CHOICES, 
        blank=True, 
        null=True, 
        verbose_name='Sexo'
    )
    imagem = models.ImageField(
        upload_to='alunos/', 
        blank=True, 
        null=True, 
        verbose_name='Foto'
    )
    data = models.DateField(default=timezone.now, verbose_name='Data de Cadastro')
    
    class Meta:
        db_table = 'tb_alunos'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    def tem_imagem(self):
        return bool(self.imagem)
    
    def get_imagem_base64(self):
        """Retorna a imagem em formato base64 para o frontend"""
        if self.imagem:
            try:
                with self.imagem.open('rb') as img_file:
                    img_data = img_file.read()
                    img_base64 = base64.b64encode(img_data).decode('utf-8')
                    return f"data:image/jpeg;base64,{img_base64}"
            except Exception:
                return None
        return None