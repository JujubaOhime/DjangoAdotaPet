from django.contrib import admin

from autenticacao.models import PetOwner
from .models import Pet



class PetAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'disponivel', 'estado', 'cidade', 'sexo', 'imagem']
    search_fields = ['nome', 'estado', 'cidade']
    list_filter = ['categoria', 'estado']
    list_editable = ['categoria', 'sexo', 'disponivel', 'imagem', 'sexo']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Pet, PetAdmin)