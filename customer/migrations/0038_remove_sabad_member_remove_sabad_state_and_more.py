# Generated by Django 4.2.6 on 2023-12-27 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0037_remove_faktor_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sabad',
            name='member',
        ),
        migrations.RemoveField(
            model_name='sabad',
            name='state',
        ),
        migrations.DeleteModel(
            name='ProductSabad',
        ),
        migrations.DeleteModel(
            name='Sabad',
        ),
    ]