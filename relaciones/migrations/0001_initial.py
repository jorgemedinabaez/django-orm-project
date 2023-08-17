# Generated by Django 4.2.4 on 2023-08-16 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre fabricante')),
            ],
        ),
        migrations.CreateModel(
            name='ModeloAuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Modelo')),
                ('fabricante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='relaciones.fabricante')),
            ],
        ),
    ]
