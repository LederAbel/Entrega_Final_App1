# Generated by Django 4.1.5 on 2023-02-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_ventapropio_pedalclon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedalreparar',
            name='presupuesto',
            field=models.IntegerField(default=6000),
        ),
    ]