# Generated by Django 4.2.6 on 2023-11-26 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('customer', '0010_alter_listprudoct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsabad',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AlterField(
            model_name='productsabad',
            name='sabad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.sabad'),
        ),
        migrations.AlterField(
            model_name='sabad',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.member'),
        ),
    ]