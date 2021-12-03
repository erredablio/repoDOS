from django.contrib import admin
from core.models import Cadastro

# Register your models here.

class CadastroAdmin(admin.ModelAdmin):
    list_field = ('id', 'nome', 'sobrenome', 'nascimento', 'sexo', 'estado', 'municipio', 'bairro', 'CEP', 'endereco', 'numero', 'complemento')
admin.site.register(Cadastro, CadastroAdmin)