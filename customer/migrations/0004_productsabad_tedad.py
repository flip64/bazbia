# Generated by Django 4.2.6 on 2023-11-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_remove_sabad_product_sabad_mablag_productsabad'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsabad',
            name='tedad',
            field=models.IntegerField(default=1),
        ),
    ]
