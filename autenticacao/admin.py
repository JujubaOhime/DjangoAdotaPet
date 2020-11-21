from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'genero', 'data_cadastro', 'estado', 'cidade', 'cpf', 'rg']
    search_fields = ['estado', 'cidade']
    list_filter = [ 'estado']

admin.site.register(Profile, ProfileAdmin)