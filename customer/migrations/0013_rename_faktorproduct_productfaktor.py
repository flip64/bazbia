# Generated by Django 4.2.6 on 2023-11-26 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('customer', '0012_rename_listprudoct_faktorproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FaktorProduct',
            new_name='ProductFaktor',
        ),
    ]