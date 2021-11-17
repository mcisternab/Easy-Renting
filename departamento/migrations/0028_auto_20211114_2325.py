# Generated by Django 2.2.8 on 2021-11-15 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0027_auto_20211114_2325'),
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
            model_name='servicio',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio'),
        ),
    ]
