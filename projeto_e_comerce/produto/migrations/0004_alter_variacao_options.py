# Generated by Django 3.2.7 on 2021-09-17 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_variacao_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variável', 'verbose_name_plural': 'Variações'},
        ),
    ]
