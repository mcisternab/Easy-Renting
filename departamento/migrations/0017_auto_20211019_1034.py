# Generated by Django 2.2.8 on 2021-10-19 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0016_auto_20211019_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiposervicio',
            old_name='Servicio',
            new_name='tipo',
        ),
    ]
