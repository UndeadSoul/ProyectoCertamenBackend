# Generated by Django 4.2.16 on 2024-11-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_masadisp_alter_contenido_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='dough',
            field=models.ManyToManyField(to='crud.masadisp', verbose_name='Masa'),
        ),
    ]