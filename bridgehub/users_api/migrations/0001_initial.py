# Generated by Django 3.2.13 on 2022-06-18 16:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(code='nomatch', message='Telefone Inválido', regex='^\\([1-9]{2}\\) (?:[2-8]|9[1-9])[0-9]{3}\\-[0-9]{4}$')])),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['nome'],
            },
        ),
    ]