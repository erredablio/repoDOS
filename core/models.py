from django.db import models

# Create your models here.

class Cadastro(models.Model):
    choice_sexo = [
        ('F', 'FEMININO'),
        ('M', 'MASCULINO'),
    ]

    choice_estado = [
        ('RJ', 'RIO DE JANEIRO'),
        ('SP', 'SAO PAULO')
    ]

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=choice_sexo)
    estado = models.CharField(max_length=2, choices=choice_estado)
    municipio = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    CEP = models.CharField(max_length=9)
    endereco = models.TextField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'cadastro'

    def __str__(self):
        return self.nome
