# Generated by Django 4.2.6 on 2023-11-28 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0022_alter_faktor_pardakht_alter_faktor_sum_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfaktor',
            name='priceJam',
        ),
        migrations.RemoveField(
            model_name='productfaktor',
            name='tedad',
        ),
    ]
