# Generated by Django 4.2.6 on 2023-12-26 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0036_faktor_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faktor',
            name='products',
        ),
    ]
