# Generated by Django 4.2.6 on 2023-12-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_exelefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exelefile',
            name='file',
            field=models.FileField(upload_to='upload/exel/%Y/%m/%d'),
        ),
    ]