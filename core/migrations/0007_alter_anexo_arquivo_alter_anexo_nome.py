# Generated by Django 5.1.2 on 2024-11-19 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_anexo_arquivo_alter_anexo_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexo',
            name='arquivo',
            field=models.FileField(upload_to='anexos/'),
        ),
        migrations.AlterField(
            model_name='anexo',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
