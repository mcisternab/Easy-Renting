# Generated by Django 2.2.8 on 2021-11-27 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0030_auto_20211121_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actain',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio'),
        ),
        migrations.AlterField(
            model_name='actaout',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio'),
        ),
        migrations.AlterField(
            model_name='arriendo',
            name='departamento',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='arriendo',
            name='zona',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio'),
        ),
    ]
