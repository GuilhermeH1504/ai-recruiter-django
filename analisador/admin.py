from django.contrib import admin
from .models import AnaliseCurriculo

# Register your models here.

@admin.register(AnaliseCurriculo)
class AnaliseCurriculoAdmin(admin.ModelAdmin):
    list_display =  ('nome_vaga', 'criado_em')
    search_fields =  ('nome_vaga', 'analise')
