# Generated by Django 3.2.9 on 2021-12-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('nascimento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'FEMININO'), ('M', 'MASCULINO')], max_length=1)),
                ('estado', models.CharField(choices=[('RJ', 'RIO DE JANEIRO'), ('SP', 'SAO PAULO')], max_length=2)),
                ('municipio', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=30)),
                ('CEP', models.CharField(max_length=9)),
                ('endereco', models.TextField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'cadastro',
            },
        ),
    ]
