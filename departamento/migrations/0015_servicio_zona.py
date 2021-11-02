# Generated by Django 2.2.8 on 2021-10-19 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0014_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='zona',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='departamento.Zona'),
            preserve_default=False,
        ),
    ]