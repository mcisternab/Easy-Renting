# Generated by Django 2.2.8 on 2021-10-19 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0017_auto_20211019_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio'),
        ),
    ]