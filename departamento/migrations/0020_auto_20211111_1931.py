# Generated by Django 2.2.8 on 2021-11-11 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0019_auto_20211023_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio'),
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Zona')),
            ],
        ),
    ]