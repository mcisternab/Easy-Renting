# Generated by Django 2.2.8 on 2021-12-06 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_arriendo_precio_final'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_compra', models.CharField(max_length=20)),
                ('numero_tarjeta', models.IntegerField()),
                ('titular_tarjeta', models.CharField(max_length=100)),
                ('expira', models.CharField(max_length=20)),
                ('cvc', models.CharField(max_length=8)),
            ],
        ),
    ]
