# Generated by Django 4.2.6 on 2023-11-28 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0026_alter_faktor_takhfif_alter_takhfif_darsad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faktor',
            name='pardakht',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]