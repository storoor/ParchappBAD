# Generated by Django 4.1.6 on 2023-04-24 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0016_alter_lugar_categoria_alter_lugar_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='foto',
            field=models.ImageField(upload_to='Parcha-App/images/'),
        ),
    ]
