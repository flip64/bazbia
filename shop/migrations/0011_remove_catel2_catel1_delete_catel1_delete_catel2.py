# Generated by Django 4.2.6 on 2023-12-27 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catel2',
            name='catel1',
        ),
        migrations.DeleteModel(
            name='CateL1',
        ),
        migrations.DeleteModel(
            name='CateL2',
        ),
    ]