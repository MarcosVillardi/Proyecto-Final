# Generated by Django 4.2.1 on 2023-06-27 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_cliente_alter_garaje_comentarios_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='garaje',
            options={'verbose_name': 'Garaje', 'verbose_name_plural': 'Garajes'},
        ),
        migrations.AlterModelOptions(
            name='reserva',
            options={'verbose_name': 'Reserva', 'verbose_name_plural': 'Reservas'},
        ),
    ]
