# Generated by Django 4.2.6 on 2023-12-25 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='poshak', unique=True),
            preserve_default=False,
        ),
    ]
