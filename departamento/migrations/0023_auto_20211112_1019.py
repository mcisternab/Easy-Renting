# Generated by Django 2.2.8 on 2021-11-12 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0022_auto_20211112_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendo',
            name='fecha_entrada',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='arriendo',
            name='fecha_salida',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio'),
        ),
    ]
