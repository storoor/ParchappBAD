# Generated by Django 4.1.6 on 2023-05-03 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0026_alter_lugar_punt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lugar',
            name='punt',
        ),
    ]
