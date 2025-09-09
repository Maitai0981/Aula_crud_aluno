from django.contrib import admin
from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'serie', 'sexo', 'data', 'tem_imagem']
    list_filter = ['sexo', 'serie', 'data']
    search_fields = ['nome', 'serie']
    date_hierarchy = 'data'
    ordering = ['nome']
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'serie', 'sexo')
        }),
        ('Foto', {
            'fields': ('imagem',)
        }),
        ('Data', {
            'fields': ('data',)
        }),
    )
    
    def tem_imagem(self, obj):
        return obj.tem_imagem()
    tem_imagem.boolean = True
    tem_imagem.short_description = 'Tem Foto'