# Generated by Django 4.1.6 on 2023-03-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0009_alter_lugares_lvleconomico_alter_lugares_zona_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lugares',
            name='cat',
        ),
        migrations.AddField(
            model_name='lugares',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Discoteca', 'Discoteca'), ('Restaurante', 'Restaurante'), ('Mirador', 'Mirador')], max_length=50),
        ),
        migrations.AlterField(
            model_name='lugares',
            name='edad',
            field=models.CharField(blank=True, choices=[('menor de edad', 'menor de edad'), ('mayor de edad', 'mayor de edad')], max_length=50, null=True),
        ),
    ]
