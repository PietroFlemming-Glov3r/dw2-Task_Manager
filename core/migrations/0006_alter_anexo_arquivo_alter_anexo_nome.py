# Generated by Django 5.1.2 on 2024-11-19 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_tarefa_prazo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexo',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='anexos/'),
        ),
        migrations.AlterField(
            model_name='anexo',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
