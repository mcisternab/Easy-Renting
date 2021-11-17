# Generated by Django 2.2.8 on 2021-11-15 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departamento', '0026_auto_20211114_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actain',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio'),
        ),
        migrations.CreateModel(
            name='ActaOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conforme', models.BooleanField()),
                ('multa', models.BooleanField()),
                ('transporte', models.BooleanField()),
                ('condiciones', models.CharField(max_length=50)),
                ('problemas', models.CharField(max_length=50)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Departamento')),
                ('first_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio')),
            ],
        ),
    ]
