# Generated by Django 4.0.5 on 2022-06-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula_imo', models.IntegerField(max_length=8)),
                ('rua_imo', models.CharField(max_length=2)),
                ('cep_imo', models.CharField(max_length=9)),
                ('bairro_imo', models.CharField(max_length=50)),
                ('cidade_imo', models.CharField(max_length=30)),
                ('uf_imo', models.CharField(max_length=2)),
                ('tamanho_imo', models.IntegerField(max_length=100)),
                ('comodos_imo', models.CharField(max_length=50)),
                ('garagem_imo', models.CharField(max_length=50)),
                ('valor_imo', models.IntegerField(max_length=100)),
                ('tipo_imo', models.CharField(max_length=50)),
                ('status_imo', models.CharField(max_length=50)),
            ],
        ),
    ]
