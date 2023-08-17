# Generated by Django 4.2.4 on 2023-08-16 06:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('relaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCombustible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('Gasolina', 'Gasolina'), ('Gas', 'Gas'), ('Diesel', 'Diesel'), ('Biodiesel', 'Biodiesel')], max_length=255, verbose_name='Tipo Combustible')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
        ),
        migrations.AddField(
            model_name='fabricante',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fabricante',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AddField(
            model_name='modeloauto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modeloauto',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AddField(
            model_name='modeloauto',
            name='tipo_combustible',
            field=models.ManyToManyField(to='relaciones.tipocombustible'),
        ),
    ]
