# Generated by Django 4.1.5 on 2023-02-07 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0004_cliente_email_alter_pedalreparar_envio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentaPropio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.cliente')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.stockpropio')),
            ],
        ),
        migrations.CreateModel(
            name='PedalClon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clon_de', models.CharField(max_length=80)),
                ('mods', models.TextField()),
                ('envio', models.BooleanField()),
                ('precio', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.cliente')),
            ],
        ),
    ]