# Generated by Django 4.2.6 on 2023-11-30 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0028_takhfif_maximum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faktor',
            name='takhfif',
        ),
    ]
