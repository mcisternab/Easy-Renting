# Generated by Django 2.2.8 on 2021-11-12 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0020_auto_20211111_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Tiposervicio'),
        ),
        migrations.CreateModel(
            name='Arriendo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=20)),
                ('apellido_cliente', models.CharField(max_length=20)),
                ('email_cliente', models.EmailField(max_length=254)),
                ('usuario_cliente', models.CharField(max_length=20)),
                ('cantidad_personas', models.IntegerField()),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('precio', models.IntegerField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Departamento')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Zona')),
            ],
        ),
    ]