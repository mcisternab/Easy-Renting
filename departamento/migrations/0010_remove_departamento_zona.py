# Generated by Django 2.2.8 on 2021-10-17 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0009_auto_20211017_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='zona',
        ),
    ]